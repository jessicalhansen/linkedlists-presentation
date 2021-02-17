class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  #Create the list with some starting data
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next
  #Displays list content when list is printed
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)
  #Iterate through the list
  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next
  #Add a new node to the start of the list
  def add_first(self, node):
    node.next = self.head
    self.head = node
  #Add a new node to the end of the list
  def add_last(self, node):
    if self.head is None:
      self.head = node
      return
    for current_node in self:
      pass
    current_node.next = node
  #Add a new node after a seleccted node
  def add_after(self, target_node_data, new_node):
    if self.head is None:
      raise Exception("List is empty")
    for node in self:
      if node.data == target_node_data:
        new_node.next = node.next
        node.next = new_node
        return
  #Remove a node
  def remove_node(self, target_node_data):
    if self.head is None:
      raise Exception("List is empty")
    if self.head.data == target_node_data:
      self.head = self.head.next
      return
    previous_node = self.head
    for node in self:
      if node.data == target_node_data:
        previous_node.next = node.next
        return
      previous_node = node

llist = LinkedList(["b", "c", "d", "e"])
print(llist)
#llist.add_first(Node("a"))
#print(llist)
#llist.add_last(Node("g"))
#print(llist)
#llist.add_after("e", Node("f"))
#print(llist)
#llist.remove_node("e")
#print(llist)
