from RVIRInsns.RVIRMemInsn import RVIRMemInsn

# Using x5, x6, x7 as the shuttle register (they are caller saved)

class StackInsnAdder():

  def __init__(self,lis_RVIRInsns,mapping):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = mapping

  def trivialRegisterAllocation(self):
    pass


  # TODO: these functions just add the insns before and after, still need
  # to update the actual instruction to use the RISCV registers

  def addInsnsBefore(self,insn):
    uses = insn.uses() 
    beforeInsns = []
    currReg = 5
    for temp in uses:
      offset = self.mapping.getOffset(temp)
      beforeInsns.append(RVIRMemInsn('lw','x'+currReg,'fp', offset))
      currReg += 1

    # TODO: what do we do after this?
    return beforeInsns

  def addInsnsAfter(self,insn):
    writes = insn.writes()
    afterInsns = []


    return afterInsns