from BrilBooleanMathInsn import BrilBooleanMathInsn

class BrilAndInsn(BrilBooleanMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilAndInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # and dest, src1, src2
      pass