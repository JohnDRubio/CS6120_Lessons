import itertools
import json
import sys
import blocks

'''
Trivial Dead Code Elimination: Optimization #1
    If a variable, v, is def'd but never used (and the def has no side effects),
    remove def(v).

    Example:
        a: int = const 4                    a: int = const 4
        b: int = const 2                    b: int = const 2
        c: int = const 1        --->        d: int = add a b
        d: int = add a b                    print d
        e: int = add c d
        print d
'''

def tdce_opt1(func):
    # print(func['instrs'][0])
    changed = True
    while changed:
        changed = False
        remove = []
        used = []
        defined = []
        for insn in func['instrs']:
            # print(insn)
            if 'dest' in insn:
                defined.append(insn['dest'])
            if 'args' in insn:
                for var in insn['args']:
                    used.append(var)
        # pass 2: Any insn that's been def'd but never used gets removed
        for insn in func['instrs']:
            if 'dest' in insn and insn['dest'] not in used:
                remove.append(insn)  
                changed = True              
        func['instrs'] = [ x for x in func['instrs'] if x not in remove ]
    return func['instrs']

'''
Trivial Dead Code Elimination: Optimization #2
    Within a basic block, if a variable, v, is def'd two or more times in a row
    before being used, only keep the most recent def(v) before use(v).

    Example:
        a: int = const 4                    a: int = const 5
        a: int = const 5        --->        print a
        print a
'''
def tdce_opt2(blocks):
    newBlocks = []
    for block in blocks:
        changed = True
        newBlock = block
        last_def = {}
        while changed:
            changed = False
            remove = []
            for insn in newBlock:
                # check for uses
                if 'args' in insn:
                    for a in insn['args']:
                        if a in last_def:
                            del last_def[a]             
                # check for defs
                if 'dest' in insn:
                    if insn['dest'] not in last_def:
                        last_def[insn['dest']] = insn
                    else:
                        remove.append(last_def[insn['dest']])
                        changed = True
                        last_def[insn['dest']] = insn
                        # newBlock = [ x for x in newBlock if x not in remove ]
            newBlock = [ x for x in newBlock if x not in remove ]
        newBlocks.append(newBlock)
    return newBlocks

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        insns = tdce_opt1(func)
        basicBlocks = blocks.formBasicBlocks(insns)
        basicBlocks = tdce_opt2(basicBlocks)
        func['instrs'] = list(itertools.chain(*basicBlocks))
    json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()