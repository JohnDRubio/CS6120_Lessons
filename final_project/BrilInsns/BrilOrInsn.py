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

class BrilOrInsn(BrilBooleanMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilOrInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # or dest, src1, src2
      return [RVIRRegRegInsn("or",self.dest,self.src1,self.src2)]