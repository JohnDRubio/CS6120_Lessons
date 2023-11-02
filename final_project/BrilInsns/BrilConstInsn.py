import BrilInsn

# maybe don't need IntegerLiteral and BooleanLiteral classes
class BrilConstInsn(BrilInsn):

  def __init__(self,dest):
      self.dest = dest

  def conv_riscvir(self):
      pass 