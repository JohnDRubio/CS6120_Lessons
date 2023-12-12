from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRNopInsn(RVIRInsn):
    def __init__(self):
        pass
    
    def emit_asm(self):
        return "nop"

    def get_abstract_registers(self):
        return []

    def uses(self):
        return []

    def writes(self):
        return []

    def convert_registers(self):
        pass