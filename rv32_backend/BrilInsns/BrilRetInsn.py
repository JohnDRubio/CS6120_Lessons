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
  # Keep in mind that Bril has one optional return value
  def __init__(self, rv=None):
      self.rv = rv

  def conv_riscvir(self):
      '''
      if rv
          addi x10, val, 0;
          jalr x0, 0(x1);
      else:
          jalr x0, 0(x1);
      '''
      insns = []
      if self.rv:
          insns.append(RVIRRegImmInsn('addi','a0',self.rv, 0))      # Store return value
      insns.append(RVIRJumpInsn('jalr','x0', 'x1', 0)) # TODO: check since this isn't what you put in RVIRJumpInsn
      return insns