main:
	addi sp, sp, -44
	sw x1, 40(sp)
	sw fp, 36(sp)
	addi fp, sp, 40
	sw s1, 32(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, x0, 1
	sw x6, -12(fp)
	lw x5, -8(fp)
	lw x6, -8(fp)
	mul x7, x5, x6
	sw x7, -16(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
.outer_loop:
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
.inner_loop:
	lw x5, -20(fp)
	lw x6, -20(fp)
	mul x7, x5, x6
	sw x7, -28(fp)
	lw x5, -24(fp)
	lw x6, -24(fp)
	mul x7, x5, x6
	sw x7, -32(fp)
	lw x5, -28(fp)
	lw x6, -32(fp)
	add x7, x5, x6
	sw x7, -36(fp)
	lw x5, -36(fp)
	lw x6, -16(fp)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -40(fp)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -40(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -44(fp)
	lw x5, -40(fp)
	lw x6, -44(fp)
	beq x5, x6, .found
	jal x0, .inner_continue
.found:
	nop
.inner_continue:
	lw x5, -24(fp)
	lw x6, -12(fp)
	add x7, x5, x6
	sw x7, -24(fp)
	lw x5, -24(fp)
	lw x6, -20(fp)
	bge x5, x6, .ge2
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond2
.ge2:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -52(fp)
	lw x5, -48(fp)
	lw x6, -52(fp)
	beq x5, x6, .outer_continue
	jal x0, .inner_loop
.outer_continue:
	lw x5, -20(fp)
	lw x6, -12(fp)
	add x7, x5, x6
	sw x7, -20(fp)
	lw x5, -20(fp)
	lw x6, -8(fp)
	bge x5, x6, .ge3
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond3
.ge3:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond3:
	addi x6, x0, 1
	sw x6, -56(fp)
	lw x5, -48(fp)
	lw x6, -56(fp)
	beq x5, x6, .finish
	jal x0, .outer_loop
.finish:
	lw s1, 32(sp)
	lw fp, 36(sp)
	lw x1, 40(sp)
	addi sp, sp, 44
	jalr x0, x1, 0 
