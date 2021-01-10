# 트리 순회
class Node:
    def __init__(self, root, lchild, rchild):
        self.root = root
        self.lchild = lchild
        self.rchild = rchild
    
def preorder(node):
    print(node.root, end="")
    if node.lchild != ".":
        preorder(data[node.lchild])
    if node.rchild != ".":
        preorder(data[node.rchild])

def inorder(node):
    if node.lchild != ".":
        inorder(data[node.lchild])
    print(node.root, end="")
    if node.rchild != ".":
        inorder(data[node.rchild])

def postorder(node):
    if node.lchild != ".":
        postorder(data[node.lchild])
    if node.rchild != ".":
        postorder(data[node.rchild])
    print(node.root, end="")

N = int(input())
data = {}
for _ in range(N):
    root, lchild, rchild = map(str, input().split())
    data[root] = Node(root, lchild, rchild)
preorder(data["A"])
print()
inorder(data["A"])
print()
postorder(data["A"])

'''
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
'''