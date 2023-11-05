from BrilInsns.BrilIntegerMathInsn import BrilIntegerMathInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilAddInsn(BrilIntegerMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilAddInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # add dest, src1, src2
      pass 

# b = BrilAddInsn("a","b","c")
r = RVIRRegRegInsn("add","b","c","d")
# print(b.dest)