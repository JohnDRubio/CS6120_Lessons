import z3

def solve(phi):
  s = z3.Solver()
  s.add(phi)
  if s.check() == z3.sat:
      return s.model()
  else:
      return "No solution found."

# I've been trying to come up with expression that make the solver 
# think for a long time, but I'm only getting things that don't converge
if __name__ == '__main__':
  x = z3.BitVec('x',8)
  # slow_expr = x * 4
  slow_expr = ((x & 0b111) << 2) + ((x + 3) | (x << 1))

  h = z3.BitVec('h',8)
  # fast_expr = x << h
  fast_expr = ((x << h) + (x & h)) & 0xFF

  goal = z3.ForAll([x], slow_expr == fast_expr)
  print(solve(goal))