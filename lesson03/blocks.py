def removeEmptyBasicBlocks(basicBlocks):
    newBasicBlocks = [x for x in basicBlocks if x != []]
    return newBasicBlocks

def printBasicBlocks(blocks):
    counter = 1
    for block in blocks:
        print('BLOCK '+str(counter))
        counter += 1
        for insn in block:
            print(insn)

def addLabels(basicBlocks):
    num = 0
    for block in basicBlocks:
        if 'label' not in block[0]:
            block.insert(0,{"label": "label_"+str(num)})
            num = num + 1
    return basicBlocks

def formBasicBlocks(program):
    basicBlocks = []
    currBlock = []
    for func in program['functions']:
        for i in func['instrs']:
            if 'label' in i:
                basicBlocks.append(currBlock)
                currBlock = []
                currBlock.append(i)
            elif i['op'] == 'br' or i['op'] == 'jmp' or i['op'] == 'ret':
                currBlock.append(i)
                basicBlocks.append(currBlock)
                currBlock = []
            else:
                currBlock.append(i)
        basicBlocks.append(currBlock)
        basicBlocks = removeEmptyBasicBlocks(basicBlocks)
        basicBlocks = addLabels(basicBlocks)
    return basicBlocks