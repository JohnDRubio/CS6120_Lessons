class RVIRInsn:
    '''
        RVIRInsn insances represent abstract RISC-V assembly code. 
        Several passes are performed on a list of RVIRInsn instances
        to eventually lower to RISC-V machine code.
        The syntax and semantics of each RVIR instruction is identical to RISC-V
        instructions. The only difference is that RVIR instructions
        use arbitrary, abstract registers.
    '''
    isa_regs = [
                'x0','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12',
                'x13','x14','x15','x16','x17','x18','x19','x20','x21','x22','x23',
                'x24','x25','x26','x27','x28','x29','x30','x31','sp','s0','s1','s2',
                's3','s4','s5','s6','s7','s8','s9','s10','s11','fp','a0','a1','a2',
                'a3','a4','a5','a6','a7'
                ]
    
    tra_regs = ['x5','x6','x7']
    
    reg_map = {
        'zero': 'x0',
        'ra'  : 'x1',
        'sp'  : 'x2',
        'gp'  : 'x3',
        'tp'  : 'x4',
        't0'  : 'x5',
        't1'  : 'x6',
        't2'  : 'x7',
        'fp'  : 'x8',
        's0'  : 'x8',    # ISA states x8 can be either fp or s0
        's1'  : 'x9',
        'a0'  : 'x10',
        'a1'  : 'x11',
        'a2'  : 'x12',
        'a3'  : 'x13',
        'a4'  : 'x14',
        'a5'  : 'x15',
        'a6'  : 'x16',
        'a7'  : 'x17',
        's2'  : 'x18',
        's3'  : 'x19',
        's4'  : 'x20',
        's5'  : 'x21',
        's6'  : 'x22',
        's7'  : 'x23',
        's8'  : 'x24',
        's9'  : 'x25',
        's10' : 'x26',
        's11' : 'x27',
        't3'  : 'x28',
        't4'  : 'x29',
        't5'  : 'x30',
        't6'  : 'x31',
    }
    
    def __init__(self, abstact_src1=None, abstract_src2=None,abstract_dst=None):
        self.abstract_src1= abstact_src1
        self.abstract_src2= abstract_src2
        self.abstract_dst= abstract_dst

    def emit_asm(self):
        '''
            Return this RVIRInsn as a string.
        '''
        pass
    
    # ? - Feels a little weird transforming RVIRInsns to pure 
    # ?   RISC-V instructions but maybe that's the best way?
    def get_abstract_registers(self):
        '''
            For an arbitrary RVIRInsn that has been
            lowered to a pure, RISC-V machine code instruction,
            return the abstract registers used by its RVIR equivalent.
        '''
        pass

    def uses(self):
        '''
            Returns a list (possibly empty) of registers that this 
            RVIR instruction uses.

            The registers returned by this method will end up being
            the registers written to prior to the "working instruction"
            in trivial register allocation.
        '''
        pass

    def writes(self):
        '''
            Returns the register that this RVIR instruction writes.
            Not all RVIR instructions write to registers.

            The register returned by this method will end up being
            the register written to after the "working instruction"
            in trivial register allocation.
        '''
        pass

    def convert_registers(self, visitor):
        '''
            Convert all abstract registers to the machine registers
            they've been mapped to.
        '''
        pass
    
    def xregs(self, visitor):
        pass

    def get_containers(self):
        return []
    
    def cc_update(self, lis):
        pass
