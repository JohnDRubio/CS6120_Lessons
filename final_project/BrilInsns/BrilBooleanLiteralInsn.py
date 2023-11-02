import BrilConstInsn

class BrilBooleanLiteralInsn(BrilConstInsn):

  def __init__(self,dest,value):
      super(BrilBooleanLiteralInsn, self).__init__(dest)
      self.value = value

  def conv_riscvir(self):
      # if value == true
      #   addi dest, x0, 1
      # else
      #   addi dest, x0, 0
      pass 