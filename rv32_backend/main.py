import json
from util.util import *

def main():
  # Read in source Bril program
  program = json.load(sys.stdin)

  # Lower to RISC-V
  lower(program)

if __name__ == "__main__":
    main()