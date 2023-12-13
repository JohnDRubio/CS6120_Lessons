#---------------------------------------
# sample asm file for tutorial
#---------------------------------------

# set the address where you want this
# code segment


   xor x1, x1, x1
   xori x1, x1, 0x0200
   add x3, x1, x1
   xor x1, x1, x1
   #Loading Data section
   lui x1, 0x0002
   # label_a is 0x000, it's true location is 0x0002000 
   # but sw only takes lower 12-bits
   sw x3,  label_a(x1)
   #data section
   .data
   label_a:
   .word 5000
