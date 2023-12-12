main:
	addi sp, sp, -12
	sw x1, 8(sp)
	sw fp, 4(sp)
	addi fp, sp, 8
	sw s1, 0(sp)
	addi x6, a0, 0
	sw x6, -12(fp)
	lw x6, -12(fp)
	add a0, x0, x6
	jal x1, printBinary
	lw s1, 0(sp)
	lw fp, 4(sp)
	lw x1, 8(sp)
	addi sp, sp, 12
	jalr x0, x1, 0 
printBinary:
	addi sp, sp, -36
	sw x1, 32(sp)
	sw fp, 28(sp)
	addi fp, sp, 32
	sw s1, 24(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	addi x6, x0, 0
	sw x6, -20(fp)
	lw x5, -16(fp)
	lw x6, -20(fp)
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
	jal x0, .rec
.rec:
	addi x6, x0, 2
	sw x6, -32(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -32(fp)
	add a1, x0, x6
	jal x1, mod
	add x7, a0, x0
	sw x7, -36(fp)
	lw x5, -16(fp)
	lw x6, -32(fp)
	div x7, x5, x6
	sw x7, -40(fp)
	lw x6, -40(fp)
	add a0, x0, x6
	jal x1, printBinary
	nop
.end:
	lw s1, 24(sp)
	lw fp, 28(sp)
	lw x1, 32(sp)
	addi sp, sp, 36
	jalr x0, x1, 0 
mod:
	addi sp, sp, -20
	sw x1, 16(sp)
	sw fp, 12(sp)
	addi fp, sp, 16
	sw s1, 8(sp)
	sw s2, 4(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, a1, 0
	sw x6, -12(fp)
	lw x5, -8(fp)
	lw x6, -12(fp)
	div x7, x5, x6
	sw x7, -16(fp)
	lw x5, -16(fp)
	lw x6, -12(fp)
	mul x7, x5, x6
	sw x7, -20(fp)
	lw x5, -8(fp)
	lw x6, -20(fp)
	sub x7, x5, x6
	sw x7, -24(fp)
	lw x5, -24(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s2, 4(sp)
	lw s1, 8(sp)
	lw fp, 12(sp)
	lw x1, 16(sp)
	addi sp, sp, 20
	jalr x0, x1, 0 
