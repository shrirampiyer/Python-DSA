class binarytree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None 

def bt(arr, index, n):
  root = None 
  if index <n :
    root = binarytree(arr[index])
    root.left = bt(arr, 2*index +1, n)
    root.right = bt(arr, 2*index + 2, n)
  return root

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root = bt(arr, 0, n)