from RVIRInsns.RVIRInsn import RVIRInsn
import numbers

class RVIRMemInsn(RVIRInsn):
    valid_ops = ['LW','SW']
    def __init__(self, op, src1, src2, imm):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if not isinstance(imm, numbers.Real):
                raise ValueError(f"Invalid operand '{imm}'. Supported operands must be numeric.")
        super().__init__(abstact_src1=src2, abstract_dst=src1)
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.imm = imm
    
    def emit_asm(self):
        return f'{self.op} {self.src1}, {self.imm}({self.src2})'
    
    def get_abstract_registers(self):
        abstract_regs = []
        for reg in [self.abstract_src1, self.abstract_dst]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        if self.op.upper() == 'LW':
            return [self.src2]
        else:
            return [self.src1,self.src2]

    def writes(self):
        if self.op.upper() == 'LW':
            return [self.src1]
        else:
            return []

    # Visitor pattern
    def convert_registers(self, visitor):
        visitor.RVIRMemInsn_convert_registers(self)
    
    def xregs(self, visitor):
        visitor.RVIRMemInsn_xregs(self)

    # For Calling Conventions
    def get_containers(self):
        return self.src1, self.src2

    def cc_update(self, new_regs):
        self.src1, self.src2 = new_regs


# r = RVIRMemInsn('lw','x1','x2','x3')      # raises error
# r = RVIRMemInsn('lw','x1','x2',0)
# r = RVIRMemInsn('john','x1','x2',0)
# print(r.emit_asm())