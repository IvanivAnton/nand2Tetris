// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/05/CPU.tst

load CPU.hdl,
output-file CPU.out,
compare-to CPU.cmp,
output-list time%S0.4.0 inM%D0.6.0 instruction%B0.16.0 reset%B2.1.2 outM%D1.6.0 writeM%B3.1.3 addressM%D0.5.0 pc%D0.5.0 DRegister[]%D1.6.1;

set instruction %B1111010011110000, // AD=D-M
set inM 11111,
tick, output, tock, output;

set instruction %B0000000000001110, // @14
tick, output, tock, output;