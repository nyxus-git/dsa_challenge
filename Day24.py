class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Lowest Common Ancestor
def LCA(root, p, q):
    if not root or root == p or root == q:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left and right:
        return root

    return left if left else right
#build tree
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root
#find node
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    
    left = find_node(root.left, val)
    if left:
        return left
    
    return find_node(root.right, val)

root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = find_node(root, 5)
q = find_node(root, 4)
result = LCA(root, p, q)
print(result.val)
