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

class BrilLabelInsn(BrilInsn):

  def __init__(self,label):
      self.label = label

  def conv_riscvir(self):
      # .label
      # TODO: can probably stay the same - but it would not a RISCV type
      # maybe have a generic label instruction class that isn't bril or riscv
      pass 