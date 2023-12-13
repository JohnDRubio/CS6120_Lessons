.main:
	addi x3, x3, -24
	sw x1, 20(x3)
	sw x8, 16(x3)
	addi x8, x3, 20
	sw x9, 12(x3)
	sw x18, 8(x3)
	addi x6, x10, 0
	sw x6, -8(x8)
	addi x6, x11, 0
	sw x6, -12(x8)
	jal x0, .start
.end:
	jalr x0, x1, 0 
.l_1_3:
	jal x0, .end
.l_1_2:
	addi x6, x0, 0
	sw x6, -16(x8)
	jal x0, .l_1_3
.l_1_1:
	addi x6, x0, 1
	sw x6, -20(x8)
	jal x0, .l_1_3
.l_0_3:
	addi x6, x0, 1
	sw x6, -24(x8)
	lw x5, -12(x8)
	lw x6, -24(x8)
	beq x5, x6, .l_1_1
	jal x0, .l_1_2
.l_0_2:
	addi x6, x0, 2
	sw x6, -28(x8)
	jal x0, .l_0_3
.l_0_1:
	addi x6, x0, 3
	sw x6, -32(x8)
	jal x0, .l_0_3
.start:
	addi x6, x0, 1
	sw x6, -36(x8)
	lw x5, -8(x8)
	lw x6, -36(x8)
	beq x5, x6, .l_0_1
	jal x0, .l_0_2
	lw x18, 8(x3)
	lw x9, 12(x3)
	lw x8, 16(x3)
	lw x1, 20(x3)
	addi x3, x3, 24
	jalr x0, x1, 0 
