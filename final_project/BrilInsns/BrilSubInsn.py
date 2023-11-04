from BrilInsns.BrilIntegerMathInsn import BrilIntegerMathInsn


class BrilSubInsn(BrilIntegerMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilSubInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # sub dest, src1, src2
      pass 