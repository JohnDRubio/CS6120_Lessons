import BrilIntegerMathInsn

class BrilAddInsn(BrilIntegerMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilAddInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # add dest, src1, src2
      pass 