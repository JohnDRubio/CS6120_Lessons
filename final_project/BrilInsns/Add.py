import IntegerMath

class Add(IntegerMath):

  def __init__(self,dest,src1,src2):
      super(Add, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # add dest, src1, src2
      pass 