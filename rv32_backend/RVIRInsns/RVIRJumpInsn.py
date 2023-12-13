from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRJumpInsn(RVIRInsn):
    valid_ops = ['JAL', 'JALR']
    def __init__(self, op, src1, jmp_target, imm=None, isFunc=None):
        if op.upper() not in self.valid_ops:
            raise ValueError(f"Invalid operation '{op}'. Supported operations are: {', '.join(self.valid_ops)}")
        if op.upper() == self.valid_ops[0] and imm is not None:
             raise ValueError(f"Invalid JAL instruction: JAL takes 2 operands but 3 were provided.")
        if op.upper() == self.valid_ops[1] and imm is None:
             raise ValueError(f"Invalid JALR instruction: JALR takes 3 operands but 2 were provided.")
        super().__init__(abstract_dst=src1,abstact_src1=jmp_target,abstract_src2=imm)
        self.op = op
        self.src1 = src1
        self.imm = imm
        self.jmp_target = jmp_target
        self.isFunc = isFunc
    
    def emit_asm(self):
        '''
            JAL instructions have format: <op> <rd>, <target>
            where op can be: JAL
                  rd can be: any register but typically x0 or x1
                  target can be: an alias for an immediate or an immediate
            
            JALR instructions have format: <op> <rd>, <ret_address>, <offset>
            where op can be: JAL
                  rd can be: any register but typically x0
                  ret_address can be: x1
                  offset can be: an immediate
        '''
        if self.op.upper() == self.valid_ops[0]:
            return f'{self.op} {self.src1}, {self.jmp_target}'     
        return f'{self.op} {self.src1}, {self.jmp_target}, {self.imm} '

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
            return [self.jmp_target]  # JALR reads its second operand

    def writes(self):
        return [self.src1]

    # Visitor pattern
    def convert_registers(self, visitor):
        visitor.RVIRJumpInsn_convert_registers(self)
    
    def xregs(self, visitor):
        visitor.RVIRJumpInsn_xregs(self)
    
    # For Calling Conventions
    def get_containers(self):
        return self.src1, self.jmp_target

    def cc_update(self, new_regs):
        self.src1, self.jmp_target = new_regs
    

# r = RVIRJumpInsn('jal','x1','.loop')      
# r = RVIRJumpInsn('jal','x1', 'x2','.loop')  # raises error   
# r = RVIRJumpInsn('jalr','x0', imm='0',jmp_target='x1')    
# r = RVIRJumpInsn('jalr','x1','.loop')  # raises error  
# r = RVIRJumpInsn('john','x1','x2','.loop')  # raises error    
# print(r.emit_asm())