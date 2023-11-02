import BooleanMath

class Not(BooleanMath):

  def __init__(self,dest,src1):
      super(Not, self).__init__(dest,src1)

  def conv_riscvir(self):
      # xori dest, src1, 1
      pass