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

class BrilRelationalMathInsn(BrilValueOperationInsn):

  def __init__(self,dest,src1,op,src2):
      super(BrilRelationalMathInsn, self).__init__(dest)
      self.op = op
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      # TODO: need to make sure that if we have multiple relational maths, that we change up the label
      '''
      b(op) src1, src2, .freshLabel; 
      addi dest, x0, 0; 
      jal x0 .exit_cond;  
      .freshLabel: addi dest, x0, 1;
      .exit_cond:
      '''
      insns = []
      freshLabel = "" # TODO: generate fresh label
      exitCond = "" # TODO: generate fresh label for exit_cond
      insns.append(RVIRBranchInsn('b'+self.op,self.src1,self.src2,freshLabel))
      insns.append(RVIRRegImmInsn('addi',self.dest,'x0', 0))
      insns.append(RVIRJumpInsn('jal','x0',exitCond))
      # TODO: add label instruction for freshLabel
      insns.append(RVIRRegImmInsn('addi',self.dest,'x0', 1))
      # TODO: add label instruction for exit_cond

      return insns 