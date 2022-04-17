import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'maze1.txt'), 'r')

def read_maze(n, m, f):
    maze = []
    for i in range(cols):
        row = list(f.readline().rstrip())
        maze.append(row)
    return maze


def print_maze(maze):
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'V': # VISITED
                print('O', end = '')
            elif maze[i][j] == 'B': # BACKTRACKED
                print(' ', end = '')
            else:
                print(maze[i][j], end = '')
        print()


n, m = map(int, f.readline().split())
rows = 2 * n + 1
cols = 2 * m + 1

maze = read_maze(n, m, f)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = []
cur_x = 1
cur_y = 1

while True:
    maze[cur_x][cur_y] = 'V';
    if cur_x == rows - 2 and cur_y == cols - 2:
        print_maze(maze)
        print('Found the path')
        break

    forwarded = False
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx >= 1 and nx < rows and ny >= 1 and ny < cols and maze[nx][ny] == ' ':
            stack.append((cur_x, cur_y))
            print('push', (cur_x, cur_y))
            cur_x = nx
            cur_y = ny
            forwarded = True
            break
    
    if not forwarded:
        maze[cur_x][cur_y] = 'B'
        if not stack:
            print('No path exist')
            break
        pos = stack.pop()
        print('pop', pos)
        cur_x = pos[0]
        cur_y = pos[1]