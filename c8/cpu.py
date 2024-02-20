from c8 import ram

reg = [0, 0, 0, 0, 
       0, 0, 0, 0]

class halt(Exception):
    pass

def read(address):
    try:
        return reg[int(address)]
    except ValueError:
        raise Exception("Unknown Reg Address!")

def write(address, data):
    try:
        reg[int(address)] = data
    except IndexError:
        raise Exception("Reg Over Flow!")
    except ValueError:
        raise Exception("Unknown Reg Adress!")

def cpu(opcode, operend, pc, out):
    pc += 1
    match opcode:
        case "00010000":
            raise halt
        case "00000000":
            pass
        case "00000001":
            pc = int(operend[0])
        case "00000010":
            if read(operend[0]) == read(operend[1]):
                pc = int(operend[2])
            else:
                pass
        case "00000011":
            write(operend[0], operend[1])
        case "00000100":
            write(operend[0], ram.read(operend[1]))
        case "00000101":
            ram.write(operend[0], operend[1])
        case "00000110":
            ram.write(operend[0], read(operend[1]))
        case "00000111":
            out.append(operend[0])
        case "00001000":
            out.append(read(operend[0]))
        case "00001001":
            write(operend[0], str(int(read(operend[0])) + 1))
        case "00001010":
            write(operend[0], str(int(read(operend[0])) - 1))
        case "00001011":
            write(operend[0], str(int(read(operend[1])) + int(read(operend[2]))))
        case "00001100":
            write(operend[0], str(int(read(operend[1])) - int(read(operend[2]))))
        case "00001101":
            if read(operend[1]) or read(operend[2]):
                write(operend[0], "1")
        case "00001110":
            if read(operend[1]) != read(operend[2]):
                write(operend[0], "1")
        case "00001111":
            if read(operend[1]) and read(operend[2]):
                write(operend[0], "1")
        case "00010001":
            write(operend[0], input("? "))
        case "00010010":
            out = ""
    return pc, out