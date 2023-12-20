main:
	addi sp, sp, -24
	sw x1, 20(sp)
	sw fp, 16(sp)
	addi fp, sp, 20
.start:
	addi x6, x0, 0
	sw x6, -8(fp)
	addi x6, x0, 10
	sw x6, -12(fp)
	addi x6, x0, 1
	sw x6, -16(fp)
.loop:
	lw x5, -8(fp)
	lw x6, -12(fp)
	bge x5, x6, .ge1
	addi x6, x0, 0
	sw x6, -20(fp)
	jal x0, .exit_cond1
.ge1:
	addi x6, x0, 1
	sw x6, -20(fp)
.exit_cond1:
	add x0, x0, x0
	lw x5, -8(fp)
	lw x6, -16(fp)
	add x7, x5, x6
	sw x7, -8(fp)
	addi x6, x0, 1
	sw x6, -24(fp)
	lw x5, -20(fp)
	lw x6, -24(fp)
	beq x5, x6, .exit
	jal x0, .loop
.exit:
	lw fp, 16(sp)
	lw x1, 20(sp)
	addi sp, sp, 24
	jalr x0, x1, 0 
