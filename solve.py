from collections import deque
def dfs(dfs_start):
    dfs_dq.append(dfs_start)
    while dfs_dq:
        dfs_chk.append(dfs_dq.pop())
        for i in mapp[dfs_start]:
            if i not in dfs_chk:
                dfs(i)
    return dfs_chk

def bfs(bfs_start):
    bfs_dq.appendleft(bfs_start)
    bfs_chk.append(bfs_start)
    while bfs_dq:
        now = bfs_dq.popleft()
        for next in mapp[now]:
            if next not in bfs_chk:
                bfs_chk.append(next)
                bfs_dq.append(next)
    return bfs_chk

n,m,start=map(int, input().split())
mapp=[[] for _ in range(n+1)]
dfs_chk = []
bfs_chk = []
dfs_dq = deque()
bfs_dq = deque()
for _ in range(m):
    x,y=map(int, input().split())
    mapp[x].append(y)
    mapp[x].sort()
    mapp[y].append(x)
    mapp[y].sort()
print(*dfs(start))
print(*bfs(start))