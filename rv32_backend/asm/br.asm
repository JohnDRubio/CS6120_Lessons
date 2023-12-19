main:
	addi sp, sp, -16
	sw x1, 12(sp)
	sw fp, 8(sp)
	addi fp, sp, 12
	addi x6, x0, 4
	sw x6, -8(fp)
	addi x6, x0, 0
	sw x6, -12(fp)
	addi x6, x0, 1
	sw x6, -16(fp)
	lw x5, -12(fp)
	lw x6, -16(fp)
	beq x5, x6, .there
	jal x0, .here
.here:
	addi x6, x0, 2
	sw x6, -8(fp)
.there:
	add x0, x0, x0
	lw fp, 8(sp)
	lw x1, 12(sp)
	addi sp, sp, 16
	jalr x0, x1, 0 
