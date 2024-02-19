# c8
This is a python 8bit cpu emulator with assembler and disassembler.

## Spec
1. 64 Ram Address (0 - 63)
2. 8 Reg Address (0 - 7)
3. I/O function (IN & OUT)

# How to use?
Run the example:

`python3 c8/assembler.py example/count_to_10.casm a.out`

`python3 emulator.py 100 a.out`

![](https://github.com/Jeremy-JYL/c8/blob/main/src/example.mov)

# Format
The c8 assembler support comment for example:

    ; Simple counter in casm

    ; Write 10 to Reg 0
    ldi 0 10
    ; Increase in Reg 1
    inc 1
    ; Jump to address 4 if Reg 1 == Reg 0
    jcn 1 0 4
    ; Else Jump to address 0
    jmp 0
    ; Stop the program
    halt

Also, Upper case or Lower case is support.

