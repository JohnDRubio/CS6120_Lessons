main:
	addi sp, sp, -32
	sw x1, 28(sp)
	sw fp, 24(sp)
	addi fp, sp, 28
	sw s1, 20(sp)
	add x7, x0, a0
	sw x7, -8(fp)
	addi x6, x0, 1
	sw x6, -12(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
.cond.0:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	lw x5, -20(fp)
	lw x6, -8(fp)
	blt x5, x6, .lt1
	addi x6, x0, 0
	sw x6, -24(fp)
	jal x0, .exit_cond1
.lt1:
	addi x6, x0, 1
	sw x6, -24(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -28(fp)
	lw x5, -24(fp)
	lw x6, -28(fp)
	beq x5, x6, .true.0
	jal x0, .false.0
.true.0:
	addi x6, x0, True
	sw x6, -32(fp)
	add x0, x0, x0
	jal x0, .exit.0
.false.0:
	addi x6, x0, False
	sw x6, -36(fp)
.exit.0:
	lw s1, 20(sp)
	lw fp, 24(sp)
	lw x1, 28(sp)
	addi sp, sp, 32
	jalr x0, x1, 0 
