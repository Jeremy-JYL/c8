# cASM

## Instructions

| ASM   | BIN       | MEAN              |
|-------|-----------|-------------------|
| NOP   | 0000 0000 | NOTHING           |
| JMP   | 0000 0001 | JUMP UNCODITIONAL |
| JCN   | 0000 0010 | JUMP CODITIONAL   |
| LDI   | 0000 0011 | LOAD IMMEDIATE    |
| LD    | 0000 0100 | LOAD              |
| MOVI  | 0000 0101 | MOVE IMMEDIATE    |
| MOV   | 0000 0110 | MOVE              |
| OUTI  | 0000 0111 | OUTPUT IMMEDIATE  |
| OUT   | 0000 1000 | OUTPUT            |
| INC   | 0000 1001 | INCREASE          |
| DEC   | 0000 1010 | DECREASE          |
| ADD   | 0000 1011 | ADD               |
| SUB   | 0000 1100 | SUBTRACT          |
| OR    | 0000 1101 | OR LOGIC          |
| XOR   | 0000 1110 | XOR LOGIC         |
| AND   | 0000 1111 | AND LOGIC         |
| HALT  | 0001 0000 | HALT              |
| IN    | 0001 0001 | INPUT             |
-----------------------------------------

## Instructions Format
| OPCODES | OPERENDS          |
|---------|-------------------|
| NOP     | N/A               |
| JMP     | ADDRESS           |
| JCN     | REG REG ADDRESS   |
| LDI     | REG VALUE         |
| LD      | REG RAM           |
| MOVI    | RAM VALUE         |
| MOV     | RAM REG           |
| OUTI    | VALUE             |
| OUT     | REG               |
| INC     | REG               |
| DEC     | REG               |
| ADD     | REG REG REG       |
| SUB     | REG REG REG       |
| OR      | REG REG REG       |
| XOR     | REG REG REG       |
| AND     | REG REG REG       |
| HALT    | N/A               |
| IN      | REG               |
-------------------------------
