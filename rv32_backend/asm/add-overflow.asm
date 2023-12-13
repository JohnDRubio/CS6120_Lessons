pow:
	addi x2, x2, -24
	sw x1, 20(x2)
	sw x8, 16(x2)
	addi x8, x2, 20
	sw x9, 12(x2)
	sw x18, 8(x2)
	addi x6, x10, 0
	sw x6, -8(x8)
	addi x6, x11, 0
	sw x6, -12(x8)
	addi x6, x0, 1
	sw x6, -16(x8)
	addi x6, x0, 1
	sw x6, -20(x8)
.loop:
	lw x5, -12(x8)
	lw x6, -20(x8)
	blt x5, x6, .lt1
	addi x6, x0, 0
	sw x6, -24(x8)
	jal x0, .exit_cond1
.lt1:
	addi x6, x0, 1
	sw x6, -24(x8)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -28(x8)
	lw x5, -24(x8)
	lw x6, -28(x8)
	beq x5, x6, .ret
	jal x0, .body
.body:
	lw x5, -16(x8)
	lw x6, -8(x8)
	mul x7, x5, x6
	sw x7, -16(x8)
	lw x5, -12(x8)
	lw x6, -20(x8)
	sub x7, x5, x6
	sw x7, -12(x8)
	jal x0, .loop
.ret:
	lw x5, -16(x8)
	addi x10, x5, 0
	jalr x0, x1, 0 
	lw x18, 8(x2)
	lw x9, 12(x2)
	lw x8, 16(x2)
	lw x1, 20(x2)
	addi x2, x2, 24
	jalr x0, x1, 0 
main:
	addi x2, x2, -44
	sw x1, 40(x2)
	sw x8, 36(x2)
	addi x8, x2, 40
	addi x6, x0, 1
	sw x6, -16(x8)
	addi x6, x0, 2
	sw x6, -20(x8)
	addi x6, x0, 62
	sw x6, -24(x8)
	lw x6, -20(x8)
	add x10, x0, x6
	lw x6, -24(x8)
	add x11, x0, x6
	jal x1, pow
	add x7, x10, x0
	sw x7, -28(x8)
	add x0, x0, x0
	lw x5, -28(x8)
	lw x6, -16(x8)
	sub x7, x5, x6
	sw x7, -32(x8)
	lw x5, -28(x8)
	lw x6, -32(x8)
	add x7, x5, x6
	sw x7, -36(x8)
	add x0, x0, x0
	lw x5, -36(x8)
	lw x6, -16(x8)
	add x7, x5, x6
	sw x7, -40(x8)
	add x0, x0, x0
	lw x8, 36(x2)
	lw x1, 40(x2)
	addi x2, x2, 44
	jalr x0, x1, 0 
