# 요세푸스 문제
N, K = map(int, input().split())
lst = list(i for i in range(1, N+1))
lst2 = list()
K, K2 = K-1, K-1
for i in range(N):
    lst2.append(str(lst.pop(K)))
    if len(lst) == 0:
        break
    K = (K+K2)%len(lst)
print('<'+', '.join(lst2)+'>')