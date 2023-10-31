def main():
  pass

if __name__ == "__main__":
    main()

'''
Notes about classes / structure:

Heirarchy for Bril Instructions
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

'''
