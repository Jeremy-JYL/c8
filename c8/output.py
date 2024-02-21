def list_to_string(lst):
    return " ".join(map(str, lst))

def output(clk, pc, ram, reg, out, inst, cycle):
    print("\033[2J\033[1;1H", end="")
    print("# C8 CPU")
    print(f"Clock: {clk} Hz")
    print(f"Cycle: {cycle}")
    cycle += 1
    print(f"PC: {pc}")
    print("REG")
    print(list_to_string(reg))
    print("# OUT")
    print(list_to_string(out))
    print("# RAM")
    print(list_to_string(ram))
    print("# CURRENT INSTRUCTION")
    print(f"{inst}")
    return cycle
