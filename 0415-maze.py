import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'maze1.txt'), 'r')

n, m = map(int, f.readline().split())
print(n, m)

origin_map = []
for _ in range(m * 2 + 1):
    origin_map.append(list(str(f.readline().rstrip())))

# ' ' : 방문 가능
# 그 외 : 벽
# 'O' : 방문함

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def dfs(x, y):
    global count
    print(x, y)
    print(n, m)
    if x < 1 or x > 2 * n or y < 1 or y > 2 * m:
        return False
    
    if x == n * 2 - 2 and y == m * 2 - 2:
        count += 1
        return True
    
    if origin_map[x][y] == ' ':
        origin_map[x][y] = 'O'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

dfs(1, 1)

for op in origin_map:
    print(op)

print(count)