class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def is_mirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return left.value == right.value and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def isSymmetric(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)

root = build_tree([1, 2, 2, 3, 4, 4, 3])
print(isSymmetric(root))
