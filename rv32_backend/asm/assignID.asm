main:
	addi sp, sp, -40
	sw x1, 36(sp)
	sw fp, 32(sp)
	addi fp, sp, 36
	addi x6, x0, 1
	sw x6, -8(fp)
	addi x6, x0, 2
	sw x6, -12(fp)
	addi x6, x0, 0
	sw x6, -16(fp)
	addi x6, x0, 1
	sw x6, -20(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -28(fp)
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -32(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -36(fp)
	lw fp, 32(sp)
	lw x1, 36(sp)
	addi sp, sp, 40
	jalr x0, x1, 0 
