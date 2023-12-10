import json
from util.util import *

'''
Notes about classes / structure:

Hierarchy for a Bril Program
-List of Bril Functions

Hierarchy for Bril Functions
-Args
-RetVal
-Body (List of BrilInsns)

Heierarchy for Bril Instructions
 - Label
 - BrilInsn
    - ConstInsn
        - IntegerLiteral
        - BooleanLiteral
    - ValueOperationInsn
        - IntegerMath
            - Add
            - Mul
            - Sub
            - Div
        - RelationalMath
            - Eq
            - Lt
            - Gt
            - Le
            - Ge
        - BooleanMath
            - Not
            - And
            - Or
        - Function call (w and without args)
        - Id
    - EffectOperationInsn
        - Jump
        - Branch
        - Procedure call (w and without args)
        - Ret
  - DummyInsn
      - Bril instructions that we are ignoring -> basically no-ops (print, memory, etc.)

Hierarchy for RISC-V IR Functions
-Label
-Args
-RetVal
-Body (List of RISCV_IR_INSN)

Hierarchy for RISC-V IR Instructions:
- Label
- RISCV_IR_INSN
    - RegRegInsn
        - ADD
        - MUL
        - SUB
        - DIV
        - AND
        - OR
        - XOR
        - SLT
        - SLTU
        - SRA
        - SRL
        - SLL

    - RegImmInsn
        - ADDI
        - ANDI
        - ORI
        - XORI
        - SLTI
        - SLTIU
        - SRAI
        - SRLI
        - SLLI
        - LUI
        - AUIPC

    - Memory
        -LW
        -SW

    - Conditional Branch
        - BEQ
        - BNE
        - BLT
        - BLTU
        - BGEU

    - Jump
        - JAL
        - JALR
'''
def main(): # TODO: Figure out what's going on with jump instructions
  program = json.load(sys.stdin)
#   file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\final_project\\test\\trivial-reg-alloc\\nonRV_branch.json')
#   program = json.load(file)

  # Preprocessing
  insert_labels(program)
  mangle(program)
  
  # Lower to RISC-V
  lower(program)

  # TODO: Write RISC-V IR to output file
  # json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()