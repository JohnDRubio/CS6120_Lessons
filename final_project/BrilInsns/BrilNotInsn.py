from BrilInsns.BrilBooleanMathInsn import BrilBooleanMathInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilNotInsn(BrilBooleanMathInsn):

  def __init__(self,dest,src1):
      super(BrilNotInsn, self).__init__(dest,src1)

  def conv_riscvir(self):
      # xori dest, src1, 1
      pass