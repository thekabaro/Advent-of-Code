myFile = open("../input.txt", "r")

total = 0
while (True):
    myString = myFile.readline()
    myString = myString.strip()
    if (not myString):
        break
    myNums = myString.split("\t")
    largest = myNums[0]
    smallest = myNums[0]
    for num in myNums:
        if (int(num) > int(largest)):
            largest = num
        if (int(num) < int(smallest)):
            smallest = num
    total += (int(largest) - int(smallest))

print(total)