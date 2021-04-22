# 이모티콘
from collections import deque
def is_in(n_imo):
    if 0 <= n_imo <= 1000:
        return True
    return False

def bfs(n):
    visited[n][0] = True
    deq = deque([(n, 0, 0)])
    while deq:
        imoticon, cnt, clipboard = deq.popleft()
        # print(imoticon, clipboard)
        if imoticon == S:
            print(cnt)
            return
        for i in range(3):
            if i == 0:
                if imoticon == 0:
                    continue
                n_clipboard = imoticon
                n_imo = imoticon
            elif i == 1:
                if clipboard == 0:
                    continue
                n_clipboard = clipboard
                n_imo = imoticon + clipboard
            else:
                if imoticon == 0:
                    continue
                n_clipboard = clipboard
                n_imo = imoticon-1
            if not is_in(n_imo):
                continue
            if visited[n_imo][n_clipboard]:
                continue
            visited[n_imo][n_clipboard] = True
            deq.append((n_imo, cnt+1, n_clipboard))

S = int(input())
visited = [[False]*1001 for _ in range(1001)]
bfs(1)