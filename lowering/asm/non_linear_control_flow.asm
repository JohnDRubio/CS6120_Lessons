main:
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
	jal x0, .start
.end:
	nop
	nop
	jalr x0, x1, 0 
.l_1_3:
	jal x0, .end
.l_1_2:
	addi x6, x0, 0
	sw x6, -16(fp)
	jal x0, .l_1_3
.l_1_1:
	addi x6, x0, 1
	sw x6, -20(fp)
	jal x0, .l_1_3
.l_0_3:
	addi x6, x0, 1
	sw x6, -24(fp)
	lw x5, -12(fp)
	lw x6, -24(fp)
	beq x5, x6, .l_1_1
	jal x0, .l_1_2
.l_0_2:
	addi x6, x0, 2
	sw x6, -28(fp)
	jal x0, .l_0_3
.l_0_1:
	addi x6, x0, 3
	sw x6, -32(fp)
	jal x0, .l_0_3
.start:
	addi x6, x0, 1
	sw x6, -36(fp)
	lw x5, -8(fp)
	lw x6, -36(fp)
	beq x5, x6, .l_0_1
	jal x0, .l_0_2
	lw s2, 8(sp)
	lw s1, 12(sp)
	lw fp, 16(sp)
	lw x1, 20(sp)
	addi sp, sp, 24
	jalr x0, x1, 0 
