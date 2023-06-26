// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/Max.asm

// Computes R2 = max(R0, R1)  (R0,R1,R2 refer to RAM[0],RAM[1],RAM[2])

   @R0
   D=M              // D = first number 001
   @R1
   D=D-M            // D = first number - second number 001
   @OUTPUT_FIRST
   D;JGT            // if D>0 (first is greater) goto output_first  000
   @R1
   D=M              // D = second number 001
   @OUTPUT_D
   0;JMP            // goto output_d 000
(OUTPUT_FIRST)
   @R0             
   D=M              // D = first number 001
(OUTPUT_D)
   @R2
   M=D              // M[2] = D (greatest number) 010
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop 000
