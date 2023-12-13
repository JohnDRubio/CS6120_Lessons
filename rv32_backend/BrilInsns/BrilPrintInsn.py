from BrilInsns.BrilInsn import BrilInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn
from RVIRInsns.RVIRNopInsn import RVIRNopInsn

class BrilPrintInsn(BrilInsn):

  def __init__(self,args):
      self.args = args

  def conv_riscvir(self):
      return [RVIRNopInsn()]