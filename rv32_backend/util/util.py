import json
import sys
import util.cfg as cfg
import itertools

# from BrilInsns import *
from BrilInsns.BrilLabelInsn import BrilLabelInsn
from BrilInsns.BrilAddInsn import BrilAddInsn
from BrilInsns.BrilSubInsn import BrilSubInsn
from BrilInsns.BrilAndInsn import BrilAndInsn
from BrilInsns.BrilBooleanLiteralInsn import BrilBooleanLiteralInsn
from BrilInsns.BrilBooleanMathInsn import BrilBooleanMathInsn
from BrilInsns.BrilBranchInsn import BrilBranchInsn
from BrilInsns.BrilConstInsn import BrilConstInsn
from BrilInsns.BrilDivInsn import BrilDivInsn
from BrilInsns.BrilEffectOperationInsn import BrilEffectOperationInsn
from BrilInsns.BrilFunctionCallInsn import BrilFunctionCallInsn
from BrilInsns.BrilIdInsn import BrilIdInsn
from BrilInsns.BrilIntegerLiteralInsn import BrilIntegerLiteralInsn
from BrilInsns.BrilIntegerMathInsn import BrilIntegerMathInsn
from BrilInsns.BrilJumpInsn import BrilJumpInsn
from BrilInsns.BrilLabelInsn import BrilLabelInsn
from BrilInsns.BrilMulInsn import BrilMulInsn
from BrilInsns.BrilNopInsn import BrilNopInsn
from BrilInsns.BrilNotInsn import BrilNotInsn
from BrilInsns.BrilOrInsn import BrilOrInsn
from BrilInsns.BrilPrintInsn import BrilPrintInsn
from BrilInsns.BrilRelationalMathInsn import BrilRelationalMathInsn
from BrilInsns.BrilRetInsn import BrilRetInsn
from BrilInsns.BrilValueOperationInsn import BrilValueOperationInsn

# from RVIRInsns import *
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn

from TrivialRegAlloc.IRToMachMapping import IRToMachMapping
from TrivialRegAlloc.TrivialRegisterAllocator import TrivialRegisterAllocator

from util.prologue import Prologue
from util.epilogue import Epilogue
from util.visitor import Visitor

def set_fileName():
    output_filename = 'asm/out.asm'
    if len(sys.argv) > 1:
        if sys.argv[1] == '-o' and len(sys.argv) > 2:
            output_filename = 'asm/'+sys.argv[2]
    return output_filename

def get_frame_size(func):
    '''
        To calculate frame size, must consider:
            - return address saved to stack
            - frame pointer saved to stack
            - the function call in function body with the highest # of args (if > 8, overflow is pushed to stack)
            - temporaries saved to stack (include all local variables)
    '''
    ret_addr_size = 4
    fp_size = 4
    locals = len(get_temps(func))*4
    blocks = cfg.formBasicBlocks(func['instrs'])
    max_nargs = 0
    for block in blocks:
        for insn in block:
            if 'op' in insn:
                if 'call' in insn['op']:
                    if 'args' in insn:
                        if len(insn['args']) > max_nargs:
                            max_nargs = len(insn['args'])
    overflow_arg_size = (max_nargs - 8)*4 if max_nargs > 8 else 0
    saved_regs_size = max_nargs *4      # Assume number saved regs used == number of args
    frame_size = ret_addr_size + fp_size + locals + overflow_arg_size + saved_regs_size
    reserved = frame_size - locals - overflow_arg_size
    return frame_size, reserved

def get_temps(func):
    '''
        Returns a list of all local variables in func.
    '''
    temps = []
    blocks = cfg.formBasicBlocks(func['instrs'])
    for block in blocks:
        for insn in block:
            if 'dest' in insn and insn['dest'] not in temps:
                if 'args' in func and insn['dest'] in func['args']:
                    continue
                temps.append(insn['dest'])
    return temps

def convert_to_RVIRInsns(lis_BrilInsns, frame_size=0, nargs=0, temps=[],args=[]):
    lis_RVIRInsns = []
    for b_insn in lis_BrilInsns:
        if isinstance(b_insn, Prologue) or isinstance(b_insn, Epilogue):    # Part of calling conventions pass
            lis_RVIRInsns.extend(b_insn.conv_riscvir(frame_size=frame_size,nargs=nargs, args=args))
        elif isinstance(b_insn, BrilFunctionCallInsn):                      # Part of calling conventions pass
            lis_RVIRInsns.extend(b_insn.conv_riscvir(nargs=nargs, temps=temps))
        else:
            lis_RVIRInsns.extend(b_insn.conv_riscvir())
    return lis_RVIRInsns

