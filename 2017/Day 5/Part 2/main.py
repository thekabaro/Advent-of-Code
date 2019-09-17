maze = []

myFile = open("../input.txt", "r")
for line in myFile:
    line = line.strip()
    maze.append(int(line))

curr_pos = 0
old_pos = 0
num_steps = 0
three_or_more = False

while (True):
    if (maze[curr_pos] >= 3):
        three_or_more = True
    else:
        three_or_more = False
    old_pos = curr_pos
    curr_pos += maze[curr_pos]
    if (three_or_more):
        maze[old_pos] -= 1
    else:
        maze[old_pos] += 1
    num_steps += 1
    if (curr_pos < 0 or curr_pos >= len(maze)):
        break

print(num_steps)