main:
	addi sp, sp, -32
	sw x1, 28(sp)
	sw fp, 24(sp)
	addi fp, sp, 28
	addi x6, x0, 1
	sw x6, -8(fp)
	addi x6, x0, 2
	sw x6, -12(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	add x7, x5, x6
	sw x7, -16(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	sub x7, x5, x6
	sw x7, -20(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	mul x7, x5, x6
	sw x7, -24(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	div x7, x5, x6
	sw x7, -28(fp)
	lw fp, 24(sp)
	lw x1, 28(sp)
	addi sp, sp, 32
	jalr x0, x1, 0 
