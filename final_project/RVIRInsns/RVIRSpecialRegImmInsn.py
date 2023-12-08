from RVIRInsns.RVIRInsn import RVIRInsn
import numbers

class RVIRSpecialRegImmInsn(RVIRInsn):
    valid_ops = ['LUI','AUIPC']
    def __init__(self, op, dst, src1, src2=None):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if src2 is not None:
            raise ValueError(f"Invalid operand '{src2}'. LUI / AUIPC take 2 operands.")
        if not isinstance(src1, numbers.Real):
            raise ValueError(f"Invalid operand '{src1}'. Supported operands must be numeric.")
        self.op = op
        self.dst  = dst
        self.src1 = src1
    
    def emit_asm(self):
        return f'{self.op} {self.dst}, {self.src1}'

    def get_abstract_temps(self):
        return [self.dst,self.src1]

# r = RVIRSpecialRegImmInsn('lui','x1','x2','x3')   # raises error
# r = RVIRSpecialRegImmInsn('lui','x1',2)   
# r = RVIRSpecialRegImmInsn('auipc','x1',2)   
# r = RVIRSpecialRegImmInsn('john','x1',2)      # raises error
# print(r.emit_asm())