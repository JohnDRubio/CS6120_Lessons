import BrilEffectOperationInsn

class BrilBranchInsn(BrilEffectOperationInsn):

  def __init__(self, cond, label1, label2):
      self.cond = cond
      self.label1 = label1
      self.label2 = label2

  def conv_riscvir(self):
      '''
      addi x, x0, 1;
      beq cond, x, label1;
      jal x0, label2; 
      '''
      pass 