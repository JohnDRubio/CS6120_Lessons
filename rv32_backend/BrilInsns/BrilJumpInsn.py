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

class BrilJumpInsn(BrilEffectOperationInsn):

  def __init__(self,target):
      self.target = target

  def conv_riscvir(self):
      # jal x0, .label
      return [RVIRJumpInsn('jal','x0','.'+self.target)]  