ram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def write(address, data):
    try:
        ram[int(address)] = data
    except IndexError:
        raise Exception("Ram Over Flow!")
    except ValueError:
        raise Exception("Unknown Ram Address!")

def read(address):
    try:
        return ram[int(address)]
    except ValueError:
        raise Exception("Unknown Ram Address!")
