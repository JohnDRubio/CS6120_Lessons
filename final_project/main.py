import json
import sys
sys.path.append("../library")
import cfg
import itertools

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
        - Add
        - Mul
        - Sub
        - Div
        - And
        - Or
    - RegImmInsn
        - Addi
        - Subi
        - Xori
    - Conditional Branch
        - Beq
        - Blt
        - Bgt
        - Ble
        - Bge
    - Jump
        - Jump and Link
        - Jump and Link Register
'''

def mangle(vars):
    newVars = []
    for var in vars:
        newVars.append("_"+var)
    return newVars

def main():
  program = json.load(sys.stdin)
  for func in program['functions']:
     blocks = cfg.formBasicBlocks(func['instrs'])
     for block in blocks:
        for insn in block:
            if 'dest' in insn:
                insn['dest'] = mangle([insn['dest']])[0]
            if 'args' in insn:
                insn['args'] = mangle(insn['args'])
     func['instrs'] = list(itertools.chain(*blocks))
  json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()