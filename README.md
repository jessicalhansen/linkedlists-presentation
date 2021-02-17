# linked-lists
Alex
```python
# Taken from https://realpython.com/linked-lists-python/
# Building our list's classes
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  #Create the list with some starting data
  def __init__(self nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next
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
        if node.data == target_node_data
          previous_node.next = node.next
          return
        previous_node = node






```
Matt
#### At least two examples of the assigned topic:
 1. Trains (Singly) - Train cars are linked in a specific order so that they may be loaded, unloaded, transferred, dropped off, and picked up in the most efficient manner possible. The train travels only forward and the last train car has no connections.
 <img src="https://www.atnyla.com/library/images-tutorials/Linkedlist-Slide4.PNG" style="height: 100px" />
 2. Spotify (Doubly) - Each song points to both the previous and next songs.
 <img src="https://www.androidpolice.com/wp-content/uploads/2019/03/spotify-now-playing-newer.png"  style="height: 100px"/>
#### Identify situations where you use a linked list instead of an array.
 1. When you need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
 2. Not sure how many items will be in the list
 3. If you do not need random access to any elements
 4. If you'll want to be able to insert items in the middle of the list

Vishwa
* One paragraph explaining the concept behind the topic assigned to your group. Include this in your README.md.
* One paragraph outlining different types of questions that can be asked/solved using the given topic.


Jessica
* Explain how a node stores data.


##### Resources
* This video is a part of HackerRank's Cracking The Coding Interview Tutorial with Gayle Laakmann McDowell
  * https://www.youtube.com/watch?v=njTh_OwMljA&feature=emb_logo
* Stackoverflow for when to use a linked list over an array
  * https://stackoverflow.com/questions/393556/when-to-use-a-linked-list-over-an-array-array-list
