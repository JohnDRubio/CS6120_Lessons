import BrilBooleanMathInsn

class BrilNotInsn(BrilBooleanMathInsn):

  def __init__(self,dest,src1):
      super(BrilNotInsn, self).__init__(dest,src1)

  def conv_riscvir(self):
      # xori dest, src1, 1
      pass