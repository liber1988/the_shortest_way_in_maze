from collections import deque

def print_path(field,path):
    field=[[field[i]] for i in range(len(field))]
    for i ,j in enumerate(field):
        res = []

        for el in j:
            res=[[x] for x in el]
        field[i]=res
    for i in path:
        field[i[0]][i[1]]=['X']

    for i,j in enumerate(field):
        row=""
        for x in j:
            a=''.join(x)
            row=row+a
        print(row)



def bfs(field, s, t):
    n = len(field)
    m = len(field[0])
    INF = 10 ** 9
    delta = [(1, 0), (-1, 0),(0, -1), (0, 1)]
    d = [[INF] * m for _ in range(n)]
    p = [[None] * m for _ in range(n)]
    used = [[False] * m for _ in range(n)]
    queue = deque()
    d[s[0]][s[1]] = 0
    used[s[0]][s[1]] = True
    queue.append(s)
    while len(queue) != 0:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 < nx < n and 0 < ny < m and not used[nx][ny] and field[nx][ny] != '#':
                d[nx][ny] = d[x][y] + 1
                p[nx][ny]=(x,y)
                used[nx][ny] = True
                queue.append((nx, ny))

    print(d[t[0]][t[1]])

    cur=t
    path=[]
    while cur is not None:
        path.append(cur)
        cur=p[cur[0]][cur[1]]

    path.reverse()

    print_path(field,path[1:-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fin = open('path.txt', 'r')
    field = fin.readlines()
    n = len(field)
    m = len(field[0]) - 1
    s = None
    t = None
    for i in range(n):
        field[i] = field[i].strip()
        if field[i].find('S') != -1:
            s = (i, field[i].find('S'))
        if field[i].find('T') != -1:
            t = (i, field[i].find('T'))





bfs(field, s, t)
# Se PyCharm help at https://www.jetbrains.com/help/pycharm/
