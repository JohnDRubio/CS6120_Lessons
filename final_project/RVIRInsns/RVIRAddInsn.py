from RVIRRegRegInsn import RVIRRegRegInsn

class RVIRAddInsn(RVIRRegRegInsn):
    def __init__(self, dst, src1, src2):
        super(RVIRAddInsn, self).__init__(dst, src1, src2)
    
    def emit_asm(self):
        return f'add {self.dst}, {self.src1}, {self.src2}'

# r = RVIRAddInsn('x1','x2','x3')
# print(r.emit_asm())