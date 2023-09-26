class Stack:
  def __init__(self):
    self.list = []

  def push(self,x):
    self.list.append(x)

  def pop(self):
    return self.list.pop()

  def peek(self):
    return self.list[-1]

  def size(self):
    return len(self.list)