from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn

class IRToMachMapping():
  '''
    Helper class to store mapping of abstract
    registers in RVIR to their physical locations
    in memory.
  '''
  def __init__(self,lis_RVIRInsns, reserved=0):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = {}
    self.reserved = reserved

  def assignOffsets(self):
    '''
      Assign 4-byte aligned offsets
      to each abstract register in list 
      of provided RVIR instructions.
    '''
    currentOffset = -self.reserved    # Assuming 32-bit architecture
    for insn in self.lis_RVIRInsns:
      if isinstance(insn, RVIRInsn): # still just pass bril function calls through
        if not isinstance(insn, RVIRJumpInsn) and not isinstance(insn, RVIRBranchInsn):
          abstract_temps = insn.get_abstract_registers()
          for temp in abstract_temps:
            if temp not in self.mapping and temp not in insn.isa_regs:
              self.mapping[temp] = currentOffset
              currentOffset -= 4

  def getOffset(self,var):
    '''
      Returns physical location of abstract register.
    '''
    if var in self.mapping:
      return self.mapping[var]


        


  