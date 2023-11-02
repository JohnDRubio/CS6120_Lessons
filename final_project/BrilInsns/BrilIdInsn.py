from BrilValueOperationInsn import BrilValueOperationInsn

class BrilIdInsn(BrilValueOperationInsn):

  def __init__(self,dest,src):
      super(BrilIdInsn, self).__init__(dest)
      self.src = src

  def conv_riscvir(self):
      # addi dest, src, 0
      pass