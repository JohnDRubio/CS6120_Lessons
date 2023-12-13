import json
from util.util import *

def main():
  # Read in source Bril program
  # file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\rv32_backend\\test\\interp\\core\\add-overflow.json')
  # program = json.load(file)
  program = json.load(sys.stdin)
  output_file = set_fileName()

  # Preprocessing
  insert_labels(program)
  mangle(program)
  
  # Lower to RISC-V
  lower(program, output_file)

if __name__ == "__main__":
    main()