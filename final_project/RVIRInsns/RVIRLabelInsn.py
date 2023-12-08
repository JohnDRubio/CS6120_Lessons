from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRLabelInsn(RVIRInsn):
    def __init__(self, label):
        self.label = label
    
    def emit_asm(self):
        return self.label