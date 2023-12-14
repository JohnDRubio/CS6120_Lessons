# The goal
The goal of this project is to develop a compiler backend which lowers from [Bril](https://capra.cs.cornell.edu/bril/) to RISC-V. Specifically, the target is [TINYRV32IM](https://www.csl.cornell.edu/courses/ece4750/handouts/ece4750-tinyrv-isa.pdf).

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

- BrilInsn
  - BrilLabelInsn
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

- Like Bril, each RISC-V IR (RVIR) program is structured as a list of functions
- Each RVIR function has:
  - Zero or more arguments passed in
  - Zero or more return values
  - A function body (which is just a list of RVIR instructions)
- We represent RVIR functions as a list of RVIRInsn instances

### Class Heierarchy for RVIRInsn

- RVIRInsn
  - RVIRLabelInsn
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

## How to run

`bril2json < path/to/bril/file.bril | python main.py -o optional_file_name.asm`
