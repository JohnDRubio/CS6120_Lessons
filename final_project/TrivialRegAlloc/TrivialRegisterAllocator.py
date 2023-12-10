from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRInsn import RVIRInsn

class TrivialRegisterAllocator():
  '''
    When lowering from RVIR to RISC-V, register allocation is required.
    Here, we define a class that allows users to instantiate an instance
    of a register allocator. This particular register allocator uses
    trivial register allocation. The shuttle registers used are the
    caler-saved RISC-V registers: x5, x6, and x7.
  '''
  def __init__(self,lis_RVIRInsns,mapping):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = mapping

  def trivialRegisterAllocation(self):
    '''
      Replaces all abstract registers with machine registers for all instructions.
      Key assumption: For an arbitrary RVIR instruction, uses[0] -> 'x5', 
      uses[1] -> 'x6'. dest -> most recent register allocated + 1.
    '''
    newInsns = [] # should only have real registers -> only insns not done would be BrilCallInsns 
                   # (just passing them through below)

    for insn in self.lis_RVIRInsns:
      if isinstance(insn, RVIRInsn):
        dest, beforeInsns, abstract_idx = self.insnsBefore(insn)
        newInsns.extend(beforeInsns)    # insert 'before' TRA instructions
        insn.convert_registers()        # convert all abstract registers to machine registers 
        newInsns.append(insn)           # insert 'after TRA instructions
        afterInsns = self.insnsAfter(insn,dest,abstract_idx)
        newInsns.extend(afterInsns)
      else:
        newInsns.append(insn)

    return newInsns

  def insnsBefore(self,insn):
    '''
      Returns tuple: (currReg, beforeInsn)
      currReg: Next register available for allocation
      beforeInsn: list of RVIRMemInsn instances implementing 
      'before working instruction' TRA logic.

      len(uses) == # abstract src regs
    '''
    beforeInsns = []
    uses = insn.uses() 
    currReg = 5
    abstract_idx = 0
    for reg in uses:
      if reg not in insn.isa_regs:
        temp = insn.get_abstract_registers()[abstract_idx]
        offset = self.mapping.getOffset(temp)
        beforeInsns.append(RVIRMemInsn('lw','x'+str(currReg),'fp', offset))
        abstract_idx += 1
      currReg += 1
    return currReg, beforeInsns, abstract_idx

  def insnsAfter(self,insn,dest, abstract_idx):
    '''
      Returns list of RVIRMemInsn instances implementing
      'after working instruction' TRA logic.
    '''
    afterInsns = []   
    writes = insn.writes() # should only be one value
    for reg in writes:
      if reg not in insn.isa_regs:
        temp = insn.get_abstract_registers()[abstract_idx]
        offset = self.mapping.getOffset(temp)
        afterInsns.append(RVIRMemInsn('sw','x'+str(dest),'fp', offset))
        abstract_idx = 0
    return afterInsns