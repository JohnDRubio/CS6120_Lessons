import BooleanMath

class And(BooleanMath):

  def __init__(self,dest,src1,src2):
      super(And, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # and dest, src1, src2
      pass