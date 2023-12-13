from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRRegRegInsn(RVIRInsn):
    valid_ops = ['ADD','SUB','MUL','DIV','AND','OR','XOR','SLT','SLTU','SRA','SRL','SLL']
    def __init__(self, op, dst, src1, src2):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        super().__init__(abstact_src1=src1, abstract_src2=src2, abstract_dst=dst)
        self.op = op
        self.dst  = dst
        self.src1 = src1
        self.src2 = src2
    
    def emit_asm(self):
        return f'{self.op} {self.dst}, {self.src1}, {self.src2}'

    def get_abstract_registers(self):
        abstract_regs = []
        for reg in [self.abstract_src1,self.abstract_src2,self.abstract_dst]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        return [self.src1,self.src2]

    def writes(self):
        return [self.dst]

    # Visitor pattern
    def convert_registers(self, visitor):
        visitor.RVIRRegRegInsn_convert_registers(self)
    
    # For Calling Conventions
    def get_containers(self):
        return self.dst, self.src1, self.src2

    def cc_update(self, new_regs):
        self.dst, self.src1, self.src2 = new_regs
    
    def xregs(self):
        self.dst = self.dst if self.dst not in self.reg_map else self.reg_map[self.dst]
        self.src1 = self.src1 if self.src1 not in self.reg_map else self.reg_map[self.src1]
        self.src2 = self.src2 if self.src2 not in self.reg_map else self.reg_map[self.src2]

# r = RVIRRegRegInsn('add','x1','x2','x3')
# r = RVIRRegRegInsn('john','x1','x2','x3')   # raises error
# print(r.emit_asm())