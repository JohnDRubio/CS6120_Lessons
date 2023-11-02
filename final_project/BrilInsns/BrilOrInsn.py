import BrilBooleanMathInsn

class BrilOrInsn(BrilBooleanMathInsn):

  def __init__(self,dest,src1,src2):
      super(BrilOrInsn, self).__init__(dest,src1,src2)

  def conv_riscvir(self):
      # or dest, src1, src2
      pass