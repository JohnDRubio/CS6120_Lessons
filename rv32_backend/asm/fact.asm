main:
	addi x2, x2, -20
	sw x1, 16(x2)
	sw x8, 12(x2)
	addi x8, x2, 16
	sw x9, 8(x2)
	addi x6, x10, 0
	sw x6, -12(x8)
	lw x6, -12(x8)
	add x10, x0, x6
	jal x1, fact
	add x7, x10, x0
	sw x7, -16(x8)
	add x0, x0, x0
	addi x6, x0, 0
	sw x6, -20(x8)
	lw x9, 8(x2)
	lw x8, 12(x2)
	lw x1, 16(x2)
	addi x2, x2, 20
	jalr x0, x1, 0 
fact:
	addi x2, x2, -52
	sw x1, 48(x2)
	sw x8, 44(x2)
	addi x8, x2, 48
	sw x9, 40(x2)
	addi x6, x10, 0
	sw x6, -12(x8)
	lw x5, -12(x8)
	addi x6, x5, 0
	sw x6, -16(x8)
	addi x6, x0, 0
	sw x6, -20(x8)
	lw x5, -16(x8)
	lw x6, -20(x8)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -24(x8)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -24(x8)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -28(x8)
	lw x5, -24(x8)
	lw x6, -28(x8)
	beq x5, x6, .then.0
	jal x0, .else.0
.then.0:
	addi x6, x0, 1
	sw x6, -32(x8)
	lw x5, -32(x8)
	addi x10, x5, 0
	jalr x0, x1, 0 
.label_0:
	jal x0, .endif.0
.else.0:
	lw x5, -12(x8)
	addi x6, x5, 0
	sw x6, -36(x8)
	lw x5, -12(x8)
	addi x6, x5, 0
	sw x6, -40(x8)
	addi x6, x0, 1
	sw x6, -44(x8)
	lw x5, -40(x8)
	lw x6, -44(x8)
	sub x7, x5, x6
	sw x7, -48(x8)
	lw x6, -48(x8)
	add x10, x0, x6
	jal x1, fact
	add x7, x10, x0
	sw x7, -52(x8)
	lw x5, -36(x8)
	lw x6, -52(x8)
	mul x7, x5, x6
	sw x7, -56(x8)
	lw x5, -56(x8)
	addi x10, x5, 0
	jalr x0, x1, 0 
.endif.0:
	lw x9, 40(x2)
	lw x8, 44(x2)
	lw x1, 48(x2)
	addi x2, x2, 52
	jalr x0, x1, 0 
