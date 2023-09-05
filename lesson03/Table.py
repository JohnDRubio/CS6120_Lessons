class Table:
    def __init__(self):
        self.table = {}
        self.var2num = {}
        self.nrows = 0
    
    def __str__(self):
        return f"VALUE -> (VAR, NUM): {str(self.table)}, VAR -> NUM: {str(self.var2num)}"

    def addRow(self, value, varName):
        self.table[value] = (varName, self.nrows)
        self.var2num[varName] = self.nrows
        self.nrows += 1
        
# test = Table()

# value = "ADD", 1, 2

# test.table[value] = "a", test.nrows

# test.var2num["a"] = test.nrows

# test.nrows += 1

# print(test)