def convert_to_BrilInsn(insn, isFuncName=False):
    relational_ops = ['eq','lt','gt','le','ge']
    if 'op' in insn and insn['op'] in relational_ops:
        return BrilRelationalMathInsn(insn['dest'], insn['args'][0], insn['op'], insn['args'][1])
    if 'label' in insn:
        return BrilLabelInsn(insn['label'], isFuncName)
    if 'op' in insn:
        match insn['op']:
            case 'add':
                return BrilAddInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'mul':
                return BrilMulInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'sub':
                return BrilSubInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'div':
                return BrilDivInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'and':
                return BrilAndInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'or':
                return BrilOrInsn(insn['dest'], insn['args'][0], insn['args'][1])
            case 'not':
                return BrilNotInsn(insn['dest'], insn['args'][0])
            case 'const':
                if insn['type'] == 'int':
                    return BrilIntegerLiteralInsn(insn['dest'], insn['value'])
                return BrilBooleanLiteralInsn(insn['dest'], insn['value'])
            case 'jmp':
                return BrilJumpInsn(insn['labels'][0])
            case 'br':
                return BrilBranchInsn(insn['args'][0], insn['labels'][0], insn['labels'][1])
            case 'call':
                dst = None if 'dest' not in insn else insn['dest']
                args = None if 'args' not in insn else insn['args']
                return BrilFunctionCallInsn(insn['funcs'][0], dst, args)
            case 'ret':
                retval = None if 'args' not in insn else insn['args'][0]
                return BrilRetInsn(retval)
            case 'id':
                return BrilIdInsn(insn['dest'], insn['args'][0])
            case 'print':
                return BrilPrintInsn(insn['args'])
            case 'nop':
                return BrilNopInsn()
            case _:
                return insn
    return insn

def convert_to_BrilInsns(func):
    lis_BrilInsns = []
    blocks = cfg.formBasicBlocks(func['instrs'])
    for i, block in enumerate(blocks):
        for j, insn in enumerate(block):
            if i == 0 and j == 0:
                lis_BrilInsns.append(convert_to_BrilInsn(insn,True))    # function name label
                # insert prologue
                lis_BrilInsns.append(Prologue())
            elif i == len(blocks)-1 and j == len(block)-1:
                # insert epilogue
                lis_BrilInsns.append(convert_to_BrilInsn(insn))         # last function body instruction
                lis_BrilInsns.append(Epilogue())
            else:
                lis_BrilInsns.append(convert_to_BrilInsn(insn))         # ordinary function body instruction
    return lis_BrilInsns

def mangle_bril_insn(vars):
    newVars = []
    for var in vars:
        newVars.append("_"+var)
    return newVars

def mangle(program):
    for func in program['functions']:
        blocks = cfg.formBasicBlocks(func['instrs'])
        for block in blocks:
            for insn in block:
                if 'dest' in insn:
                    insn['dest'] = mangle_bril_insn([insn['dest']])[0]
                if 'args' in insn:
                    insn['args'] = mangle_bril_insn(insn['args'])
        if 'args' in func:
            for arg in func['args']:
                arg['name'] = '_'+arg['name']
        func['instrs'] = list(itertools.chain(*blocks))

def insert_labels(program):
    for func in program['functions']:
        blocks = cfg.formBasicBlocks(func['instrs'], func['name'])
        func['instrs'] = list(itertools.chain(*blocks))

def write_asm(listRISCVObjs):
    asm = []
    for riscvobj in listRISCVObjs:
        if isinstance(riscvobj, RVIRInsn):
            if isinstance(riscvobj, RVIRLabelInsn):
                asm.append(riscvobj.emit_asm())
            else:
                asm.append("\t"+riscvobj.emit_asm())
    return asm

def get_nargs(func):
    if 'args' in func:
        return len(func['args']) 
    return 0

def map_args(lis_RVIRInsns, args):
    # TODO: Dealing with < 8 arg case for now

    tra_regs = ['x5','x6','x7']
    
    # Using regs s1-s11
    idx = 1
    mapping = {}
    for i, insn in enumerate(lis_RVIRInsns):
        if i > 11:
            break
        regs = insn.get_containers()
        new_regs = []
        for reg in regs:
            if reg in args:
                mapping[reg] = idx
                new_regs.append('s'+str(idx)); idx += 1
        while len(new_regs) < len(regs):
            new_regs.append(regs[len(new_regs)])
        insn.cc_update(new_regs)

def use_xregs(RVIRInsnsAfterTrivialRA):
    visitor = Visitor(RVIRInsnsAfterTrivialRA)
    visitor.xregs()

def lower(program, output_file):
  # logic for renaming to 'x' register names
  x_regs = False
  if '-x' in sys.argv:
      x_regs = True
  assembly_code = []
  for func in program['functions']:
    # convert each Bril instruction to a BrilInsn object
    lis_BrilInsns = convert_to_BrilInsns(func)
  
    # convert each BrilInsn object to N RVIRInsn objects
    frame_size, reserved = get_frame_size(func)
    nargs = get_nargs(func)
    temps = get_temps(func)
    func_args = [] if 'args' not in func else func['args']
    lis_RVIRInsns = convert_to_RVIRInsns(lis_BrilInsns, frame_size, nargs, temps, func_args)

    # assign offsets to each instruction
    mapping = IRToMachMapping(lis_RVIRInsns, reserved)
    mapping.assignOffsets()

    # map args -> regs
    map_args(lis_RVIRInsns, func_args)

    # do trivial register allocation
    trivialRegAllocator = TrivialRegisterAllocator(lis_RVIRInsns,mapping)
    RVIRInsnsAfterTrivialRA = trivialRegAllocator.trivialRegisterAllocation()
    
    # convert special regs to x_regs if x_regs flag passed
    if x_regs:
        use_xregs(RVIRInsnsAfterTrivialRA)

    # convert RVIRInsn objects to assembly code
    assembly_code.extend(write_asm(RVIRInsnsAfterTrivialRA))

  with open(output_file, 'w') as file:
        for insn in assembly_code:
            file.write(insn + '\n')