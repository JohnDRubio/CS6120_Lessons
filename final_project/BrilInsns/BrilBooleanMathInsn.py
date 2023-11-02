import BrilValueOperationInsn

class BrilBooleanMathInsn(BrilValueOperationInsn):

  def __init__(self,dest,src1,src2=None):
      super(BrilBooleanMathInsn, self).__init__(dest)
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      pass 