main:
	addi sp, sp, -24
	sw x1, 20(sp)
	sw fp, 16(sp)
	addi fp, sp, 20
	addi x6, x0, 1
	sw x6, -8(fp)
	addi x6, x0, 2
	sw x6, -12(fp)
	addi x6, x0, 0
	sw x6, -16(fp)
	addi x6, x0, 1
	sw x6, -20(fp)
	lw fp, 16(sp)
	lw x1, 20(sp)
	addi sp, sp, 24
	jalr x0, x1, 0 
