from BrilInsns.BrilInsn import BrilInsn


class BrilLabelInsn(BrilInsn):

  def __init__(self,label):
      self.label = label

  def conv_riscvir(self):
      # .label
      pass 