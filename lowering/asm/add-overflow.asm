main:
	addi sp, sp, 0xFFFFFFFC
	addi sp, sp, -44
	sw x1, 40(sp)
	sw fp, 36(sp)
	addi fp, sp, 40
	addi x6, x0, 1
	sw x6, -16(fp)
	addi x6, x0, 2
	sw x6, -20(fp)
	addi x6, x0, 62
	sw x6, -24(fp)
	lw x6, -20(fp)
	add a0, x0, x6
	lw x6, -24(fp)
	add a1, x0, x6
	jal x1, pow
	add x7, a0, x0
	sw x7, -28(fp)
	nop
	lw x5, -28(fp)
	lw x6, -16(fp)
	sub x7, x5, x6
	sw x7, -32(fp)
	lw x5, -28(fp)
	lw x6, -32(fp)
	add x7, x5, x6
	sw x7, -36(fp)
	nop
	lw x5, -36(fp)
	lw x6, -16(fp)
	add x7, x5, x6
	sw x7, -40(fp)
	nop
	lw fp, 36(sp)
	lw x1, 40(sp)
	addi sp, sp, 44
	jalr x0, x1, 0 
pow:
	addi sp, sp, -24
	sw x1, 20(sp)
	sw fp, 16(sp)
	addi fp, sp, 20
	sw s1, 12(sp)
	sw s2, 8(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, a1, 0
	sw x6, -12(fp)
	addi x6, x0, 1
	sw x6, -16(fp)
	addi x6, x0, 1
	sw x6, -20(fp)
.loop:
	lw x5, -12(fp)
	lw x6, -20(fp)
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
	beq x5, x6, .ret
	jal x0, .body
.body:
	lw x5, -16(fp)
	lw x6, -8(fp)
	mul x7, x5, x6
	sw x7, -16(fp)
	lw x5, -12(fp)
	lw x6, -20(fp)
	sub x7, x5, x6
	sw x7, -12(fp)
	jal x0, .loop
.ret:
	lw x5, -16(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s2, 8(sp)
	lw s1, 12(sp)
	lw fp, 16(sp)
	lw x1, 20(sp)
	addi sp, sp, 24
	jalr x0, x1, 0 
