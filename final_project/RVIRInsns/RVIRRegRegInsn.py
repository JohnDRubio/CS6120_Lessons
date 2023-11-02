from RVIRInsn import RVIRInsn

class RVIRRegRegInsn(RVIRInsn):
    def __init__(self, dst, src1, src2):
        self.dst  = dst
        self.src1 = src1
        self.src2 = src2
    
    def emit_asm(self):
        pass