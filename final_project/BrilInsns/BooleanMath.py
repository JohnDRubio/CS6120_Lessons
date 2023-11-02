import ValueOperationInsn

class BooleanMath(ValueOperationInsn):

  def __init__(self,dest,src1,src2=None):
      super(BooleanMath, self).__init__(dest)
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      pass 