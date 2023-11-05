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
      # if value == true
      #   addi dest, x0, 1
      # else
      #   addi dest, x0, 0
      pass 