from RVIRInsns.RVIRInsn import RVIRInsn
import numbers

# ? Do we need this? doesn't look like we are using them in any of the convert functions
# A: Let's keep these because these instructions are the only way
#    for Bril programs to use numbers larger than 2^12 -1
#    We probably won't get around to using these though.
class RVIRSpecialRegImmInsn(RVIRInsn):
    valid_ops = ['LUI','AUIPC']
    def __init__(self, op, dst, imm):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        # if not isinstance(imm, numbers.Real):     # Not enforcing this b/c I'm not sure if imm can be a label
        #     raise ValueError(f"Invalid operand '{src1}'. Supported operands must be numeric.")
        super().__init__(abstract_dst=dst)
        self.op = op
        self.dst  = dst
        self.imm = imm
    
    def emit_asm(self):
        return f'{self.op} {self.dst}, {self.imm}'

    def get_abstract_registers(self):
        abstract_regs = []
        for reg in [self.abstract_dst]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        pass

    def writes(self):
        pass

    def convert_registers(self):
        self.dst = 'x5'

# r = RVIRSpecialRegImmInsn('lui','x1','x2','x3')   # raises error
# r = RVIRSpecialRegImmInsn('lui','x1',2)   
# r = RVIRSpecialRegImmInsn('auipc','x1',2)   
# r = RVIRSpecialRegImmInsn('john','x1',2)      # raises error
# print(r.emit_asm())