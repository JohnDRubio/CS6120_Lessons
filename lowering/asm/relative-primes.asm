main:
	addi sp, sp, -28
	sw x1, 24(sp)
	sw fp, 20(sp)
	addi fp, sp, 24
	addi x6, x0, 20
	sw x6, -12(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	lw x6, -20(fp)
	add a0, x0, x6
	jal x1, relative_primes
	addi x6, x0, 0
	sw x6, -24(fp)
	lw fp, 20(sp)
	lw x1, 24(sp)
	addi sp, sp, 28
	jalr x0, x1, 0 
mod:
	addi sp, sp, -28
	sw x1, 24(sp)
	sw fp, 20(sp)
	addi fp, sp, 24
	sw s1, 16(sp)
	sw s2, 12(sp)
	addi x6, a0, 0
	sw x6, -8(fp)
	addi x6, a1, 0
	sw x6, -12(fp)
	lw x5, -8(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
	lw x5, -12(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	lw x5, -16(fp)
	lw x6, -20(fp)
	div x7, x5, x6
	sw x7, -24(fp)
	lw x5, -24(fp)
	lw x6, -20(fp)
	mul x7, x5, x6
	sw x7, -28(fp)
	lw x5, -16(fp)
	lw x6, -28(fp)
	sub x7, x5, x6
	sw x7, -32(fp)
	lw x5, -32(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s2, 12(sp)
	lw s1, 16(sp)
	lw fp, 20(sp)
	lw x1, 24(sp)
	addi sp, sp, 28
	jalr x0, x1, 0 
gcd:
	addi sp, sp, -112
	sw x1, 108(sp)
	sw fp, 104(sp)
	addi fp, sp, 108
	sw s1, 100(sp)
	sw s2, 96(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	addi x6, a1, 0
	sw x6, -20(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -28(fp)
	lw x5, -28(fp)
	lw x6, -24(fp)
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
	beq x5, x6, .then.0
	jal x0, .else.0
.then.0:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -40(fp)
	lw x5, -40(fp)
	addi x6, x5, 0
	sw x6, -44(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -48(fp)
	lw x5, -48(fp)
	addi x6, x5, 0
	sw x6, -16(fp)
	lw x5, -44(fp)
	addi x6, x5, 0
	sw x6, -52(fp)
	lw x5, -52(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	jal x0, .endif.0
.else.0:
.endif.0:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -56(fp)
	addi x6, x0, 0
	sw x6, -60(fp)
	lw x5, -56(fp)
	lw x6, -60(fp)
	beq x5, x6, .eq2
	addi x6, x0, 0
	sw x6, -64(fp)
	jal x0, .exit_cond2
.eq2:
	addi x6, x0, 1
	sw x6, -64(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -68(fp)
	lw x5, -64(fp)
	lw x6, -68(fp)
	beq x5, x6, .then.7
	jal x0, .else.7
.then.7:
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -72(fp)
	lw x5, -72(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.label_0:
	jal x0, .endif.7
.else.7:
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -76(fp)
	addi x6, x0, 0
	sw x6, -80(fp)
	lw x5, -76(fp)
	lw x6, -80(fp)
	beq x5, x6, .eq3
	addi x6, x0, 0
	sw x6, -84(fp)
	jal x0, .exit_cond3
.eq3:
	addi x6, x0, 1
	sw x6, -84(fp)
.exit_cond3:
	addi x6, x0, 1
	sw x6, -88(fp)
	lw x5, -84(fp)
	lw x6, -88(fp)
	beq x5, x6, .then.12
	jal x0, .else.12
.then.12:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -92(fp)
	lw x5, -92(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
.label_1:
	jal x0, .endif.12
.else.12:
.endif.12:
.endif.7:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -96(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -100(fp)
	lw x6, -96(fp)
	add a0, x0, x6
	lw x6, -100(fp)
	add a1, x0, x6
	jal x1, mod
	add x7, a0, x0
	sw x7, -104(fp)
	lw x5, -104(fp)
	addi x6, x5, 0
	sw x6, -104(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -108(fp)
	lw x5, -104(fp)
	addi x6, x5, 0
	sw x6, -112(fp)
	lw x6, -108(fp)
	add a0, x0, x6
	lw x6, -112(fp)
	add a1, x0, x6
	jal x1, gcd
	add x7, a0, x0
	sw x7, -116(fp)
	lw x5, -116(fp)
	addi x6, x5, 0
	sw x6, -116(fp)
	lw x5, -116(fp)
	addi x6, x5, 0
	sw x6, -120(fp)
	lw x5, -120(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s2, 96(sp)
	lw s1, 100(sp)
	lw fp, 104(sp)
	lw x1, 108(sp)
	addi sp, sp, 112
	jalr x0, x1, 0 
relative_primes:
	addi sp, sp, -80
	sw x1, 76(sp)
	sw fp, 72(sp)
	addi fp, sp, 76
	sw s1, 68(sp)
	addi x6, a0, 0
	sw x6, -16(fp)
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -20(fp)
	lw x5, -20(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
.for.cond.0:
	lw x5, -24(fp)
	addi x6, x5, 0
	sw x6, -28(fp)
	addi x6, x0, 1
	sw x6, -32(fp)
	lw x5, -28(fp)
	lw x6, -32(fp)
	bge x5, x6, .ge4
	addi x6, x0, 0
	sw x6, -36(fp)
	jal x0, .exit_cond4
.ge4:
	addi x6, x0, 1
	sw x6, -36(fp)
.exit_cond4:
	addi x6, x0, 1
	sw x6, -40(fp)
	lw x5, -36(fp)
	lw x6, -40(fp)
	beq x5, x6, .for.body.0
	jal x0, .for.end.0
.for.body.0:
	lw x5, -16(fp)
	addi x6, x5, 0
	sw x6, -44(fp)
	lw x5, -24(fp)
	addi x6, x5, 0
	sw x6, -48(fp)
	lw x6, -44(fp)
	add a0, x0, x6
	lw x6, -48(fp)
	add a1, x0, x6
	jal x1, gcd
	add x7, a0, x0
	sw x7, -52(fp)
	lw x5, -52(fp)
	addi x6, x5, 0
	sw x6, -52(fp)
	lw x5, -52(fp)
	addi x6, x5, 0
	sw x6, -56(fp)
	addi x6, x0, 1
	sw x6, -60(fp)
	lw x5, -56(fp)
	lw x6, -60(fp)
	beq x5, x6, .eq5
	addi x6, x0, 0
	sw x6, -64(fp)
	jal x0, .exit_cond5
.eq5:
	addi x6, x0, 1
	sw x6, -64(fp)
.exit_cond5:
	addi x6, x0, 1
	sw x6, -68(fp)
	lw x5, -64(fp)
	lw x6, -68(fp)
	beq x5, x6, .then.7
	jal x0, .else.7
.then.7:
	lw x5, -24(fp)
	addi x6, x5, 0
	sw x6, -72(fp)
	nop
	addi x6, x0, 0
	sw x6, -76(fp)
	jal x0, .endif.7
.else.7:
.endif.7:
	lw x5, -24(fp)
	addi x6, x5, 0
	sw x6, -80(fp)
	addi x6, x0, 1
	sw x6, -84(fp)
	lw x5, -80(fp)
	lw x6, -84(fp)
	sub x7, x5, x6
	sw x7, -88(fp)
	lw x5, -88(fp)
	addi x6, x5, 0
	sw x6, -24(fp)
	jal x0, .for.cond.0
.for.end.0:
	lw s1, 68(sp)
	lw fp, 72(sp)
	lw x1, 76(sp)
	addi sp, sp, 80
	jalr x0, x1, 0 
