# A+B - 8
T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    # print("Case #"+str(i)+": "+str(A)+" + "+str(B)+" = "+str(A+B))
    print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A+B))