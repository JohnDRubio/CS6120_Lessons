from BrilInsns.BrilValueOperationInsn import BrilValueOperationInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilRelationalMathInsn(BrilValueOperationInsn):

  numRel = 1
  non_RV_rel_ops = ['le', 'gt']     # these ops are in Bril but not RISC-V
  def __init__(self,dest,src1,op,src2):
      super(BrilRelationalMathInsn, self).__init__(dest)
      
      # if relational op is a 'Bril-only' op, invert the op
      # and swap the operands
      if op in self.non_RV_rel_ops:
         op = 'ge' if op == 'le' else 'lt'
         src1, src2 = src2, src1
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
      freshLabel = "."+self.op+str(BrilRelationalMathInsn.numRel)
      exitCond = ".exit_cond"+str(BrilRelationalMathInsn.numRel)
      insns.append(RVIRBranchInsn('b'+self.op,self.src1,self.src2,freshLabel))
      insns.append(RVIRRegImmInsn('addi',self.dest,'x0', 0))
      insns.append(RVIRJumpInsn('jal','x0',exitCond))
      insns.append(RVIRLabelInsn(freshLabel))
      insns.append(RVIRRegImmInsn('addi',self.dest,'x0', 1))
      insns.append(RVIRLabelInsn(exitCond))
      BrilRelationalMathInsn.numRel+=1
      return insns 