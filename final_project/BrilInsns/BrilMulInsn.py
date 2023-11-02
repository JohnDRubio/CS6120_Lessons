from BrilIntegerMathInsn import BrilIntegerMathInsn

class BrilMulInsn(BrilIntegerMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilMulInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # mul dest, src1, src2
      pass 