# Lowering System Architecture

## Representing Bril Programs

### Bril Functions

- Each Bril program is structured as a list of Bril functions

- Each Bril function has:
  - Zero or more arguments passed in
  - Zero or more return values
  - A function body (which is just a list of Bril instructions)
- We represent Bril functions as a list of BrilInsn instances

### Class Heierarchy for BrilInsn

- Label # TODO: Circle back to this
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

## RISC-V IR

- We use a 1-to-N mapping of Bril instructions to RISC-V IR instructions
- Each Bril instruction is mapped to the sequence of RISC-V IR instructions shown in Table 1 below:
  - TODO: Add in translation table

- Like Bril, each RISC-V IR (RVIR) program is structured as a list of functions
- Each RVIR function has:
  - Zero or more arguments passed in
  - Zero or more return values
  - A function body (which is just a list of RVIR instructions)
- We represent RVIR functions as a list of RVIRInsn instances

### Class Heierarchy for RVIRInsn

- Label # TODO: Circle back to this
- RVIRInsn
  - RVIRRegRegInsn
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

  - RVIRRegImmInsn
    - ADDI
    - ANDI
    - ORI
    - XORI
    - SLTI
    - SLTIU
    - SRAI
    - SRLI
    - SLLI

  - RVIRSpecialRegImmInsn
    - LUI
    - AUIPC

  - RVIRMemInsn
    - LW
    - SW

  - RVIRBranchInsn
    - BEQ
    - BNE
    - BLT
    - BLTU
    - BGEU

  - RVIRJumpInsn
    - JAL
    - JALR

  - RVIRNopInsn
    - NOP

## TODO: Include diagram illustrating progressive lowering from Bril->RVIR->RISC-V

## TODO: Include other sections
