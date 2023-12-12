import json
from util.util import *

def main():
#   program = json.load(sys.stdin)
#   file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\final_project\\test\\trivial-reg-alloc\\nonRV_branch.json')
#   file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\final_project\\test\\interp\\mem\\ptr_ret.json')
  file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\final_project\\test\\interp\\core\\add-overflow.json')
  program = json.load(file)

  # Preprocessing
  insert_labels(program)
  mangle(program)
  
  # Lower to RISC-V
  lower(program)

  # TODO: Write RISC-V IR to output file
  # json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()