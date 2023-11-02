import BooleanMath

class Or(BooleanMath):

  def __init__(self,dest,src1,src2):
      super(Or, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # or dest, src1, src2
      pass