myFile = open("../input.txt", "r")
myString = myFile.read()
myString = myString.strip()

total = 0
for i in range(len(myString)):
    if (i == len(myString) - 1):
        if (myString[i] == myString[0]):
            total += int(myString[i])
    else:
        if (myString[i] == myString[i + 1]):
            total += int(myString[i])

print(total)