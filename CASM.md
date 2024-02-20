# Instructions
Check out the INSTRUCTIONS.md

## Basic

 Comment, the casm assembler support those format of comment:

    CODE ...
    ; Comment

casm assembler don't support:

    CODE ; Comment

## Hello World

    ; Print Hello
    outi Hello
    ; Print World
    outi World
    ; Stop the PC
    halt

To run it assemble the program with `python3 c8/assembler.py helloworld.casm a.out`, then `python3 emulator.py 10 a.out`

## Storing Data

To store data in Reg 0

    ldi 0 DATA

To store data in Ram 0

    movi 0 DATA

To load data from Ram 0 to Reg 1

    ld 1 0

To load date from Reg 0 to Ram 1

    mov 1 0

## ADD / SUB

To add the Reg 0 1 and the out is in 2

    add 2 0 1

To sub the Reg 0 1 and the out is in 2

    sub 2 0 1

## Logic

c8 cpu support or, xor, and

or

    or 0 1 2

if reg 1 or reg 2 and return 0 in reg 0

xor

    xor 0 1 2

if reg 1 xor reg 2 and return 0 in reg 0

and

    and 0 1 2

if reg 1 and reg 2 and return 0 in reg 0

## I/O

To output data

    outi DATA

To output Reg 0 

    out 0

To clear output

    cout

To get input to Reg 0

    in 0

## Loop

There were two loop method: jmp jcn

jmp is for forever loop

jcn is for coditional loop

Forever loop

    outi Forever
    outi Loop
    jmp 0
    halt

Coditional loop

    ldi 1 5
    outi Coditional
    outi Loop
    inc 0
    jcn 0 1 6
    jmp 0
    halt

## Functions

To create functions in casm we can use jmp

    ; Hello World function
    jmp 4
    outi Hello
    outi World
    halt

    ; Calling the function
    jmp 1

## IF / Else

    ; Basic If / Else (Out: Hello)
    ldi 0 Hello
    ldi 1 Hi
    jcn 0 1 5
    out 0
    halt
    out 1
    halt

If the Reg 0 == 1 the program output "Hi" else it output "Hello"

    ; Basic If / Else (Out: Hi)
    ldi 0 Hi
    ldi 1 Hi
    jcn 0 1 5
    out 0
    halt
    out 1
    halt
