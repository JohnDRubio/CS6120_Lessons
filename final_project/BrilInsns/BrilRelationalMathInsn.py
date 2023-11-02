import BrilValueOperationInsn

class BrilRelationalMathInsn(BrilValueOperationInsn):

  def __init__(self,dest,src1,op,src2):
      super(BrilRelationalMathInsn, self).__init__(dest)
      self.op = op
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      # need to make sure that if we have multiple relational maths, that we change up the label
      '''
      b(op) src1, src2, .freshLabel; 
      addi dest, x0, 0; 
      jal x0 .exit_cond;  
      .freshLabel: addi dest, x0, 1;
      .exit_cond:
      '''
      pass 