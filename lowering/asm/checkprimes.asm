main:
	addi sp, sp, -72
	sw x1, 68(sp)
	sw fp, 64(sp)
	addi fp, sp, 68
	sw s1, 60(sp)
	addi x6, a0, 0
	sw x6, -12(fp)
	addi x6, x0, 1
	sw x6, -16(fp)
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
.for.cond.1:
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -28(fp)
	lw x5, -24(fp)
	lw x6, -28(fp)
	blt x5, x6, .lt1
	addi x6, x0, 0
	sw x6, -32(fp)
	jal x0, .exit_cond1
.lt1:
	addi x6, x0, 1
	sw x6, -32(fp)
.exit_cond1:
	addi x6, x0, 1
	sw x6, -36(fp)
	lw x5, -32(fp)
	lw x6, -36(fp)
	beq x5, x6, .for.body.1
	jal x0, .for.end.1
.for.body.1:
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -40(fp)
	lw x6, -40(fp)
	add a0, x0, x6
	jal x1, checkPrime
	add x7, a0, x0
	sw x7, -44(fp)
	lw x5, -44(fp)
	addi x6, x5, 0
	sw x6, -44(fp)
	lw x5, -44(fp)
	addi x6, x5, 0
	sw x6, -48(fp)
	addi x6, x0, 1
	sw x6, -52(fp)
	lw x5, -48(fp)
	lw x6, -52(fp)
	beq x5, x6, .then.7
	jal x0, .else.7
.then.7:
	addi x6, x0, 1
	sw x6, -56(fp)
	nop
	addi x6, x0, 0
	sw x6, -60(fp)
	jal x0, .endif.7
.else.7:
	addi x6, x0, 0
	sw x6, -64(fp)
	nop
	addi x6, x0, 0
	sw x6, -68(fp)
.endif.7:
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -72(fp)
	addi x6, x0, 1
	sw x6, -76(fp)
	lw x5, -72(fp)
	lw x6, -76(fp)
	add x7, x5, x6
	sw x7, -80(fp)
	lw x5, -80(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	jal x0, .for.cond.1
.for.end.1:
	lw s1, 60(sp)
	lw fp, 64(sp)
	lw x1, 68(sp)
	addi sp, sp, 72
	jalr x0, x1, 0 
checkPrime:
	addi sp, sp, -108
	sw x1, 104(sp)
	sw fp, 100(sp)
	addi fp, sp, 104
	sw s1, 96(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -12(fp)
	addi x6, x0, 1
	sw x6, -16(fp)
	lw x5, -16(fp)
	lw x6, -12(fp)
	bge x5, x6, .ge2
	addi x6, x0, 0
	sw x6, -20(fp)
	jal x0, .exit_cond2
.ge2:
	addi x6, x0, 1
	sw x6, -20(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -24(fp)
	lw x5, -20(fp)
	lw x6, -24(fp)
	beq x5, x6, .then.0
	jal x0, .else.0
.then.0:
	addi x6, x0, 0
	sw x6, -28(fp)
	lw x5, -28(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.else.0:
.endif.0:
	addi x6, x0, 2
	sw x6, -32(fp)
	lw x5, -32(fp)
	addi x6, x5, 0
	sw x6, -36(fp)
.for.cond.5:
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -40(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -44(fp)
	lw x5, -40(fp)
	lw x6, -44(fp)
	blt x5, x6, .lt3
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond3
.lt3:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond3:
	addi x6, x0, 1
	sw x6, -52(fp)
	lw x5, -48(fp)
	lw x6, -52(fp)
	beq x5, x6, .for.body.5
	jal x0, .for.end.5
.for.body.5:
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -56(fp)
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -60(fp)
	lw x5, -56(fp)
	lw x6, -60(fp)
	div x7, x5, x6
	sw x7, -64(fp)
	lw x5, -64(fp)
	addi x6, x5, 0
	sw x6, -68(fp)
	lw x5, -68(fp)
	addi x6, x5, 0
	sw x6, -72(fp)
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -76(fp)
	lw x5, -72(fp)
	lw x6, -76(fp)
	mul x7, x5, x6
	sw x7, -80(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -84(fp)
	lw x5, -80(fp)
	lw x6, -84(fp)
	beq x5, x6, .eq4
	addi x6, x0, 0
	sw x6, -88(fp)
	jal x0, .exit_cond4
.eq4:
	addi x6, x0, 1
	sw x6, -88(fp)
.exit_cond4:
	lw x5, -88(fp)
	addi x6, x5, 0
	sw x6, -92(fp)
	lw x5, -92(fp)
	addi x6, x5, 0
	sw x6, -96(fp)
	addi x6, x0, 1
	sw x6, -100(fp)
	lw x5, -96(fp)
	lw x6, -100(fp)
	beq x5, x6, .then.18
	jal x0, .else.18
.then.18:
	addi x6, x0, 0
	sw x6, -104(fp)
	lw x5, -104(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.else.18:
.endif.18:
	lw x5, -36(fp)
	addi x6, x5, 0
	sw x6, -108(fp)
	addi x6, x0, 1
	sw x6, -112(fp)
	lw x5, -108(fp)
	lw x6, -112(fp)
	add x7, x5, x6
	sw x7, -116(fp)
	lw x5, -116(fp)
	addi x6, x5, 0
	sw x6, -36(fp)
	jal x0, .for.cond.5
.for.end.5:
	addi x6, x0, 1
	sw x6, -120(fp)
	lw x5, -120(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s1, 96(sp)
	lw fp, 100(sp)
	lw x1, 104(sp)
	addi sp, sp, 108
	jalr x0, x1, 0 
