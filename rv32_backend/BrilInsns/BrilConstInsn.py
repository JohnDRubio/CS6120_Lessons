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

# maybe don't need IntegerLiteral and BooleanLiteral classes
class BrilConstInsn(BrilInsn):

  def __init__(self, type, dest, value):
      self.type = type
      self.dest = dest
      self.value = value

  def conv_riscvir(self):
      if self.type.lower() != "bool":
        # addi dest, x0, value
        return [RVIRRegImmInsn('addi',self.dest,'x0', self.value)]
      # if value == true
      #   addi dest, x0, 1
      # else
      #   addi dest, x0, 0
      if self.value:
        return [RVIRRegImmInsn('addi',self.dest,'x0', 1)]
      else:
        return [RVIRRegImmInsn('addi',self.dest,'x0', 0)] 