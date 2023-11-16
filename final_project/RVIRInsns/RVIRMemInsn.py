from RVIRInsns.RVIRInsn import RVIRInsn
import numbers

class RVIRMemInsn(RVIRInsn):
    valid_ops = ['LW','SW']
    def __init__(self, op, src1, src2, imm):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if not isinstance(imm, numbers.Real):
                raise ValueError(f"Invalid operand '{imm}'. Supported operands must be numeric.")
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.imm = imm
    
    def emit_asm(self):
        return f'{self.op} {self.src1}, {self.imm}({self.src2})'

# r = RVIRMemInsn('lw','x1','x2','x3')      # raises error
# r = RVIRMemInsn('lw','x1','x2',0)
# r = RVIRMemInsn('john','x1','x2',0)
# print(r.emit_asm())