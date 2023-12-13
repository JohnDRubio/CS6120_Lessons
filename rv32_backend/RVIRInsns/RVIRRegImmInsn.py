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
        super().__init__(abstact_src1=src1, abstract_dst=dst)
        self.op = op
        self.dst  = dst
        self.src1 = src1
        self.src2 = src2
    
    def emit_asm(self):
        return f'{self.op} {self.dst}, {self.src1}, {self.src2}'

    def get_abstract_registers(self): 
        abstract_regs = []
        for reg in [self.abstract_src1,self.abstract_dst]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        return [self.src1]

    def writes(self):
        return [self.dst]

    # Visitor pattern
    def convert_registers(self, visitor):
        visitor.RVIRRegImmInsn_convert_registers(self)
    
    def xregs(self, visitor):
        visitor.RVIRRegImmInsn_xregs(self)
    
    # For Calling Conventions
    def get_containers(self):
        return self.dst, self.src1

    def cc_update(self, new_regs):
        self.dst, self.src1 = new_regs


# r = RVIRRegImmInsn('addi','x1','x2','x3')   # raises error
# r = RVIRRegImmInsn('addi','x1','x2',2)   
# r = RVIRRegImmInsn('john','x1','x2',2)   # raises error
# print(r.emit_asm())