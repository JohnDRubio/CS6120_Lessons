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
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn

class BrilLabelInsn(BrilInsn):

  def __init__(self,label, isFuncName=False):
      self.label = label+':'
      self.isFuncName = isFuncName

  def conv_riscvir(self):
      label = '.'+self.label if not self.isFuncName else self.label
      if self.label[-1] != ':':
         return [RVIRLabelInsn(label+':')]
      return [RVIRLabelInsn(label)]
      