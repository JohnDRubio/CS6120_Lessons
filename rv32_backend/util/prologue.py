# from RVIRInsns import *
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn

class Prologue:
    def __init__(self):
        pass
    
    def conv_riscvir(self, frame_size=0, nargs=0, args=[]):
        '''
            Push things that need pushing before executing function body.

            This list of things includes:
                - return address
                - frame pointer

            Side-note: if nargs > 8, need to load from stack
                       *overflow args will be saved at bottom of
                       previous stack frame - so can reference using
                       fp + offset
            
            Stack Frame:
            -----------------------------------
                    Ret Address
            -----------------------------------
                    Old Frame Pointer
            -----------------------------------
                    Saved Registers
            -----------------------------------
                    Locals
            -----------------------------------
                    Overflow args
            -----------------------------------
        '''
        insns = []
        # Step 1: create stack frame
        #   addi sp, sp, -frame_size
        insns.append(RVIRRegImmInsn('addi','sp','sp', -frame_size))

        # Step 2: Store return address 
        insns.append(RVIRMemInsn('sw','x1','sp',frame_size-4))

        # Step 3: Store old frame pointer
        insns.append(RVIRMemInsn('sw','fp','sp',frame_size-8))

        # Step 4: Set new frame pointer
        insns.append(RVIRRegImmInsn('addi','fp','sp', frame_size-4))

        # Step 5: Store saved regs
        bound = min(nargs, 8)
        offset = frame_size-12
        for i in range(1,bound+1):
            insns.append(RVIRMemInsn('sw','s'+str(i),'sp',offset))
            offset = offset -4   
        
        # Step 6: Put args into saved registers
        for i in range(len(args)):
            insns.append(RVIRRegRegInsn('add',args[i]['name'],'x0','a'+str(i)))
        return insns
