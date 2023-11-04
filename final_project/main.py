import json
import sys
sys.path.append("../library")
import cfg
import itertools
from BrilInsns import *
# from RVIRInsns import *
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn


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

def mangle_bril_insn(vars):
    newVars = []
    for var in vars:
        newVars.append("_"+var)
    return newVars

def mangle(program):
    for func in program['functions']:
        blocks = cfg.formBasicBlocks(func['instrs'])
        for block in blocks:
            for insn in block:
                if 'dest' in insn:
                    insn['dest'] = mangle_bril_insn([insn['dest']])[0]
                if 'args' in insn:
                    insn['args'] = mangle_bril_insn(insn['args'])
        func['instrs'] = list(itertools.chain(*blocks))
    return program

def main():
  program = json.load(sys.stdin)
  mangle(program)
  # convert each Bril instruction to a BrinInsn object
  # convert each BrilInsn object to N RVIRInsn objects
  json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()