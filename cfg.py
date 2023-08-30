import json

file = open('myCode.json')
data = json.load(file)


def formBasicBlocks(insns):
    basicBlocks = []
    currBlock = []
    for i in insns:
        if 'label' in i:
            basicBlocks.append(currBlock)
            currBlock = []
            currBlock.append(i)
        elif 'br' in i['op'] or 'jmp' in i['op']:
            currBlock.append(i)
            basicBlocks.append(currBlock)
            currBlock = []
        else:
            currBlock.append(i)
    basicBlocks.append(currBlock)
    return basicBlocks

for i in data['functions']:
    blocks = formBasicBlocks(i['instrs'])

for block in blocks:
    print(block)
    print("=================\n")