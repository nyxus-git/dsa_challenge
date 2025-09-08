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
  
def inOrderTraversal(node, result_list):
  if node is None:
    return
  inOrderTraversal(node.left, result_list)

  result_list.append(node.value)

  inOrderTraversal(node.right, result_list)

def isValidBST(root):
  result_list = []

  inOrderTraversal(root, result_list)

  for i in range(1, len(result_list)):
    if result_list[i-1] >= result_list[i]:
      return False

  return True

root = build_tree([2,1,3])
print(isValidBST(root))
