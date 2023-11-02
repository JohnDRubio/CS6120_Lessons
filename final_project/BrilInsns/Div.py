import IntegerMath

class Div(IntegerMath):

  def __init__(self,dest,src1,src2):
      super(Div, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # sub dst, src1, src2
      pass 