main:
	addi sp, sp, -20
	sw x1, 16(sp)
	sw fp, 12(sp)
	addi fp, sp, 16
	sw s1, 8(sp)
	add x7, x0, a0
	sw x7, -12(fp)
	lw x6, -12(fp)
	add a0, x0, x6
	jal x1, fact
	add x7, a0, x0
	sw x7, -16(fp)
	add x0, x0, x0
	addi x6, x0, 0
	sw x6, -20(fp)
	lw s1, 8(sp)
	lw fp, 12(sp)
	lw x1, 16(sp)
	addi sp, sp, 20
	jalr x0, x1, 0 
fact:
	addi sp, sp, -52
	sw x1, 48(sp)
	sw fp, 44(sp)
	addi fp, sp, 48
	sw s1, 40(sp)
	add x7, x0, a0
	sw x7, -12(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
	addi x6, x0, 0
	sw x6, -20(fp)
	lw x5, -16(fp)
	lw x6, -20(fp)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -24(fp)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -24(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -28(fp)
	lw x5, -24(fp)
	lw x6, -28(fp)
	beq x5, x6, .then.0
	jal x0, .else.0
.then.0:
	addi x6, x0, 1
	sw x6, -32(fp)
	lw x5, -32(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.label_0:
	jal x0, .endif.0
.else.0:
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -36(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -40(fp)
	addi x6, x0, 1
	sw x6, -44(fp)
	lw x5, -40(fp)
	lw x6, -44(fp)
	sub x7, x5, x6
	sw x7, -48(fp)
	lw x6, -48(fp)
	add a0, x0, x6
	jal x1, fact
	add x7, a0, x0
	sw x7, -52(fp)
	lw x5, -36(fp)
	lw x6, -52(fp)
	mul x7, x5, x6
	sw x7, -56(fp)
	lw x5, -56(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.endif.0:
	lw s1, 40(sp)
	lw fp, 44(sp)
	lw x1, 48(sp)
	addi sp, sp, 52
	jalr x0, x1, 0 
