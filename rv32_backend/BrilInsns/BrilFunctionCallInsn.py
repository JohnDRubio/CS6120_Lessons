from BrilInsns.BrilValueOperationInsn import BrilValueOperationInsn

import sys
sys.path.append("../")
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn

class BrilFunctionCallInsn(BrilValueOperationInsn):

  def __init__(self, func_name, dest=None, args=None):
      super(BrilFunctionCallInsn, self).__init__(dest)
      self.func_name = func_name
      self.args = args

  def get_args(self):
     return self.args
  
  def get_dest(self):
     return self.dest

  def conv_riscvir(self,nargs=0, temps=[]):
      '''
      if args != None:
        if args.size <= 8:
          start from a0 and push arguments all the way to a7 if necessary
        else:
          start from a0 and push arguments all the way to a7 if necessary
          push all arguments after

      jal x1, func
      if dest != None:
        addi dest, x10, x0
      '''
      insns = []
      overflow = len(self.args) - 8 if len(self.args) > 8 else 0
      NARG_REGS = 8
      idx = 0

      # Step 1: Move arguments to arg registers
      while idx < NARG_REGS and idx < len(self.args):
         insns.append(RVIRRegRegInsn('add','a'+str(idx),'x0',self.args[idx])); idx += 1
      
      # Step 2: Push overflow arguments to stack
      for i in range(overflow):     # Will not execute if overflow 
         insns.append(RVIRMemInsn('sw',self.args[idx],'sp',i*4)); idx += 1

      # Step 3: Function call
      insns.append(RVIRJumpInsn('jal','x1',self.func_name,isFunc=True))

      # Step 4: Move result to dest
      if self.dest is not None:
        insns.append(RVIRRegRegInsn('add',self.dest,'a0','x0'))
      return insns