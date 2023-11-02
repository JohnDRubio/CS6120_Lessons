from BrilConstInsn import BrilConstInsn

class BrilIntegerLiteralInsn(BrilConstInsn):

  def __init__(self,dest,value):
      super(BrilIntegerLiteralInsn, self).__init__(dest)
      self.value = value

  def conv_riscvir(self):
      # addi dest, x0, value
      pass 