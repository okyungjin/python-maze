class Stack:
    def __init__(self):
        self.num = []

    def push(self, x):
        self.num.append(x)

    def pop(self):
        try:
            return self.num.pop()
        except IndexError:
            print("Empty stack")

    def __len__(self):
        return len(self.num)

    def isEmpty(self):
        return self.__len__() == 0

    def peek(self):
        try:
            return self.num[-1]
        except IndexError:
            return -1

    #스택의 내용물 전부 출력
    def dump(self):
        if self.isEmpty():
            print("empty")
        else:
            return self.num

    #스택에 있는지 확인
    def find(self, val):
        for i in range(self.__len__() - 1,-1,-1):
            if self.num[i] == val:
                return i
        return -1

data = []

import os
import pprint as pp
import copy
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'maze1.txt'), 'r')

#with open('maze1.txt') as f:
size = f.readline()[:-1]
while True:
    line = f.readline()
    if not line: break
    if '\n' in line:
        if '\n' != line:
            data.append(line[:-1])
    else:
        data.append(line)
    
# 불러온 파일의 내용을 우선 data 변수에 담는다.
width=len(data[0])
height=len(data)
print(width, height)

def make_maze(maze, width, height):
    newmaze = []
    for i in range(height):
        list = []
        for j in range(width):
            if maze[i][j] == " ":
                item_mod = '0' # 움직일 수 있음
            else:
                item_mod = '1' # 벽
            list.append(item_mod)
        newmaze.append(list)

    return newmaze

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isValidPos(x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    # else:
    #     return maps[y][x] == '0' or maps[y][x] == 'x'

# global stack

def DFS(x, y):
    global maps
    
    if x < 1 or y < 1 or x >= width-1 or y >= height-1:
        return False

    # print('push', x, y)
    # if x % 2 == 0 and y % 2 == 0:
        # print('pop', x % 2, y % 2)


    if x == width - 2 and y == height - 2:
        print('=====================YE=====================')
        return True
    
    # stack.push((x, y))
    # print('push', x, y)

    if not maps[x][y] == '0':
        return False

    maps[x][y] = 'V'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # if nx >= 1 and ny >= 1 and nx <= width-1 and ny <= height-1 and maps[nx][ny] == '0':    
        DFS(nx, ny)
        
        # print('pop', nx, ny)
    maps[x][y] = '0'
    return True

        


        # if nx % 2 == 0 and ny % 2 == 0:
        #     print('push', x % 2, y % 2)
    # maps[x][y] = '0'    

    # maps[x][y] = '0'

    # while not stack.isEmpty():
    #     here = stack.pop()
    #     print("pop ",here)
    #     (x, y) = here
    #     print(maps[x][y])
        
            # print(stack.dump())
            # return True
        # else:
        #     maps[y][x] = '.'
            
        #     if isValidPos(x, y - 1):
                
        #         stack.push((x, y - 1))
        #         print("push",x,y-1)
        #     if isValidPos(x, y + 1):
        #         stack.push((x, y + 1))
        #         print("push",x,y+1)
        #     if isValidPos(x - 1, y):
        #         stack.push((x - 1, y))
        #         print("push",x-1,y)
        #     if isValidPos(x + 1, y):
        #         stack.push((x + 1, y))
        #         print("push",x+1,y)
            # print(stack.dump())


    # return False

for d in data:
    print(d)

newmaze = make_maze(data, width, height)

for maze in newmaze:
    print(maze)

maps = newmaze

# stack = Stack()
print('길 탐색 시작')

# result = DFS(1, 1)

# if result:
#     print(' --> 미로탐색 성공')
# else:
#     print(' --> 미로탐색 실패')


# . 지나옴
count = 0
graph = {
	1: [2,3,4],
	2:[5],
	3:[5],
	4:[],
	5:[6,7],
	6:[],
	7:[3],
}
def stack_dfs(start_vertex):
	visited = []
	stack = [start_vertex]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
				visited.append(vertex)
				for item in graph[vertex]:
					stack.append(item)
	return visited

print(stack_dfs(1))