import tdce
from Table import Table
import itertools
import json
import sys
import blocks

def construct_value(insn, lvn_table):
    for a in insn['args']:
        if a not in lvn_table.var2num:
            lvn_table.addRow(('unknown', a), a)

    if insn['op'] == 'id':
        arg = insn['args'][0]
        num = lvn_table.var2num[arg]
        lvn_table.var2num[insn['dest']] = num
        value = lvn_table.getValue(num)
        return value
    else:
        nums = []
        for a in insn['args']:
            nums.append(lvn_table.var2num[a])
        # sort list so (ADD, 0, 2) == (ADD, 2, 0) can be more easily supported
        nums.sort()
        return (insn['op'],) + tuple(nums)

def willBeOverwritten(num, block, dest):
    for i in range(num+1, len(block)):
        insn = block[i]
        if 'dest' in insn:
            if dest == insn['dest']:
                return True, i
    return False, -1

def generateFreshVar(var, block):
    num = 1
    restart = True
    while restart:
        restart = False
        newVar = var+str(num)
        for insn in block:
            if 'dest' in insn:
                if newVar == insn['dest']:
                    num = num + 1
                    restart = True
                    break
    return newVar
        
def addArguments(args, table):
    for a in args:
        argName = a['name']
        table.addRow(('arg', argName), argName)

def lvn_helper(block, args):
    lvn_table = Table()
    addArguments(args, lvn_table)
    for i,insn in enumerate(block):
        value = ()
        if 'op' in insn:
            # Construct value 
            if 'args' in insn:
                value = construct_value(insn, lvn_table)
            else:   # 'value' in insn
                value = (insn['op'], insn['value'])
            # Add value to table
            if value not in lvn_table.table:
                if 'dest' in insn:
                    # Edge case
                    dest = insn['dest']
                    w, end = willBeOverwritten(i, block, dest)
                    if (w):
                        insn['dest'] = generateFreshVar(dest, block)
                        for n in range(i+1, end):
                            if 'args' in block[n]:
                                newArgs = []
                                for a in block[n]['args']:
                                    if a == dest:
                                        newArgs.append(insn['dest'])
                                    else:
                                        newArgs.append(a)
                                block[n]['args'] = newArgs
                    lvn_table.addRow(value, insn['dest'])
                    # Transforms each insn to use canonical vars for args
                    if 'args' in insn:
                        newArgs = []
                        for arg in insn['args']:
                            num = lvn_table.var2num[arg]
                            for key in lvn_table.table:
                                if lvn_table.table[key][1] == num:
                                    newArgs.append(lvn_table.table[key][0])
                        insn['args'] = newArgs
            else:
                if 'dest' in insn:
                    if insn['op'] != 'id':
                        lvn_table.var2num[insn['dest']] = lvn_table.table[value][1]
                        insn['op'] = 'id'
                    insn['args'] = [lvn_table.table[value][0]]
    
    # print(lvn_table)
    # print('\n')
    
    return block

def lvn(blocks, args):
    newBlocks = []
    for block in blocks:
        newBlock = lvn_helper(block, args)
        newBlocks.append(newBlock)
    return newBlocks

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        basicBlocks = blocks.formBasicBlocks(func)
        basicBlocks = lvn(basicBlocks, func['args'])
        func['instrs'] = list(itertools.chain(*basicBlocks))
    json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()