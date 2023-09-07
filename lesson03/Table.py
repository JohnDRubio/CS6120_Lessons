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

    def updateEnv(self, var, num):
        self.var2num[var] = num
    
    def getValue(self, num):
        for key in self.table:
            if self.table[key][1] == num:
                return key
        return -1, -1