myFile = open("../input.txt", "r")
total = 0
for line in myFile:
    clear = True
    line = line.strip()
    words = line.split()
    for i in range(len(words)):
        for j in range(len(words)):
            if (j > i and words[i] == words[j]):
                clear = False
    if (clear):
        total += 1
print(total)