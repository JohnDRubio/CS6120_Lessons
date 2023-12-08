from RVIRInsns.RVIRInsn import RVIRInsn
# import numbers

class RVIRBranchInsn(RVIRInsn):
    valid_ops = ['BEQ','BNE', 'BLT', 'BLTU', 'BGE', 'BGEU']
    def __init__(self, op, src1, src2, br_target):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        # if not isinstance(imm, numbers.Real):
        #         raise ValueError(f"Invalid operand '{imm}'. Supported operands must be numeric.")
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.br_target = br_target
    
    def emit_asm(self):
        return f'{self.op} {self.src1}, {self.src2}, {self.br_target}'

    def get_abstract_temps(self):
        return [self.src1,self.src2]

# r = RVIRBranchInsn('bne','x1','x2','.loop')      
# r = RVIRBranchInsn('john','x1','x2','.loop')  # raises error    
# print(r.emit_asm())