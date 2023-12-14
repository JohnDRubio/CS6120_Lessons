main:
	addi sp, sp, -32
	sw x1, 28(sp)
	sw fp, 24(sp)
	addi fp, sp, 28
	sw s1, 20(sp)
	sw s2, 16(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, a1, 0
	sw x6, -12(fp)
	addi x6, x0, 0
	sw x6, -16(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
.cmp.val:
	lw x5, -20(fp)
	lw x6, -24(fp)
	blt x5, x6, .lt1
	addi x6, x0, 0
	sw x6, -28(fp)
	jal x0, .exit_cond1
.lt1:
	addi x6, x0, 1
	sw x6, -28(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -32(fp)
	lw x5, -28(fp)
	lw x6, -32(fp)
	beq x5, x6, .if.1
	jal x0, .else.1
.if.1:
	lw x5, -24(fp)
	lw x6, -20(fp)
	sub x7, x5, x6
	sw x7, -36(fp)
	jal x0, .loop.bound
.else.1:
	lw x5, -20(fp)
	lw x6, -24(fp)
	sub x7, x5, x6
	sw x7, -36(fp)
	jal x0, .loop.bound
.loop.bound:
	lw x5, -36(fp)
	lw x6, -16(fp)
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
	beq x5, x6, .program.end
	jal x0, .update.val
.update.val:
	addi x6, x0, 1
	sw x6, -48(fp)
	lw x5, -28(fp)
	lw x6, -48(fp)
	beq x5, x6, .if.2
	jal x0, .else.2
.if.2:
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
	jal x0, .cmp.val
.else.2:
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	jal x0, .cmp.val
.program.end:
	add x0, x0, x0
	lw s2, 16(sp)
	lw s1, 20(sp)
	lw fp, 24(sp)
	lw x1, 28(sp)
	addi sp, sp, 32
	jalr x0, x1, 0 
