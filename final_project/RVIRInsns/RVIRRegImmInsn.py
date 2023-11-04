from RVIRInsns.RVIRInsn import RVIRInsn
import numbers

class RVIRRegImmInsn(RVIRInsn):
    valid_ops = ['ADDI','SUBI','ANDI','ORI','XORI','SLTI','SLTIU','SRAI','SRLI','SLLI']
    def __init__(self, op, dst, src1, src2=None):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if src2 is not None:
            if not isinstance(src2, numbers.Real):
                raise ValueError(f"Invalid operand '{src2}'. Supported operands must be numeric.")
        self.op = op
        self.dst  = dst
        self.src1 = src1
        self.src2 = src2
    
    def emit_asm(self):
        return f'{self.op} {self.dst}, {self.src1}, {self.src2}'

# r = RVIRRegImmInsn('addi','x1','x2','x3')   # raises error
# r = RVIRRegImmInsn('addi','x1','x2',2)   
# r = RVIRRegImmInsn('john','x1','x2',2)   # raises error
# print(r.emit_asm())