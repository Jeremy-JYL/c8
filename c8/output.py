import os

def list_to_string(lst):
    return " ".join(map(str, lst))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def output(clk, pc, ram, reg, out, inst, cycle):
    clear()
    print("# C8 CPU")
    print(f"Clock: {clk} Hz")
    print(f"Cycle: {cycle}")
    cycle += 1
    print(f"PC: {pc}")
    print(f"REG: {list_to_string(reg)}")
    print(F"OUT: {list_to_string(out)}")
    print(f"RAM: \n{list_to_string(ram)}")
    print("# CURRENT INSTRUCTION")
    print(f"{inst}")
    return cycle