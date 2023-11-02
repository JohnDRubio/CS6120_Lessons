import ValueOperationInsn

class Id(ValueOperationInsn):

  def __init__(self,dest,src):
      super(Id, self).__init__(dest)
      self.src = src

  def conv_riscvir(self):
      # addi dest, src, 0
      pass