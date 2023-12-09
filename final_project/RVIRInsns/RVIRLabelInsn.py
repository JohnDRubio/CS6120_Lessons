from RVIRInsns.RVIRInsn import RVIRInsn

class RVIRLabelInsn(RVIRInsn):
    def __init__(self, label):
        self.label = label
    
    def emit_asm(self):
        return self.label

    def get_abstract_temps(self):
        return []

    def uses(self):
        return []

    def writes(self):
        return []

    def removeAbstractTemps(self):
        pass