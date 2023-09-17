from enum import Enum
from cfg import formBasicBlocks, createCFG

class Worklist:
  def __init__(self, insns, init, merge, transfer, direction):
      self.init = init
      self.insns = insns
      self.merge = merge
      self.transfer = transfer
      self.direction = direction
      self.cfg = {}
      self.basicBlocks = []

  def setup(self):
    self.basicBlocks = formBasicBlocks(self.insns['instrs'])
    self.cfg = createCFG(self.basicBlocks)[0]
    self.predecessors = self.buildPredecessorList()