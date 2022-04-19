import numpy as np

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

#미로 생성
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

#이동가능 여부
def isValidPos(x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

#미로 길 탐색 1번
def DFS(s):
    stack = Stack()
    stack.push((1, 1))
    print("push( 1 , 1 )")
    while not stack.isEmpty():
        here = stack.peek()
        (x, y) = here
        if (map[y][x] == 'x'):
            map[y][x] = '.'
            #1번 길은 무조건 출력
            print("경로 1")
            for i in range(height):
                for j in range(width):
                    if map[i][j] == '.':
                        print('o', end='')
                    else:
                        print(data[i][j], end='')
                print()
            #1번 길을 저장한다. map3에 1번 길 저장 , map은 처음 make_maze의 결과를 저장했던 map2에 저장
            #.의 위치가 중요하고 어느 쪽을 갔다 돌아왔는지는 출력시의 결과적 루트와는 관련이 없으므로 0으로 변경해줌
            for i in range(height):
                for j in range(width):
                    map3[i][j] = map[i][j]
                    if map3[i][j] == '2':
                        map3[i][j] = '0'
                    map[i][j] = map2[i][j]
            return map3

        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))
                print("push(",x,',',y-1,')')
            elif isValidPos(x, y + 1):
                stack.push((x, y + 1))
                print("push(",x,',',y+1,')')
            elif isValidPos(x - 1, y):
                stack.push((x - 1, y))
                print("push(",x-1,',',y,')')
            elif isValidPos(x + 1, y):
                stack.push((x + 1, y))
                print("push(",x+1,',',y,')')
            #그 길이 아니면 2번으로 바꾸고 pop한다
            else:
                map[y][x] = '2'
                here = stack.pop()
                print("pop ", here)
    return False

#미로 길 탐색 2번
def DFS2(s):
    stack = Stack()
    stack.push((1, 1))
    while not stack.isEmpty():
        here = stack.peek()
        (x, y) = here
        if (map[y][x] == 'x'):
            map[y][x] = '.'
            #DFS 함수와 같이 지나왔는데 아니었던 점을 0으로 변경
            for i in range(height):
                for j in range(width):
                    if map[i][j] == '2':
                        map[i][j] = '0'
            return map
        #탐색방향을 바꾸었다. 상하좌우에서 상좌우하 로 바꾸어 아래로 가는걸 가장 마지막에 탐색하도록 했다.
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))
            elif isValidPos(x - 1, y):
                stack.push((x - 1, y))
            elif isValidPos(x + 1, y):
                stack.push((x + 1, y))
            elif isValidPos(x, y + 1):
                stack.push((x, y + 1))
            else:
                map[y][x] = '2'
                here = stack.pop()
    return False

map = make_maze(data, width, height)
map2 = make_maze(data, width, height)
map3 = make_maze(data, width, height)

DFS(map)
DFS2(map)

#2번째 길이 있을 경우
if not np.array_equal(map, map3):
    print("경로 2")
    for i in range(height):
        for j in range(width):
            if map[i][j] == '.':
                print('o', end='')
            else:
                print(data[i][j], end='')
        print()
    print("길은 총 2개")
else:
    print("길은 총 1개")