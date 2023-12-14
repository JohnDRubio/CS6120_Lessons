import json
from util.util import *

def main():
  # Read in source Bril program
  program = json.load(sys.stdin)
  output_file = set_fileName()

  # Preprocessing
  insert_labels(program)
  mangle(program)
  
  # Lower to RISC-V
  lower(program, output_file)

if __name__ == "__main__":
    main()