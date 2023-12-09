class RVIRInsn:
    '''
        RVIRInsn insances represent RISC-V instructions that have
        not yet been lowered to true RISC-V assembly code. The syntax
        and semantics of each RVIR instruction is identical to RISC-V
        instructions. The only difference is that RVIR instructions
        use arbitrary, abstract registers.
    '''
    isa_regs = ['x0','x1']
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

    def convert_registers(self):
        '''
            Convert all abstract registers to the machine registers
            they've been mapped to.
        '''
        pass