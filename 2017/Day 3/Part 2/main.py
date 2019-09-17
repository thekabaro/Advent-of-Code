grid = [[1, 1]]
curr_dir = "up"
curr_row = 0
curr_num = 0
curr_ind = 0

def change_dir(direction):
    if (direction == "right"):
        return "up"
    elif (direction == "up"):
        return "left"
    elif (direction == "left"):
        return "down"
    else:
        return "right"

test_num = 0
while (True):
    if (curr_dir == "right"):
        #####
        curr_num += grid[curr_row][len(grid[curr_row]) - 1]
        curr_num += grid[curr_row - 1][curr_ind - 1]
        if (len(grid[curr_row - 1]) - curr_ind > 0):
            curr_num += grid[curr_row - 1][curr_ind]
        if (len(grid[curr_row - 1]) - curr_ind > 1):
            curr_num += grid[curr_row - 1][curr_ind + 1]
        curr_ind += 1
        #####
        grid[curr_row].append(curr_num)
        if (len(grid[curr_row]) > len(grid[curr_row - 1])):
            curr_dir = change_dir(curr_dir)
    elif (curr_dir == "up"):
        curr_row -= 1
        curr_num += grid[curr_row + 1][len(grid[curr_row + 1]) - 1]
        curr_num += grid[curr_row + 1][len(grid[curr_row + 1]) - 2]
        if (curr_row >= 0):
            curr_num += grid[curr_row][len(grid[curr_row]) - 1]
            if (curr_row > 0):
                curr_num += grid[curr_row - 1][len(grid[curr_row - 1]) - 1]
            grid[curr_row].append(curr_num)
        else:
            newRow = []
            newRow.append(curr_num)
            grid.insert(0, newRow)
            curr_dir = change_dir(curr_dir)
            curr_row = 0
            curr_ind = len(grid[curr_row + 1]) - 1
    elif (curr_dir == "left"):
        curr_num += grid[curr_row][0]
        curr_num += grid[curr_row + 1][curr_ind]
        if (curr_ind > 0):
            curr_num += grid[curr_row + 1][curr_ind - 1]
        if (curr_ind > 1):
            curr_num += grid[curr_row + 1][curr_ind - 2]
        curr_ind -= 1
        grid[curr_row].insert(0, curr_num)
        if (len(grid[curr_row]) > len(grid[curr_row + 1])):
            curr_dir = change_dir(curr_dir)
    else:
        curr_row += 1
        curr_num += grid[curr_row - 1][0]
        curr_num += grid[curr_row - 1][1]
        if (len(grid) - curr_row > 0):
            curr_num += grid[curr_row][0]
        if (len(grid) - curr_row > 1):
            curr_num += grid[curr_row + 1][0]
        if (curr_row < len(grid)):
            grid[curr_row].insert(0, curr_num)
        else:
            newRow = []
            newRow.append(curr_num)
            grid.append(newRow)
            curr_dir = change_dir(curr_dir)
            curr_ind = 1
    if (curr_num > 265149):
        print(curr_num)
        break
    curr_num = 0