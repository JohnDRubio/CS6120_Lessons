from RVIRInsns.RVIRMemInsn import RVIRMemInsn

# Using x5, x6, x7 as the shuttle register (they are caller saved)

class StackInsnAdder():

  def __init__(self,lis_RVIRInsns,mapping):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = mapping

  def trivialRegisterAllocation(self):
    # TODO: these functions below just add the insns before and after, still need
    # to update the actual instruction to use the RISCV registers
    
    pass

  def addInsnsBefore(self,insn):
    beforeInsns = []
    uses = insn.uses() 
    currReg = 5
    for temp in uses:
      offset = self.mapping.getOffset(temp)
      beforeInsns.append(RVIRMemInsn('lw','x'+currReg,'fp', offset))
      currReg += 1

    # currReg here is the destination register to use
    return currReg, beforeInsns

  def addInsnsAfter(self,insn,dest):
    # write value in the dest register to the location of the write temp
    afterInsns = []
    write = insn.writes()[0] # should only be one value
    offset = self.mapping.getOffset(write)
    afterInsns.append(RVIRMemInsn('sw','x'+dest,'fp', offset))

    return afterInsns