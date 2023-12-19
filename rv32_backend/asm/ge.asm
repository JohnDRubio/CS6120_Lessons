main:
	addi sp, sp, -20
	sw x1, 16(sp)
	sw fp, 12(sp)
	addi fp, sp, 16
	addi x6, x0, 4
	sw x6, -8(fp)
	addi x6, x0, 10
	sw x6, -12(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	bge x5, x6, .ge1
	addi x6, x0, 0
	sw x6, -16(fp)
	jal x0, .exit_cond1
.ge1:
	addi x6, x0, 1
	sw x6, -16(fp)
.exit_cond1:
	lw fp, 12(sp)
	lw x1, 16(sp)
	addi sp, sp, 20
	jalr x0, x1, 0 
