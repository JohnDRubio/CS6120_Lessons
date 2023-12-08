from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRNopInsn(RVIRInsn):
    def __init__(self):
        pass
    
    def emit_asm(self):
        return "nop"