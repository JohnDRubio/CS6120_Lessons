main:
	addi sp, sp, -40
	sw x1, 36(sp)
	sw fp, 32(sp)
	addi fp, sp, 36
	sw s1, 28(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, x0, 1
	sw x6, -12(fp)
	addi x6, x0, 2
	sw x6, -16(fp)
	addi x6, x0, 3
	sw x6, -20(fp)
	jal x0, .print
.cond:
	lw x5, -8(fp)
	lw x6, -12(fp)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -24(fp)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -24(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -28(fp)
	lw x5, -24(fp)
	lw x6, -28(fp)
	beq x5, x6, .end
	jal x0, .loop
.loop:
	lw x5, -8(fp)
	lw x6, -16(fp)
	div x7, x5, x6
	sw x7, -32(fp)
	lw x5, -32(fp)
	lw x6, -16(fp)
	mul x7, x5, x6
	sw x7, -36(fp)
	lw x5, -8(fp)
	lw x6, -36(fp)
	beq x5, x6, .eq2
	addi x6, x0, 0
	sw x6, -40(fp)
	jal x0, .exit_cond2
.eq2:
	addi x6, x0, 1
	sw x6, -40(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -44(fp)
	lw x5, -40(fp)
	lw x6, -44(fp)
	beq x5, x6, .even
	jal x0, .odd
.even:
	lw x5, -8(fp)
	lw x6, -16(fp)
	div x7, x5, x6
	sw x7, -8(fp)
	jal x0, .print
.odd:
	lw x5, -8(fp)
	lw x6, -20(fp)
	mul x7, x5, x6
	sw x7, -8(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	add x7, x5, x6
	sw x7, -8(fp)
.print:
	nop
	jal x0, .cond
.end:
	jalr x0, x1, 0 
	lw s1, 28(sp)
	lw fp, 32(sp)
	lw x1, 36(sp)
	addi sp, sp, 40
	jalr x0, x1, 0 
