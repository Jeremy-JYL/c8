import sys, os

def assembler(asm):
    asm = asm.upper()
    opcode = {
        "NOP": "00000000",
        "JMP": "00000001",
        "JCN": "00000010",
        "LDI": "00000011",
        "LD": "00000100",
        "MOVI": "00000101",
        "MOV": "00000110",
        "OUTI": "00000111",
        "OUT": "00001000",
        "INC": "00001001",
        "DEC": "00001010",
        "ADD": "00001011",
        "SUB": "00001100",
        "OR": "00001101",
        "XOR": "00001110",
        "AND": "00001111",
        "HALT": "00010000",
        "IN": "00010001"
    }
    return opcode[asm]

def list_to_string(lst):
    return " ".join(map(str, lst))

if len(sys.argv) < 3:
    print("c8 ASM assembler")
    print("assembler [ASM FILE] [OUTPUT FILE]")
    exit()

try:
    os.remove(sys.argv[2])
except:
    pass

try:
    with open(sys.argv[1], "r") as f:
        for i in f:
            with open(sys.argv[2], "a") as f:
                if i.startswith(";"):
                    pass
                elif i == "\n":
                    pass
                else:
                    f.write(f"{assembler(i.split()[0])} {list_to_string(i.split()[1:])}\n")
except FileNotFoundError:
    print(f"Can't find the file!")
    exit(1)
except KeyError:
    print(f"Unknown Instructions!")
