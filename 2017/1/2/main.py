myFile = open("../input.txt", "r")
myString = myFile.read().strip()

total = 0
half = int(len(myString) / 2)
for i in range(len(myString)):
    num = i + half
    while (num >= len(myString)):
        num -= len(myString)
    if (myString[i] == myString[num]):
        total += int(myString[num])

print(total)