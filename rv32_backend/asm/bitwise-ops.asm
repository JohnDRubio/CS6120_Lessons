mod2:
	addi sp, sp, -32
	sw x1, 28(sp)
	sw fp, 24(sp)
	addi fp, sp, 28
	sw s1, 20(sp)
	add x7, x0, a0
	sw x7, -8(fp)
	addi x6, x0, 2
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
	addi x6, x0, 1
	sw x6, -28(fp)
	lw x5, -28(fp)
	lw x6, -24(fp)
	beq x5, x6, .eq1
	addi x6, x0, 0
	sw x6, -32(fp)
	jal x0, .exit_cond1
.eq1:
	addi x6, x0, 1
	sw x6, -32(fp)
.exit_cond1:
	lw x5, -32(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s1, 20(sp)
	lw fp, 24(sp)
	lw x1, 28(sp)
	addi sp, sp, 32
	jalr x0, x1, 0 
loop_subroutine:
	addi sp, sp, -60
	sw x1, 56(sp)
	sw fp, 52(sp)
	addi fp, sp, 56
	sw s1, 48(sp)
	sw s2, 44(sp)
	sw s3, 40(sp)
	add x7, x0, a0
	sw x7, -12(fp)
	add x7, x0, a1
	sw x7, -16(fp)
	add x7, x0, a2
	sw x7, -20(fp)
	addi x6, x0, 0
	sw x6, -24(fp)
	addi x6, x0, 63
	sw x6, -28(fp)
	addi x6, x0, 1
	sw x6, -32(fp)
	addi x6, x0, 2
	sw x6, -36(fp)
	addi x6, x0, 0
	sw x6, -40(fp)
	addi x6, x0, 1
	sw x6, -44(fp)
.loop:
	lw x5, -28(fp)
	lw x6, -24(fp)
	bge x5, x6, .ge2
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond2
.ge2:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond2:
	addi x6, x0, 1
	sw x6, -52(fp)
	lw x5, -48(fp)
	lw x6, -52(fp)
	beq x5, x6, .here
	jal x0, .end
.here:
	lw x6, -12(fp)
	add a0, x0, x6
	jal x1, mod2
	add x7, a0, x0
	sw x7, -56(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	jal x1, mod2
	add x7, a0, x0
	sw x7, -60(fp)
	lw x5, -56(fp)
	lw x6, -60(fp)
	and x7, x5, x6
	sw x7, -64(fp)
	addi x6, x0, 1
	sw x6, -68(fp)
	lw x5, -20(fp)
	lw x6, -68(fp)
	beq x5, x6, .doOr
	jal x0, .stay
.doOr:
	lw x5, -56(fp)
	lw x6, -60(fp)
	or x7, x5, x6
	sw x7, -64(fp)
.stay:
	addi x6, x0, 1
	sw x6, -72(fp)
	lw x5, -64(fp)
	lw x6, -72(fp)
	beq x5, x6, .add
	jal x0, .end_loop
.add:
	lw x5, -40(fp)
	lw x6, -44(fp)
	add x7, x5, x6
	sw x7, -40(fp)
.end_loop:
	lw x5, -12(fp)
	lw x6, -36(fp)
	div x7, x5, x6
	sw x7, -12(fp)
	lw x5, -16(fp)
	lw x6, -36(fp)
	div x7, x5, x6
	sw x7, -16(fp)
	lw x5, -44(fp)
	lw x6, -36(fp)
	mul x7, x5, x6
	sw x7, -44(fp)
	lw x5, -24(fp)
	lw x6, -32(fp)
	add x7, x5, x6
	sw x7, -24(fp)
	jal x0, .loop
.end:
	lw x5, -40(fp)
	addi a0, x5, 0
	jalr x0, x1, 0 
	lw s3, 40(sp)
	lw s2, 44(sp)
	lw s1, 48(sp)
	lw fp, 52(sp)
	lw x1, 56(sp)
	addi sp, sp, 60
	jalr x0, x1, 0 
OR:
	addi sp, sp, -28
	sw x1, 24(sp)
	sw fp, 20(sp)
	addi fp, sp, 24
	sw s1, 16(sp)
	sw s2, 12(sp)
	add x7, x0, a0
	sw x7, -20(fp)
	add x7, x0, a1
	sw x7, -24(fp)
	addi x6, x0, 1
	sw x6, -28(fp)
	lw x6, -20(fp)
	add a0, x0, x6
	lw x6, -24(fp)
	add a1, x0, x6
	lw x6, -28(fp)
	add a2, x0, x6
	jal x1, loop_subroutine
	add x7, a0, x0
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
AND:
	addi sp, sp, -28
	sw x1, 24(sp)
	sw fp, 20(sp)
	addi fp, sp, 24
	sw s1, 16(sp)
	sw s2, 12(sp)
	add x7, x0, a0
	sw x7, -20(fp)
	add x7, x0, a1
	sw x7, -24(fp)
	addi x6, x0, 0
	sw x6, -28(fp)
	lw x6, -20(fp)
	add a0, x0, x6
	lw x6, -24(fp)
	add a1, x0, x6
	lw x6, -28(fp)
	add a2, x0, x6
	jal x1, loop_subroutine
	add x7, a0, x0
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
XOR:
	addi sp, sp, -28
	sw x1, 24(sp)
	sw fp, 20(sp)
	addi fp, sp, 24
	sw s1, 16(sp)
	sw s2, 12(sp)
	add x7, x0, a0
	sw x7, -16(fp)
	add x7, x0, a1
	sw x7, -20(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, AND
	add x7, a0, x0
	sw x7, -24(fp)
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, OR
	add x7, a0, x0
	sw x7, -28(fp)
	lw x5, -28(fp)
	lw x6, -24(fp)
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
main:
	addi sp, sp, -44
	sw x1, 40(sp)
	sw fp, 36(sp)
	addi fp, sp, 40
	sw s1, 32(sp)
	sw s2, 28(sp)
	sw s3, 24(sp)
	add x7, x0, a0
	sw x7, -16(fp)
	add x7, x0, a1
	sw x7, -20(fp)
	add x7, x0, a2
	sw x7, -24(fp)
	addi x6, x0, 1
	sw x6, -28(fp)
	addi x6, x0, 0
	sw x6, -32(fp)
	lw x5, -24(fp)
	lw x6, -28(fp)
	sub x7, x5, x6
	sw x7, -36(fp)
	lw x5, -32(fp)
	addi x6, x5, 0
	sw x6, -40(fp)
	lw x5, -36(fp)
	lw x6, -32(fp)
	blt x5, x6, .lt3
	addi x6, x0, 0
	sw x6, -44(fp)
	jal x0, .exit_cond3
.lt3:
	addi x6, x0, 1
	sw x6, -44(fp)
.exit_cond3:
	lw x5, -36(fp)
	lw x6, -32(fp)
	beq x5, x6, .eq4
	addi x6, x0, 0
	sw x6, -48(fp)
	jal x0, .exit_cond4
.eq4:
	addi x6, x0, 1
	sw x6, -48(fp)
.exit_cond4:
	lw x5, -32(fp)
	lw x6, -36(fp)
	blt x5, x6, .lt5
	addi x6, x0, 0
	sw x6, -52(fp)
	jal x0, .exit_cond5
.lt5:
	addi x6, x0, 1
	sw x6, -52(fp)
.exit_cond5:
	addi x6, x0, 1
	sw x6, -56(fp)
	lw x5, -44(fp)
	lw x6, -56(fp)
	beq x5, x6, .and_op
	jal x0, .useless_lbl
.useless_lbl:
	addi x6, x0, 1
	sw x6, -60(fp)
	lw x5, -48(fp)
	lw x6, -60(fp)
	beq x5, x6, .or_op
	jal x0, .xor_op
.and_op:
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, AND
	add x7, a0, x0
	sw x7, -40(fp)
	jal x0, .end
.or_op:
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, OR
	add x7, a0, x0
	sw x7, -40(fp)
	jal x0, .end
.xor_op:
	lw x6, -16(fp)
	add a0, x0, x6
	lw x6, -20(fp)
	add a1, x0, x6
	jal x1, XOR
	add x7, a0, x0
	sw x7, -40(fp)
.end:
	add x0, x0, x0
	lw s3, 24(sp)
	lw s2, 28(sp)
	lw s1, 32(sp)
	lw fp, 36(sp)
	lw x1, 40(sp)
	addi sp, sp, 44
	jalr x0, x1, 0 
