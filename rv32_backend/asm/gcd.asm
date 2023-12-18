main:
	addi x2, x2, -32
	sw x1, 28(x2)
	sw x8, 24(x2)
	addi x8, x2, 28
	sw x9, 20(x2)
	sw x18, 16(x2)
	add x7, x0, x10
	sw x7, -8(x8)
	add x7, x0, x11
	sw x7, -12(x8)
	addi x6, x0, 0
	sw x6, -16(x8)
	lw x5, -8(x8)
	addi x6, x5, 0
	sw x6, -20(x8)
	lw x5, -12(x8)
	addi x6, x5, 0
	sw x6, -24(x8)
.cmp.val:
	lw x5, -20(x8)
	lw x6, -24(x8)
	blt x5, x6, .lt1
	addi x6, x0, 0
	sw x6, -28(x8)
	jal x0, .exit_cond1
.lt1:
	addi x6, x0, 1
	sw x6, -28(x8)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -32(x8)
	lw x5, -28(x8)
	lw x6, -32(x8)
	beq x5, x6, .if.1
	jal x0, .else.1
.if.1:
	lw x5, -24(x8)
	lw x6, -20(x8)
	sub x7, x5, x6
	sw x7, -36(x8)
	jal x0, .loop.bound
.else.1:
	lw x5, -20(x8)
	lw x6, -24(x8)
	sub x7, x5, x6
	sw x7, -36(x8)
	jal x0, .loop.bound
.loop.bound:
	lw x5, -36(x8)
	lw x6, -16(x8)
	beq x5, x6, .eq2
	addi x6, x0, 0
	sw x6, -40(x8)
	jal x0, .exit_cond2
.eq2:
	addi x6, x0, 1
	sw x6, -40(x8)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -44(x8)
	lw x5, -40(x8)
	lw x6, -44(x8)
	beq x5, x6, .program.end
	jal x0, .update.val
.update.val:
	addi x6, x0, 1
	sw x6, -48(x8)
	lw x5, -28(x8)
	lw x6, -48(x8)
	beq x5, x6, .if.2
	jal x0, .else.2
.if.2:
	lw x5, -36(x8)
	addi x6, x5, 0
	sw x6, -24(x8)
	jal x0, .cmp.val
.else.2:
	lw x5, -36(x8)
	addi x6, x5, 0
	sw x6, -20(x8)
	jal x0, .cmp.val
.program.end:
	add x0, x0, x0
	lw x18, 16(x2)
	lw x9, 20(x2)
	lw x8, 24(x2)
	lw x1, 28(x2)
	addi x2, x2, 32
	jalr x0, x1, 0 
