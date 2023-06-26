// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@SCREEN
D=A

@screen_address
M=D

@KBD
D=A

@keyboard_address
M=D


(CHECK)
@screen_address
D=M
@next_screen_address
M=D

@KBD
D=M

@UNFILL_LOOP
D;JEQ



(FILL_LOOP)
@next_screen_address
A=M
M=-1

@next_screen_address
M=M+1

@keyboard_address
D=M

@next_screen_address
D=D-M

@CHECK
D;JEQ

@FILL_LOOP
0;JMP


(UNFILL_LOOP)
@next_screen_address
A=M
M=0

@next_screen_address
M=M+1

@keyboard_address
D=M

@next_screen_address
D=D-M

@CHECK
D;JEQ

@UNFILL_LOOP
0;JMP
