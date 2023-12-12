ack:
	addi sp, sp, -56
	sw x1, 52(sp)
	sw fp, 48(sp)
	addi fp, sp, 52
	sw s1, 44(sp)
	sw s2, 40(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	addi x6, a1, 0
	sw x6, -20(fp)
	addi x6, x0, 99
	sw x6, -24(fp)
	addi x6, x0, 0
	sw x6, -28(fp)
	addi x6, x0, 1
	sw x6, -32(fp)
	lw x5, -16(fp)
	lw x6, -28(fp)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -36(fp)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -36(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -40(fp)
	lw x5, -36(fp)
	lw x6, -40(fp)
	beq x5, x6, .m_zero
	jal x0, .m_nonzero
.m_zero:
	lw x5, -20(fp)
	lw x6, -32(fp)
	add x7, x5, x6
	sw x7, -44(fp)
	lw x5, -44(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.m_nonzero:
	lw x5, -20(fp)
	lw x6, -28(fp)
	beq x5, x6, .eq2
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond2
.eq2:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -52(fp)
	lw x5, -48(fp)
	lw x6, -52(fp)
	beq x5, x6, .n_zero
	jal x0, .n_nonzero
.n_zero:
	lw x5, -16(fp)
	lw x6, -32(fp)
	sub x7, x5, x6
	sw x7, -56(fp)
	lw x6, -56(fp)
	add a0, x0, x6
	lw x6, -32(fp)
	add a1, x0, x6
	jal x1, ack
	add x7, a0, x0
	sw x7, -44(fp)
	lw x5, -44(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.n_nonzero:
	lw x5, -16(fp)
	lw x6, -32(fp)
	sub x7, x5, x6
	sw x7, -56(fp)
	lw x5, -20(fp)
	lw x6, -32(fp)
	sub x7, x5, x6
	sw x7, -60(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -60(fp)
	add a1, x0, x6
	jal x1, ack
	add x7, a0, x0
	sw x7, -64(fp)
	lw x6, -56(fp)
	add a0, x0, x6
	lw x6, -64(fp)
	add a1, x0, x6
	jal x1, ack
	add x7, a0, x0
	sw x7, -68(fp)
	lw x5, -68(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s2, 40(sp)
	lw s1, 44(sp)
	lw fp, 48(sp)
	lw x1, 52(sp)
	addi sp, sp, 56
	jalr x0, x1, 0 
main:
	addi sp, sp, -20
	sw x1, 16(sp)
	sw fp, 12(sp)
	addi fp, sp, 16
	sw s1, 8(sp)
	sw s2, 4(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	addi x6, a1, 0
	sw x6, -20(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, ack
	add x7, a0, x0
	sw x7, -24(fp)
	nop
	lw s2, 4(sp)
	lw s1, 8(sp)
	lw fp, 12(sp)
	lw x1, 16(sp)
	addi sp, sp, 20
	jalr x0, x1, 0 
