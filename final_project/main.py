def main():
  pass

if __name__ == "__main__":
    main()

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
        - BooleanMath
            - Eq
            - Lt
            - Gt
            - Le
            - Ge
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
