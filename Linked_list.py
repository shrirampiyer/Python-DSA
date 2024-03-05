class LinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None

node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)

node1.next = node2
node2.next = node3
node3.next = node4
nodes = [node1, node2, node3, node4]
def Viewlist():
  current_node = node1
  while current_node is not None:
    print(current_node.data, "->", end=" ")
    if current_node.next is not None:
      print(current_node.next.data)
    else: 
      print('Null')
    current_node = current_node.next

Viewlist()