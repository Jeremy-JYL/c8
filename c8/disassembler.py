import sys, os
def disassembler(bin):
    asm = {
        "00000000": "NOP",
        "00000001": "JMP",
        "00000010": "JCN",
        "00000011": "LDI",
        "00000100": "LD",
        "00000101": "MOVI",
        "00000110": "MOV",
        "00000111": "OUTI",
        "00001000": "OUT",
        "00001001": "INC",
        "00001010": "DEC",
        "00001011": "ADD",
        "00001101": "SUB",
        "00001110": "OR",
        "00001110": "AND",
        "00010000": "HALT",
        "00010001": "IN",
        "00010010": "COUT"
    }
    return asm[bin]

def list_to_string(lst):
    return " ".join(map(str, lst))

if len(sys.argv) < 3:
    print("c8 BIN disassembler")
    print("disassembler [BIN FILE] [OUTPUT FILE]")
    exit()

try:
    os.remove(sys.argv[2])
except:
    pass

try:
    with open(sys.argv[1], "r") as f:
        for i in f:
            with open(sys.argv[2], "a") as f:
                f.write(f"{disassembler(i.split()[0])} {list_to_string(i.split()[1:])} \n")
except FileNotFoundError:
    print(f"Can't find the file!")
    exit(1)
except KeyError:
    print(f"Unknown Binary!")
