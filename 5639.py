import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def construct_bst_from_preorder(preorder):
    if not preorder:
        return None

    root_value = preorder[0]
    root = [root_value, None, None]
    stack = [root]

    for value in preorder[1:]:
        node = [value, None, None]
        if value < stack[-1][0]:
            stack[-1][1] = node
        else:
            parent = None
            while stack and stack[-1][0] < value:
                parent = stack.pop()
            parent[2] = node
        stack.append(node)
    
    return root

def post_order(node):
    if node is None:
        return []

    result = []
    result.extend(post_order(node[1]))
    result.extend(post_order(node[2]))
    result.append(node[0])
    
    return result

li = []
while True:
    try:
        k = int(input())
        li.append(k)
    except:
        break

tree = construct_bst_from_preorder(li)

ans = post_order(tree)

for a in ans:
    print(a)