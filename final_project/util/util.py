import json
import sys
sys.path.append("../library")
import cfg
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

def convert_to_RVIRInsns(lis_BrilInsns):
    lis_RVIRInsns = []
    for b_insn in lis_BrilInsns:
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
        for insn in block:
            if i == 0:
                lis_BrilInsns.append(convert_to_BrilInsn(insn,True))
            else:
                lis_BrilInsns.append(convert_to_BrilInsn(insn))
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
        func['instrs'] = list(itertools.chain(*blocks))

def insert_labels(program):
    for func in program['functions']:
        blocks = cfg.formBasicBlocks(func['instrs'], func['name'])
        # blocks = cfg.addLabels(blocks, func['name'])
    func['instrs'] = list(itertools.chain(*blocks))


def print_asm(listRISCVObjs):
    asm = []
    for riscvobj in listRISCVObjs:
        if isinstance(riscvobj, RVIRInsn):
            if isinstance(riscvobj, RVIRLabelInsn):
                asm.append(riscvobj.emit_asm())
            else:
                asm.append("\t"+riscvobj.emit_asm())
        else:
            asm.append("TODO: call insn")
    return asm

def lower(program):
  assembly_without_cc = []
  for func in program['functions']:
    # convert each Bril instruction to a BrilInsn object
    lis_BrilInsns = convert_to_BrilInsns(func)
  
    # convert each BrilInsn object to N RVIRInsn objects
    lis_RVIRInsns = convert_to_RVIRInsns(lis_BrilInsns)

    # assign offsets to each instruction
    mapping = IRToMachMapping(lis_RVIRInsns)
    mapping.assignOffsets()

    # do trivial register allocation
    trivialRegAllocator = TrivialRegisterAllocator(lis_RVIRInsns,mapping)
    RVIRInsnsAfterTrivialRA = trivialRegAllocator.trivialRegisterAllocation()

    assembly_without_cc.extend(print_asm(RVIRInsnsAfterTrivialRA))

  for insn in assembly_without_cc:
      print(insn)