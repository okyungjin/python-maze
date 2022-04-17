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

with open('maze1.txt') as f:
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

def make_maze(maze, width, height):
    newmaze = []
    for i in range(height):
        list = []
        for j in range(width):
            if data[i][j] == " ":
                item_mod = '0'
            else:
                item_mod = '1'
            list.append(item_mod)
        newmaze.append(list)

    newmaze[-2][-2] = "x"
    return newmaze

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS(map):
    stack = Stack()
    stack.push((1, 1))
    print("push 1 1")
    while not stack.isEmpty():
        here = stack.peek()
        (x, y) = here
        if (map[y][x] == 'x'):
            stack.push((x, y))
            map[y][x] = '.'
            return map
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))
                print("push",x,y-1)
            elif isValidPos(x, y + 1):
                stack.push((x, y + 1))
                print("push",x,y+1)
            elif isValidPos(x - 1, y):
                stack.push((x - 1, y))
                print("push",x-1,y)
            elif isValidPos(x + 1, y):
                stack.push((x + 1, y))
                print("push",x+1,y)
            else:
                map[y][x] = '2'
                here = stack.pop()
                print("pop ", here)
    return False

newmaze = make_maze(data, width, height)
map = newmaze
result = DFS(map)
if result:
    print(' --> 미로탐색 성공')
    for i in range(height):
        for j in range(width):
            if map[i][j] == '.':
                print('o', end='')
            else:
                print(data[i][j], end='')
        print()
else:
    print(' --> 미로탐색 실패')