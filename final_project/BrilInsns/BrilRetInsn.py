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

class BrilRetInsn(BrilEffectOperationInsn):

  # assume for now that value is an argument
  def __init__(self, value=None):
      self.value = value

  def conv_riscvir(self):
      '''
      if value:
          addi a0, val, 0;
          jalr x0, x1, 0;
      else:
          jalr x0, x1, 0;
      '''
      insns = []
      if self.value:
          insns.append(RVIRRegImmInsn('addi','a0',self.value, 0))
      
      insns.append(RVIRJumpInsn('jalr','x0', 'x1',0)) # TODO: check since this isn't what you put in RVIRJumpInsn

      return insns