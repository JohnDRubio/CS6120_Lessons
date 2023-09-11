import lesson02 as blocks
import json
import sys

def worklist(cfg, transfer, init, merge, direction):
  ins = {}
  outs = {}
  worklist = []
  for label in cfg:
    ins[label] = init # TODO: algorithm only says entry block gets set to init
    outs[label] = init
    worklist.append(label)

  while len(worklist) != 0:
    b_label = worklist[0]
    ins[b_label] = {} # TODO: calculate
    outs[b_label] = {} # TODO: calculate

  return ins, outs

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        basicBlocks = blocks.formBasicBlocks(func['instrs'])
        cfg = blocks.createCFG(basicBlocks)
        ins, outs = worklist(cfg, -1, -1, -1, -1)


if __name__ == "__main__":
    main()