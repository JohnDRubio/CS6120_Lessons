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

class BrilBooleanMathInsn(BrilValueOperationInsn):

  def __init__(self,op,dest,src1,src2=None):
      super(BrilBooleanMathInsn, self).__init__(dest)
      self.op = op
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      if self.op.lower() == "not": 
         return [RVIRRegImmInsn('xori',self.dest,self.src1, 1)]
      return [RVIRRegRegInsn(self.op.lower(),self.dest,self.src1,self.src2)]