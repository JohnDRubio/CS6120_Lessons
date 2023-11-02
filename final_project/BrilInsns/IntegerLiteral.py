import ConstInsn

class IntegerLiteral(ConstInsn):

  def __init__(self,dest,value):
      super(IntegerLiteral, self).__init__(dest)
      self.value = value

  def conv_riscvir(self):
      # addi dest, x0, value
      pass 