import EffectOperationInsn

class Ret(EffectOperationInsn):

  # assume for now that value is an argument
  def __init__(self, value=None):
      self.value = value

  def conv_riscvir(self):
      '''
      if value:
          addi a0, val, 0;
          jalr x0, x1, 0;
      else:
          jalr x0, x1, 0;
      '''
      pass 