from RVIRInsns.RVIRInsn import RVIRInsn

class TempMapping():

  # goal of this class is given a list of abstract assembly insns, 
  # creating a mapping of var names to locations
  # TODO: is this on a per function basis? I'm assuming that it is
  def __init__(self,lis_RVIRInsns):
    self.lis_RVIRInsns = lis_RVIRInsns
    self.mapping = {}

  def assignOffsets(self):
    currentOffset = -8
    for insn in self.lis_RVIRInsns:
      if isinstance(insn, RVIRInsn): # still just pass bril function calls through
        abstract_temps = insn.get_abstract_temps()
        for temp in abstract_temps:
          if temp not in self.mapping:
            self.mapping[temp] = currentOffset
            currentOffset -= 8

  def getOffset(self,var):
    if var in self.mapping:
      return self.mapping[var]
    else:
      # TODO: throw error?


        


  