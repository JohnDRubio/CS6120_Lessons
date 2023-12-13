from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRNopInsn(RVIRInsn):
    def __init__(self):
        pass
    
    def emit_asm(self):
        return "add x0, x0, x0"

    def get_abstract_registers(self):
        return []

    def uses(self):
        return []

    def writes(self):
        return []