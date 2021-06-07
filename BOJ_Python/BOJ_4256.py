# 트리
def postorder(inorder, root):
    for i in range(len(inorder)):
        if inorder[i] == preorder[root]:
            postorder(inorder[:i], root+1)
            postorder(inorder[i+1:], root+i+1)
            print(inorder[i], end=" ")
            break

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(inorder, 0)
    print()