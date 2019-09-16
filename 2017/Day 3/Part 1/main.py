# CREATE THE GRID
grid = [[1, 2]]
curr_dir = "up"
curr_row = 0
curr_num = 3

print("")
num = input("Enter number to search for: ")
print("")

def change_dir(direction):
    if (direction == "right"):
        return "up"
    elif (direction == "up"):
        return "left"
    elif (direction == "left"):
        return "down"
    else:
        return "right"

while (True):
    length_of_first = len(grid[0])
    length_of_last  = len(grid[len(grid) - 1])
    if ((curr_num > int(num)) and (length_of_first == length_of_last)):
        break
    if (curr_dir == "right"):
        grid[curr_row].append(curr_num)
        if (len(grid[curr_row]) > len(grid[curr_row - 1])):
            curr_dir = change_dir(curr_dir)
    elif (curr_dir == "up"):
        curr_row -= 1
        if (curr_row >= 0):
            grid[curr_row].append(curr_num)
        else:
            newRow = []
            newRow.append(curr_num)
            grid.insert(0, newRow)
            curr_dir = change_dir(curr_dir)
            curr_row = 0
    elif (curr_dir == "left"):
        grid[curr_row].insert(0, curr_num)
        if (len(grid[curr_row]) > len(grid[curr_row + 1])):
            curr_dir = change_dir(curr_dir)
    else:
        curr_row += 1
        if (curr_row < len(grid)):
            grid[curr_row].insert(0, curr_num)
        else:
            newRow = []
            newRow.append(curr_num)
            grid.append(newRow)
            curr_dir = change_dir(curr_dir)
            
    curr_num += 1

x1 = x2 = y1 = y2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (grid[i][j] == 1):
            x1 = j
            y1 = i
        if (grid[i][j] == int(num)):
            x2 = j
            y2 = i

print(abs(x1 - x2) + abs(y1 - y2))