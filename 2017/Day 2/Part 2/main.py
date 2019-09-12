myFile = open("../input.txt", "r")

total = 0
while (True):
    myString = myFile.readline()
    myString = myString.strip()
    if (not myString):
        break
    myNums = myString.split("\t")
    num1 = myNums[0]
    num2 = myNums[0]
    for i in range(len(myNums)):
        for j in range(i + 1, len(myNums)):
            if (int(myNums[i]) > int(myNums[j])):
                if (int(myNums[i]) % int(myNums[j]) == 0):
                    total += int(myNums[i]) / int(myNums[j])
            elif (int(myNums[i]) < int(myNums[j])):
                if (int(myNums[j]) % int(myNums[i]) == 0):
                    total += int(myNums[j]) / int(myNums[i])
            else:
                break

print(int(total))