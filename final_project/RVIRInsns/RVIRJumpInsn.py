from RVIRInsns.RVIRInsn import RVIRInsn
# import numbers

class RVIRJumpInsn(RVIRInsn):
    valid_ops = ['JAL', 'JALR']
    def __init__(self, op, src1, jmp_target, src2=None):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if op.upper() == self.valid_ops[0] and src2 is not None:
             raise ValueError(f"Invalid JAL instruction: JAL takes 2 operands but 3 were provided.")
        if op.upper() == self.valid_ops[1] and src2 is None:
             raise ValueError(f"Invalid JALR instruction: JALR takes 3 operands but 2 were provided.")
        # if not isinstance(jmp_target, numbers.Real):
        #         raise ValueError(f"Invalid operand '{jmp_target}'. Supported operands must be numeric.")
        self.op = op
        self.src1 = src1
        self.src2 = src2
        self.jmp_target = jmp_target
    
    def emit_asm(self):
        if self.op.upper() == self.valid_ops[0]:
            return f'{self.op} {self.src1}, {self.jmp_target}'     
        return f'{self.op} {self.src1}, {self.src2}, {self.jmp_target}'

    def get_abstract_temps(self):
        abstract_temps = [self.src1]
        if self.src2 != None:
            abstract_temps.append(self.src2)

        return abstract_temps

    # TODO: come back to this, idk if it is right

    def uses(self):
        if self.op.upper() == 'JAL':
            return [self.src1]
        else:
            return [self.src2]

    def writes(self):
        if self.op.upper() == 'JAL':
            return []
        else:
            return [self.src1]

    def removeAbstractTemps(self):
        # TODO
        pass

# r = RVIRJumpInsn('jal','x1','.loop')      
# r = RVIRJumpInsn('jal','x1', 'x2','.loop')  # raises error   
# r = RVIRJumpInsn('jalr','x1', src2='x2',jmp_target='.loop')    
# r = RVIRJumpInsn('jalr','x1','.loop')  # raises error  
# r = RVIRJumpInsn('john','x1','x2','.loop')  # raises error    
# print(r.emit_asm())