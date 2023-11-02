import IntegerMath

class Mul(IntegerMath):

  def __init__(self,dest,src1,src2):
      super(Mul, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # mul dest, src1, src2
      pass 