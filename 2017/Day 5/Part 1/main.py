maze = []

myFile = open("../input.txt", "r")
for line in myFile:
    line = line.strip()
    maze.append(int(line))

curr_pos = 0
old_pos = 0
num_steps = 0

while (True):
    old_pos = curr_pos
    curr_pos += maze[curr_pos]
    maze[old_pos] += 1
    num_steps += 1
    if (curr_pos < 0 or curr_pos >= len(maze)):
        break

print(num_steps)