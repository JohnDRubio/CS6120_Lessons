from RVIRInsns.RVIRInsn import RVIRInsn

class IRToMachMapping():
  '''
    Helper class to store mapping of abstract
    registers in RVIR to their physical locations
    in memory.
  '''
  # TODO: is this on a per function basis? I'm assuming that it is
  def __init__(self,lis_RVIRInsns):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = {}

  def assignOffsets(self):
    '''
      Assign 8-byte aligned offsets
      to each abstract register in list 
      of provided RVIR instructions.
    '''
    currentOffset = -8
    for insn in self.lis_RVIRInsns:
      if isinstance(insn, RVIRInsn): # still just pass bril function calls through
        abstract_temps = insn.get_abstract_registers()
        for temp in abstract_temps:
          if temp not in self.mapping and temp not in insn.isa_regs:
            self.mapping[temp] = currentOffset
            currentOffset -= 8

  def getOffset(self,var):
    '''
      Returns physical location of abstract register.
    '''
    if var in self.mapping:
      return self.mapping[var]


        


  