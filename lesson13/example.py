import z3
import lark

GRAMMAR= """
?start: sum
    | sum "?" sum ":" sum     -> if

?sum: term
    | sum "+" term          -> add
    | sum "-" term          -> sub

?term: item
    | term "*" item         -> mul
    | term  "/" item        -> div
    | term ">>" item        -> shr
    | term "<<" item        -> shl

?item: NUMBER               -> num
    | "-" item              -> neg
    | CNAME                 -> var
    | "(" start ")"

%import common.NUMBER
%import common.WS
%import common.CNAME
%ignore WS
""".strip()


def solve(phi):
    s = z3.Solver()
    s.add(phi)
    s.check()
    return s.model()

def interp(tree, lookup):
    op = tree.data
    poss_ops = ['add', 'mul', 'sub', 'div', 'shl', 'shr']
    if op in poss_ops:
        lhs = interp(tree.children[0], lookup)
        rhs = interp(tree.children[1], lookup)
        if op == 'add':
            return lhs + rhs
        elif op == 'mul':
            return lhs * rhs
        elif op == 'sub':
            return lhs - rhs
        elif op == 'div':
            return lhs / rhs
        elif op == 'shl':
            return lhs << rhs
        elif op == 'shr':
            return lhs >> rhs
    elif op == 'neg':   # Negation
        sub = interp(tree.children[0], lookup)
        return -sub
    elif op == 'num':   # Literal
        return int(tree.children[0])
    elif op == 'var':   # Variable lookup
        return lookup(tree.children[0])
    elif op == 'if':
        cond = interp(tree.children[0], lookup)
        true_expr = interp(tree.children[1], lookup)
        false_expr = interp(tree.children[2], lookup)
        return (cond != 0) * true_expr + (cond == 0) * false_expr     # if true, return true expression; if false, return false expression

def z3_expr(tree, vars=None):
    """Create a Z3 expression from a tree.

    Return the Z3 expression and a dict mapping variable names to all
    free variables occurring in the expression. All variables are
    represented as BitVecs of width 8. Optionally, `vars` can be an
    initial set of variables.
    """

    vars = dict(vars) if vars else {}

    # Lazily construct a mapping from names to variables.
    def get_var(name):
        if name in vars:
            return vars[name]
        else:
            v = z3.BitVec(name, 8)
            vars[name] = v
            return v

    return interp(tree, get_var), vars

if __name__ == '__main__':
    parser = lark.Lark(GRAMMAR)
    slow_prog, vars1 = z3_expr(parser.parse("x * 10"))
    fast_prog, vars2 = z3_expr(parser.parse("x << h1 + x << h2"), vars1)

    plain_vars = {
        k:v for k, v in vars1.items()
        if not k.startswith('h')
    }

    goal = z3.ForAll(
        list(plain_vars.values()),
        slow_prog == fast_prog
    )

    print(solve(goal))

    # env = { 'x': 2, 'y': 9}
    tree = parser.parse(" (x*3) << y")
    # print(interp(tree, lambda v: env[v]))
    # print(interp(tree, lambda v: z3.BitVec(v, 8)))


    # x * 2
    # x << ??
    
    # x = z3.BitVec('x',8)    # x is an 8-bit vector
    # slow_expr = x * 2

    # h = z3.BitVec('h',8)    # ??
    # fast_expr = x << h      # what is the h that makes the fast_expr equivalent to the slow_expr?

    # form = z3.ForAll([x], slow_expr == fast_expr)
    # print(solve(form))

    # a = z3.BitVec('a',8)
    # b = z3.BitVec('b',8)

    # form = z3.ForAll([a], 128 % a == 0 )
    # print(solve(form))

    # formula = (z3.Int('x') / 7) == 6

    # y = z3.BitVec('y',8)
    # print(solve(y << 3 == 40))
    # print(solve(formula))

    # z = z3.Int('z')
    # n = z3.Int('n')
    # print(solve(z3.ForAll([z], z*n  == z )))  # for all z, z*n == z. What is n?
