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

class BrilFunctionCallInsn(BrilValueOperationInsn):

  def __init__(self, func, dest=None, args=None):
      super(BrilFunctionCallInsn, self).__init__(dest)
      self.func = func
      self.args = args

  def conv_riscvir(self):
      # TODO: will do this conversion after initial first pass
      '''
      if args != None:
        if args.size <= 8:
          start from a0 and push arguments all the way to a7 if necessary
        else:
          start from a0 and push arguments all the way to a7 if necessary
          push all arguments after

      jal x0, func
      if dest != None:
        addi dest, x0, a0
      '''
      return self