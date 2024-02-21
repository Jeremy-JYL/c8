from c8 import cpu
from c8 import output
import time, sys

def clock(clk):
    if clk == "M":
        input()
    else:
        clk = 1 / int(clk)
        time.sleep(clk)

def emulate(file, clk):
    with open(file, "r") as f:
        code = f.readlines()
    pc = 0
    out = []
    cycle = 0
    while True:
        try:
            pc, out = cpu.cpu(code[pc].split()[0], code[pc].split()[1:], pc, out)
            cycle = output.output(clk, pc, cpu.ram.ram, cpu.reg, out, str(code[pc]), cycle)
            clock(clk)
        except cpu.halt:
            break
        except KeyboardInterrupt:
            break
        except IndexError:
            print("Cannot find HALT")
            sys.exit(1)
