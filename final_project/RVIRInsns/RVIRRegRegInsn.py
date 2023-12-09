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
        return [self.abstract_src1,self.abstract_src2,self.abstract_dst]

    def uses(self):
        return [self.src1,self.src2]

    def writes(self):
        return [self.dst]

    def convert_registers(self):
        self.src1 = 'x5'
        self.src2 = 'x6'
        self.dst = 'x7'

# r = RVIRRegRegInsn('add','x1','x2','x3')
# r = RVIRRegRegInsn('john','x1','x2','x3')   # raises error
# print(r.emit_asm())