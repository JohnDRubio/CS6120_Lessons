import json
import sys
import blocks

def main():
    program = json.load(sys.stdin)
    basicBlocks = blocks.formBasicBlocks(program)
    # printBasicBlocks(basicBlocks)
    json.dump(program, sys.stdout, indent=2, sort_keys=True)

##TODO: Implement trivial dead code elimination (v1)

##TODO: Dump json output to stdout and interpret JSON output using brili

if __name__ == "__main__":
    main()