# 트리 순회
def preorder(V):
    if V == ".":
        return
    print(V, end="")
    preorder(data[ord(V)-65][0])
    preorder(data[ord(V)-65][1])

def inorder(V):
    if V == ".":
        return
    inorder(data[ord(V)-65][0])
    print(V, end="")
    inorder(data[ord(V)-65][1])

def postorder(V):
    if V == ".":
        return
    postorder(data[ord(V)-65][0])
    postorder(data[ord(V)-65][1])
    print(V, end="")

N = int(input())
data = [[] for _ in range(26)]
for _ in range(N):
    root, lchild, rchild = map(str, input().split())
    data[ord(root)-65].append(lchild)
    data[ord(root)-65].append(rchild)
preorder("A")
print()
inorder("A")
print()
postorder("A")