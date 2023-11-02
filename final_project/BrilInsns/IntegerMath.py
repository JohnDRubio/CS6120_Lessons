import ValueOperationInsn

class IntegerMath(ValueOperationInsn):

  def __init__(self,dest,src1,src2):
      super(IntegerMath, self).__init__(dest)
      self.src1 = src1
      self.src2 = src2

  def conv_riscvir(self):
      pass 