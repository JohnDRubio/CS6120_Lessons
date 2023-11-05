from BrilInsns.BrilEffectOperationInsn import BrilEffectOperationInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilBranchInsn(BrilEffectOperationInsn):

  def __init__(self, cond, label1, label2):
      self.cond = cond
      self.label1 = label1
      self.label2 = label2

  def conv_riscvir(self):
      '''
      addi x, x0, 1;
      beq cond, x, label1;
      jal x0, label2; 
      '''
      pass 