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

class BrilIdInsn(BrilValueOperationInsn):

  def __init__(self,dest,src):
      super(BrilIdInsn, self).__init__(dest)
      self.src = src

  def conv_riscvir(self):
      # addi dest, src, 0
      return [RVIRRegImmInsn('addi',self.dest,self.src, 0)]