main:
	addi sp, sp, -20
	sw x1, 16(sp)
	sw fp, 12(sp)
	addi fp, sp, 16
	addi x6, x0, 99
	sw x6, -12(fp)
	lw x6, -12(fp)
	add a0, x0, x6
	jal x1, no_effect
	add x7, a0, x0
	sw x7, -16(fp)
	lw fp, 12(sp)
	lw x1, 16(sp)
	addi sp, sp, 20
	jalr x0, x1, 0 
f:
	addi sp, sp, -16
	sw x1, 12(sp)
	sw fp, 8(sp)
	addi fp, sp, 12
	sw s1, 4(sp)
	add x7, x0, a0
	sw x7, -12(fp)
	lw x6, -12(fp)
	add a0, x0, x6
	jal x1, g
	add x7, a0, x0
	sw x7, -16(fp)
	lw x5, -16(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s1, 4(sp)
	lw fp, 8(sp)
	lw x1, 12(sp)
	addi sp, sp, 16
	jalr x0, x1, 0 
g:
	addi sp, sp, -12
	sw x1, 8(sp)
	sw fp, 4(sp)
	addi fp, sp, 8
	sw s1, 0(sp)
	add x7, x0, a0
	sw x7, -8(fp)
	lw x5, -8(fp)
	lw x6, -8(fp)
	mul x7, x5, x6
	sw x7, -12(fp)
	lw x5, -12(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s1, 0(sp)
	lw fp, 4(sp)
	lw x1, 8(sp)
	addi sp, sp, 12
	jalr x0, x1, 0 
