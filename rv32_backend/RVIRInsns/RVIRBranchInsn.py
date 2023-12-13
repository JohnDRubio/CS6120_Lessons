from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRBranchInsn(RVIRInsn):
    valid_ops = ['BEQ','BNE', 'BLT', 'BLTU', 'BGE', 'BGEU']
    def __init__(self, op, src1, src2, br_target):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        super().__init__(src1,src2)
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.br_target = br_target
    
    def emit_asm(self):
        return f'{self.op} {self.src1}, {self.src2}, {self.br_target}'

    def get_abstract_registers(self):
        abstract_regs = []
        for reg in [self.abstract_src1, self.abstract_src2]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        return [self.src1,self.src2]

    def writes(self):
        return []

    # Visitor pattern
    def convert_registers(self, visitor):
        visitor.RVIRBranchInsn_convert_registers(self)
    
    # For Calling Conventions
    def get_containers(self):
        return self.src1, self.src2

    def cc_update(self, new_regs):
        self.src1, self.src2 = new_regs
    
    def xregs(self):
        self.src1 = self.src1 if self.src1 not in self.reg_map else self.reg_map[self.src1]
        self.src2 = self.src2 if self.src2 not in self.reg_map else self.reg_map[self.src2]


# r = RVIRBranchInsn('bne','x1','x2','.loop')      
# r = RVIRBranchInsn('john','x1','x2','.loop')  # raises error    
# print(r.emit_asm())