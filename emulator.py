from c8 import emulate
import sys

if len(sys.argv) < 2:
    print("c8 Emulator")
    print("emulator [CLOCK SPEED] [BIN FILE]")
    print("Clock Speed: 100Hz, Recommand")
    print("Clock Speed: M, Manual")
    exit()
else:
    emulate.emulate(sys.argv[2], sys.argv[1])
