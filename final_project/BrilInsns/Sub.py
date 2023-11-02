import IntegerMath

class Sub(IntegerMath):

  def __init__(self,dest,src1,src2):
      super(Sub, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # sub dest, src1, src2
      pass 