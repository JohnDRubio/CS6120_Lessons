from BrilInsns.BrilConstInsn import BrilConstInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilIntegerLiteralInsn(BrilConstInsn):

  def __init__(self,dest,value):
      super(BrilIntegerLiteralInsn, self).__init__(dest)
      self.value = value

  def conv_riscvir(self):
      # addi dest, x0, value
      return [RVIRRegImmInsn('addi',self.dest,'x0', self.value)]