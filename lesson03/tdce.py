import itertools
import json
import sys
import blocks

##TODO: Implement trivial dead code elimination (v1)
##TODO: Modify blocks in place rather than creating a new list (if time allows)
def tdce(blocks):
    newBlocks = []
    for block in blocks:
        remove = []
        for insn in block:
            if 'dest' in insn and insn['dest'] == 'a':
                remove.append(insn)
        newBlock = [x for x in block if x not in remove ]
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