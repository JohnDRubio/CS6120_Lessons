#imports

class TempMapping():

  # goal of this class is given a list of abstract assembly insns, 
  # creating a mapping of var names to locations
  # TODO: is this on a per function basis? I'm assuming that it is
  def __init__(self,list_aa_insns):
    self.list_aa_insns = list_aa_insns
    self.mapping = {}

  def assignOffsets(self):
    currentOffset = -8
    for insn in self.list_aa_insns:
      # get args
      


  