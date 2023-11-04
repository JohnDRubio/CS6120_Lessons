from BrilInsns.BrilEffectOperationInsn import BrilEffectOperationInsn


class BrilJumpInsn(BrilEffectOperationInsn):

  def __init__(self,label):
      self.label = label

  def conv_riscvir(self):
      # jal x0, .label
      pass 