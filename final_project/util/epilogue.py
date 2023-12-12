# from RVIRInsns import *
from RVIRInsns.RVIRBranchInsn import RVIRBranchInsn
from RVIRInsns.RVIRInsn import RVIRInsn
from RVIRInsns.RVIRJumpInsn import RVIRJumpInsn
from RVIRInsns.RVIRMemInsn import RVIRMemInsn
from RVIRInsns.RVIRRegRegInsn import RVIRRegRegInsn
from RVIRInsns.RVIRRegImmInsn import RVIRRegImmInsn
from RVIRInsns.RVIRSpecialRegImmInsn import RVIRSpecialRegImmInsn
from RVIRInsns.RVIRLabelInsn import RVIRLabelInsn

class Epilogue:
    def __init__(self):
        pass
    
    def conv_riscvir(self, frame_size=0, nargs=0, args=[]):
        '''
            Pop things that need popping before returing.

            This list of things includes:
                - return address
                - frame pointerr

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
        # Step 1: Load saved regs
        bound = min(nargs, 8)
        offset = frame_size-12-(bound-1)*4
        for i in range(bound+1,1,-1):
            insns.append(RVIRMemInsn('lw','s'+str(i-1),'sp',offset))
            offset = offset + 4   

        # Step 2: Retore old frame pointer
        insns.append(RVIRMemInsn('lw','fp','sp',offset))

        # Step 3: Retore return address 
        insns.append(RVIRMemInsn('lw','x1','sp',offset+4))

        # Step 4: Destroy frame
        insns.append(RVIRRegImmInsn('addi','sp','sp', frame_size))

        # Step 5: Return
        insns.append(RVIRJumpInsn('jalr','x0','x1',0))

        return insns


        