main:
	addi sp, sp, -88
	sw x1, 84(sp)
	sw fp, 80(sp)
	addi fp, sp, 84
	sw s1, 76(sp)
	sw s2, 72(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	addi x6, a1, 0
	sw x6, -20(fp)
.for.outer.init:
	addi x6, x0, 2
	sw x6, -24(fp)
	lw x5, -16(fp)
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
	beq x5, x6, .true
	jal x0, .false
.true:
	addi x6, x0, 2
	sw x6, -36(fp)
	jal x0, .for.outer.cond
.false:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -36(fp)
.for.outer.cond:
	lw x5, -20(fp)
	lw x6, -36(fp)
	bge x5, x6, .ge2
	addi x6, x0, 0
	sw x6, -40(fp)
	jal x0, .exit_cond2
.ge2:
	addi x6, x0, 1
	sw x6, -40(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -44(fp)
	lw x5, -40(fp)
	lw x6, -44(fp)
	beq x5, x6, .for.outer.body
	jal x0, .for.outer.end
.for.outer.body:
	addi x6, x0, 1
	sw x6, -48(fp)
	lw x5, -48(fp)
	lw x6, -48(fp)
	beq x5, x6, .eq3
	addi x6, x0, 0
	sw x6, -52(fp)
	jal x0, .exit_cond3
.eq3:
	addi x6, x0, 1
	sw x6, -52(fp)
.exit_cond3:
.for.inner.init:
	addi x6, x0, 2
	sw x6, -56(fp)
	addi x6, x0, 2
	sw x6, -60(fp)
.for.inner.cond:
	lw x5, -36(fp)
	lw x6, -60(fp)
	div x7, x5, x6
	sw x7, -64(fp)
	lw x5, -64(fp)
	lw x6, -56(fp)
	bge x5, x6, .ge4
	addi x6, x0, 0
	sw x6, -68(fp)
	jal x0, .exit_cond4
.ge4:
	addi x6, x0, 1
	sw x6, -68(fp)
.exit_cond4:
	addi x6, x0, 1
	sw x6, -72(fp)
	lw x5, -68(fp)
	lw x6, -72(fp)
	beq x5, x6, .for.inner.body
	jal x0, .for.inner.end
.for.inner.body:
	lw x6, -36(fp)
	add a0, x0, x6
	lw x6, -56(fp)
	add a1, x0, x6
	jal x1, mod
	add x7, a0, x0
	sw x7, -76(fp)
	addi x6, x0, 0
	sw x6, -80(fp)
	lw x5, -76(fp)
	lw x6, -80(fp)
	beq x5, x6, .eq5
	addi x6, x0, 0
	sw x6, -84(fp)
	jal x0, .exit_cond5
.eq5:
	addi x6, x0, 1
	sw x6, -84(fp)
.exit_cond5:
	addi x6, x0, 1
	sw x6, -88(fp)
	lw x5, -84(fp)
	lw x6, -88(fp)
	beq x5, x6, .if.inner.body
	jal x0, .if.inner.end
.if.inner.body:
	addi x6, x0, 1
	sw x6, -92(fp)
	addi x6, x0, 2
	sw x6, -96(fp)
	lw x5, -92(fp)
	lw x6, -96(fp)
	beq x5, x6, .eq6
	addi x6, x0, 0
	sw x6, -52(fp)
	jal x0, .exit_cond6
.eq6:
	addi x6, x0, 1
	sw x6, -52(fp)
.exit_cond6:
	jal x0, .for.inner.end
.if.inner.end:
	addi x6, x0, 1
	sw x6, -100(fp)
	lw x5, -100(fp)
	lw x6, -56(fp)
	add x7, x5, x6
	sw x7, -56(fp)
	jal x0, .for.inner.cond
.for.inner.end:
	addi x6, x0, 1
	sw x6, -104(fp)
	lw x5, -56(fp)
	lw x6, -104(fp)
	add x7, x5, x6
	sw x7, -56(fp)
	addi x6, x0, 1
	sw x6, -108(fp)
	lw x5, -52(fp)
	lw x6, -108(fp)
	beq x5, x6, .if.outer.body
	jal x0, .if.outer.end
.if.outer.body:
	nop
.if.outer.end:
	addi x6, x0, 1
	sw x6, -112(fp)
	lw x5, -36(fp)
	lw x6, -112(fp)
	add x7, x5, x6
	sw x7, -36(fp)
	jal x0, .for.outer.cond
.for.outer.end:
	lw s2, 72(sp)
	lw s1, 76(sp)
	lw fp, 80(sp)
	lw x1, 84(sp)
	addi sp, sp, 88
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
	lw x5, -12(fp)
	lw x6, -16(fp)
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
