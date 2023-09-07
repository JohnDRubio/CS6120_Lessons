import tdce
from Table import Table
import itertools
import json
import sys
import blocks

def construct_value(insn, lvn_table):
    if insn['op'] == 'id':
        arg = insn['args'][0]
        num = lvn_table.var2num[arg]
        lvn_table.var2num[insn['dest']] = num
        value = lvn_table.getValue(num)
        return value
        # if value[0] != 'id':
        #     nums = []
        #     for a in insn['args']:
        #         nums.append(lvn_table.var2num[a])
        #     # sort list so (ADD, 0, 2) == (ADD, 2, 0) can be more easily supported
        #     nums.sort()
        #     return (insn['op'],) + tuple(nums)
        # else:
        #     lvn_table.var2num[insn['dest']] = num
        #     print('value[1]')
        #     print(value[1])
        #     return value
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
        
def lvn_helper(block):
    lvn_table = Table()
    for i,insn in enumerate(block):
        value = ()
        if 'op' in insn:

            # Construct value 
            if 'args' in insn:
                value = construct_value(insn, lvn_table)
                # print("insn: "+str(insn)+'\n value: '+str(value))
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
                        insn['args'] = [lvn_table.table[value][0]]
                        insn['op'] = 'id'
                    else:
                        insn['args'] = [lvn_table.table[value][0]]

            
            # print(lvn_table)
            # print('\n\n')

    return block

def lvn(blocks):
    newBlocks = []
    for block in blocks:
        newBlock = lvn_helper(block)
        newBlocks.append(newBlock)
    return newBlocks

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        basicBlocks = blocks.formBasicBlocks(func)
        basicBlocks = lvn(basicBlocks)
        # basicBlocks = tdce.tdce_opt1(basicBlocks)
        # basicBlocks = tdce.tdce_opt2(basicBlocks)
        func['instrs'] = list(itertools.chain(*basicBlocks))
    json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()