def split(word):
    return word.split(' ')

def combine(ls):
    res = ''
    for i in range(len(ls)):
        res += ls[i]
        if (i < len(ls) - 1):
            res += ' '
    return res

def list_str_to_int(ls):
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls

def list_int_to_str(ls):
    for i in range(len(ls)):
        ls[i] = str(ls[i])
    return ls

def reallocate(memory):
    memory = split(memory)
    list_str_to_int(memory)
    largest_num = memory[0]
    largest_ind = 0
    for i in range(len(memory)):
        if (memory[i] > largest_num):
            largest_num = memory[i]
            largest_ind = i
    memory[largest_ind] = 0
    while (largest_num > 0):
        largest_ind += 1
        if (largest_ind >= len(memory)):
            largest_ind = 0
        memory[largest_ind] += 1
        largest_num -= 1
    list_int_to_str(memory)
    return combine(memory)

memory = '10 3 15 10 5 15 5 15 9 2 5 8 5 2 3 6'
seen = [memory]
repeat = False
while (True):
    memory = reallocate(memory)
    for i in range(len(seen)):
        if (memory == seen[i]):
            repeat = True
    if (repeat):
        break
    seen.append(memory)

target = memory
repeat = False
cycles = 0
while (True):
    cycles += 1
    memory = reallocate(memory)
    if (memory == target):
        break
print(cycles)