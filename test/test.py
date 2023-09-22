import json
import sys
sys.path.append("../lesson05")
import cfg

def main():
  program = json.load(sys.stdin)
  for func in program['functions']:
     c = cfg.createCFG(func['instrs'])
     print(str(c))

if __name__ == "__main__":
    main()