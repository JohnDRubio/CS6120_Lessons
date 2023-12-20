main:
	addi sp, sp, -24
	sw x1, 20(sp)
	sw fp, 16(sp)
	addi fp, sp, 20
	addi x6, x0, 1
	sw x6, -12(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	jal x1, no_effect
	add x7, a0, x0
	sw x7, -20(fp)
	lw fp, 16(sp)
	lw x1, 20(sp)
	addi sp, sp, 24
	jalr x0, x1, 0 
no_effect:
	addi sp, sp, -8
	sw x1, 4(sp)
	sw fp, 0(sp)
	addi fp, sp, 4
	sw s1, -4(sp)
	add x7, x0, a0
	sw x7, -8(fp)
	lw x5, -8(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s1, -4(sp)
	lw fp, 0(sp)
	lw x1, 4(sp)
	addi sp, sp, 8
	jalr x0, x1, 0 
