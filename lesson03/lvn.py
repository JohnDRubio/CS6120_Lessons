import tdce
from Table import Table
import itertools
import json
import sys
import blocks

def construct_value(op, args, lvn_table):
    nums = []
    for a in args:
        nums.append(lvn_table.var2num[a])
    return (op,) + tuple(nums)

''' 
    TODO:
        - Confirm that table is being constructed correctly

        - Implement algorithm:
                    - When we look at an instruction, and one of its args already points to a value
                        in the table, replace that arg with the canonical name in the table

                    -  Handle edge case Adrian mentioned (when insn.dest is rerwritten to later in program)
'''
def lvn_helper(block):
    newBlock = block
    lvn_table = Table()
    for insn in block:
        value = ()
        if 'op' in insn:

            # Construct value 
            if 'args' in insn:
                value = construct_value(insn['op'], insn['args'], lvn_table)
            else:   # 'value' in insn
                value = (insn['op'], insn['value'])

            # Add value to table
            if value not in lvn_table.table:
                if 'dest' in insn:
                    lvn_table.addRow(value, insn['dest'])
            else:
                if 'dest' in insn:
                    lvn_table.var2num[insn['dest']] = lvn_table.table[value][1]
                    insn['args'] = [lvn_table.table[value][0]]
                    insn['op'] = 'id'
            
            print(lvn_table)
            print('\n\n')

    return block
    # return newBlock

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