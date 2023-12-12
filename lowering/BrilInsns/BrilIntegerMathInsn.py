from BrilInsns.BrilValueOperationInsn import BrilValueOperationInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilIntegerMathInsn(BrilValueOperationInsn):

  def __init__(self,dest,src1,src2):
      super(BrilIntegerMathInsn, self).__init__(dest)
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      pass 