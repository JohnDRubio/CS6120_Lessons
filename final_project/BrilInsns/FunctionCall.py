import ValueOperationInsn

class FunctionCall(ValueOperationInsn):

  def __init__(self, func, dest=None, args=None):
      super(FunctionCall, self).__init__(dest)
      self.func = func
      self.args = args

  def conv_riscvir(self):
      '''
      if args != None:
        if args.size <= 8:
          start from a0 and push arguments all the way to a7 if necessary
        else:
          start from a0 and push arguments all the way to a7 if necessary
          push all arguments after

      jal x0, func
      if dest != None:
        addi dest, x0, a0
      '''

      pass 