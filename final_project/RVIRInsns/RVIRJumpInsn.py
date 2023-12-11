from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRJumpInsn(RVIRInsn):
    valid_ops = ['JAL', 'JALR']
    def __init__(self, op, src1, jmp_target, src2=None):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if op.upper() == self.valid_ops[0] and src2 is not None:
             raise ValueError(f"Invalid JAL instruction: JAL takes 2 operands but 3 were provided.")
        if op.upper() == self.valid_ops[1] and src2 is None:
             raise ValueError(f"Invalid JALR instruction: JALR takes 3 operands but 2 were provided.")
        super().__init__(src1,src2)
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.jmp_target = jmp_target
    
    def emit_asm(self):
        if self.op.upper() == self.valid_ops[0]:
            return f'{self.op} {self.src1}, {self.jmp_target}'     
        return f'{self.op} {self.src1}, {self.src2}, {self.jmp_target}'

    def get_abstract_registers(self):
        abstract_regs = []
        for reg in [self.abstract_src1]:
            if reg not in self.isa_regs:
                abstract_regs.append(reg)
        return abstract_regs

    def uses(self):
        if self.op.upper() == 'JAL':
            return []   # JAL does not read any registers
        else:
            return [self.src2]  # JALR reads its second operand

    def writes(self):
        return [self.src1]

    def convert_registers(self):
        if self.op.upper() == 'JALR':
            self.src2 = 'x5'
        self.src1 = 'x0'        #TODO: Special case - After instruction must be x1. I think this is okay in TrivialRegisterAllocator class since insnsAfter is called after convert_registers()

# r = RVIRJumpInsn('jal','x1','.loop')      
# r = RVIRJumpInsn('jal','x1', 'x2','.loop')  # raises error   
# r = RVIRJumpInsn('jalr','x1', src2='x2',jmp_target='.loop')    
# r = RVIRJumpInsn('jalr','x1','.loop')  # raises error  
# r = RVIRJumpInsn('john','x1','x2','.loop')  # raises error    
# print(r.emit_asm())