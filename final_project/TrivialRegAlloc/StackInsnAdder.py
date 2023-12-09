from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRInsn import RVIRInsn

# Using x5, x6, x7 as the shuttle register (they are caller saved)

class StackInsnAdder():

  def __init__(self,lis_RVIRInsns,mapping):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = mapping

  def trivialRegisterAllocation(self):
    # TODO: these functions below just add the insns before and after, still need
    # to update the actual instruction to use the RISCV registers

    newInsns = [] # should only have real registers -> only insns not done would be BrilCallInsns 
                   # (just passing them through below)

    for insn in self.lis_RVIRInsns:
      if isinstance(insn, RVIRInsn):
        dest, beforeInsns = self.insnsBefore(insn)
        newInsns.extend(beforeInsns)
        newInsns.append(insn)
        afterInsns = self.insnsAfter(insn,dest)
        newInsns.extend(afterInsns)
      else:
        newInsns.append(insn)

    return newInsns

  def insnsBefore(self,insn):
    beforeInsns = []
    uses = insn.uses() 
    currReg = 5
    for temp in uses:
      offset = self.mapping.getOffset(temp)
      beforeInsns.append(RVIRMemInsn('lw','x'+str(currReg),'fp', offset))
      currReg += 1

    # currReg here is the destination register to use
    return currReg, beforeInsns

  def insnsAfter(self,insn,dest):
    # write value in the dest register to the location of the write temp
    afterInsns = []
    writes = insn.writes() # should only be one value
    for temp in writes:
      offset = self.mapping.getOffset(temp)
      afterInsns.append(RVIRMemInsn('sw','x'+str(dest),'fp', offset))

    return afterInsns