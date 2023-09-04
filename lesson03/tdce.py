import itertools
import json
import sys
import blocks

##TODO: Implement trivial dead code elimination (v1)
##TODO: Modify blocks in place rather than creating a new list (if time allows)
def tdce(blocks):
    # pass 1: Within a block, delete vars that are def'd but never used
    newBlocks = []
    for block in blocks:
        remove = []
        used = []
        defined = []
        changed = True
        for insn in block:
            if 'dest' in insn:
                defined.append(insn['dest'])
            if 'args' in insn:
                for var in insn['args']:
                    used.append(var)
        print('DEST')
        print(str(defined))
        print('ARGS')
        print(str(used))
        # pass 2: Any insn that's been def'd but never used gets removed
        for insn in block:
            if 'dest' in insn and insn['dest'] not in used:
                remove.append(insn)                
            newBlock = [ x for x in block if x not in remove ]
        # print("remove")
        # print(str(remove))
        newBlocks.append(newBlock)
    return newBlocks

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        basicBlocks = blocks.formBasicBlocks(func)
        # print(len(basicBlocks))
        basicBlocks = tdce(basicBlocks)
        # print(len(basicBlocks))
        # blocks.printBasicBlocks(basicBlocks)
        func['instrs'] = list(itertools.chain(*basicBlocks))
        # print(str(func))
    json.dump(program, sys.stdout, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()