class RVIRInsn:
    def __init__(self):
        pass

    # For an arbitrary RVirInsn instance, 
    # return the RISC-V IR instruction as a string
    def emit_asm(self):
        pass

    # For an arbitrary RISCVInsn, get all abstract temps
    def get_abstract_temps(self):
        pass


    # For each insn, return temps is uses and writes
    # for uses, we need to add insns before for trivial RA
    # for writes, we need to add insns after for trivial RA

    def uses(self):
        pass

    def writes(self):
        pass