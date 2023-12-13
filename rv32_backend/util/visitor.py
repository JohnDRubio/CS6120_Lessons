# from RVIRInsns import *
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn


class Visitor:
    def __init__(self, RVIRInsnList):
        self.insns = RVIRInsnList

    def convert_registers(self):
        for insn in self.insns:
            insn.convert_registers(self)
    
    def xregs(self):
        for insn in self.insns:
            insn.xregs(self)
    # ====================================================================
    # RVIRBranchInsn Visitor Methods
    # ====================================================================
    def RVIRBranchInsn_convert_registers(self, insn):
        insn.src1 = 'x5' if insn.src1 not in insn.isa_regs else insn.src1
        insn.src2 = 'x6' if insn.src2 not in insn.isa_regs else insn.src2
    
    # For Calling Conventions
    def RVIRBranchInsn_get_containers(self, insn):
        return insn.src1, insn.src2

    def RVIRBranchInsn_cc_update(self, insn, new_regs):
        insn.src1, insn.src2 = new_regs
    
    def RVIRBranchInsn_xregs(self, insn):
        insn.src1 = insn.src1 if insn.src1 not in insn.reg_map else insn.reg_map[insn.src1]
        insn.src2 = insn.src2 if insn.src2 not in insn.reg_map else insn.reg_map[insn.src2]

    # ====================================================================
    # RVIRJumpInsn Visitor Methods
    # ====================================================================
    def RVIRJumpInsn_convert_registers(self, insn):
        if insn.isFunc and insn.op.upper == 'JAL':
                insn.src1 = 'x1' if insn.src1 not in insn.isa_regs else insn.src1
        else:       # Unconditional jmp (within a function) or JALR
            insn.src1 = 'x0' if insn.src1 not in insn.isa_regs else insn.src1
    
    # For Calling Conventions
    def RVIRJumpInsn_get_containers(self, insn):
        return insn.src1, insn.jmp_target

    def RVIRJumpInsn_cc_update(self, insn, new_regs):
        insn.src1, insn.jmp_target = new_regs
    
    def RVIRJumpInsn_xregs(self, insn):
        insn.src1 = insn.src1 if insn.src1 not in insn.reg_map else insn.reg_map[insn.src1]
        insn.jmp_target = insn.jmp_target if insn.jmp_target not in insn.reg_map else insn.reg_map[insn.jmp_target]
    # ====================================================================
    # RVIRMemInsn Visitor Methods
    # ====================================================================
    def RVIRMemInsn_convert_registers(self, insn):
        insn.src2 = 'x5' if insn.src2 not in insn.isa_regs else insn.src2
        insn.src1 = 'x6' if insn.src1 not in insn.isa_regs else insn.src1

    # For Calling Conventions
    def RVIRMemInsn_get_containers(self, insn):
        return insn.src1, insn.src2

    def RVIRMemInsn_cc_update(self, insn, new_regs):
        insn.src1, insn.src2 = new_regs

    def RVIRMemInsn_xregs(self, insn):
        insn.src1 = insn.src1 if insn.src1 not in insn.reg_map else insn.reg_map[insn.src1]
        insn.src2 = insn.src2 if insn.src2 not in insn.reg_map else insn.reg_map[insn.src2]
    # ====================================================================
    # RVIRRegImmInsn Visitor Methods
    # ====================================================================
    def RVIRRegImmInsn_convert_registers(self, insn):
        insn.src1 = 'x5' if insn.src1 not in insn.isa_regs else insn.src1
        insn.dst = 'x6'  if insn.dst not in insn.isa_regs else insn.dst
    
    # For Calling Conventions
    def RVIRRegImmInsn_get_containers(self, insn):
        return insn.dst, insn.src1

    def RVIRRegImmInsn_cc_update(self, insn, new_regs):
        insn.dst, insn.src1 = new_regs

    def RVIRRegImmInsn_xregs(self, insn):
        insn.dst = insn.dst if insn.dst not in insn.reg_map else insn.reg_map[insn.dst]
        insn.src1 = insn.src1 if insn.src1 not in insn.reg_map else insn.reg_map[insn.src1]
    # ====================================================================
    # RVIRRegRegInsn Visitor Methods
    # ====================================================================
    def RVIRRegRegInsn_convert_registers(self, insn):
        insn.src1 = 'x5' if insn.src1 not in insn.isa_regs else insn.src1
        insn.src2 = 'x6' if insn.src2 not in insn.isa_regs else insn.src2
        insn.dst = 'x7' if insn.dst not in insn.isa_regs else insn.dst
    
    # For Calling Conventions
    def RVIRRegRegInsn_get_containers(self, insn):
        return insn.dst, insn.src1, insn.src2

    def RVIRRegRegInsn_cc_update(self, insn, new_regs):
        insn.dst, insn.src1, insn.src2 = new_regs
    
    def RVIRRegRegInsn_xregs(self, insn):
        insn.dst = insn.dst if insn.dst not in insn.reg_map else insn.reg_map[insn.dst]
        insn.src1 = insn.src1 if insn.src1 not in insn.reg_map else insn.reg_map[insn.src1]
        insn.src2 = insn.src2 if insn.src2 not in insn.reg_map else insn.reg_map[insn.src2]
    # ====================================================================
    # RVIRSpecialRegImmInsn Visitor Methods
    # ====================================================================
    def RVIRSpecialRegImmInsn_convert_registers(self, insn):
        insn.dst = 'x5' if insn.dst not in insn.isa_regs else insn.dst
    # For Calling Conventions
    def RVIRSpecialRegImmInsn_get_containers(self, insn):
        return insn.dst

    def RVIRSpecialRegImmInsn_cc_update(self, insn, new_regs):
        insn.dst = new_regs

    def RVIRSpecialRegImmInsn_xregs(self, insn):
        insn.dst = insn.dst if insn.dst not in insn.reg_map else insn.reg_map[insn.dst]