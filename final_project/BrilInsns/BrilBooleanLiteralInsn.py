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

class BrilBooleanLiteralInsn(BrilConstInsn):

  def __init__(self,dest,value):
      super(BrilBooleanLiteralInsn, self).__init__(dest)
      self.value = value

  def conv_riscvir(self):
      # TODO: need look at this more ; can be an integer or a boolean - i think this covers it though
      if self.value:
        return [RVIRRegImmInsn('addi',self.dest,'x0', 1)]
      else:
        return [RVIRRegImmInsn('addi',self.dest,'x0', 0)]

      # if value == true
      #   addi dest, x0, 1
      # else
      #   addi dest, x0, 0
