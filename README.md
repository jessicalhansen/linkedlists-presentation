# Linked List
Matt
#### At least two examples of the assigned topic:
 1. Trains (Singly) - Train cars are linked in a specific order so that they may be loaded, unloaded, transferred, dropped off, and picked up in the most efficient manner possible. The train travels only forward and the last train car has no connections.
 <p align="center">
  <img src="https://miro.medium.com/max/2280/1*7iuBvBXeST5XFo4HYxrEnw.jpeg" height="400">
 </p>
 2. Spotify (Doubly) - Each song points to both the previous and next songs.
 <p align="center">
  <img src="https://www.androidpolice.com/wp-content/uploads/2019/03/spotify-now-playing-newer.png" height="400">
 </p>
 
#### Identify situations where you use a linked list instead of an array.
 1. When you need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
 2. Not sure how many items will be in the list
 3. If you do not need random access to any elements
 4. If you'll want to be able to insert items in the middle of the list

Vishwa
* One paragraph explaining the concept behind the topic assigned to your group. Include this in your README.md.
* One paragraph outlining different types of questions that can be asked/solved using the given topic.


## How a node stores data:

Elements in a linked list are stored in key components called nodes. A node is a unit that contains two sub-elements at the same time:
* a ***data*** property, which stores a value.
* a ***pointer*** property, which points to and links the next node. 
Linked lists start with a **head node** and grow by using pointers to other nodes in different parts of the computer's memory. Nodes allow the linked list to expand fairly easily, but requires more space than an array due to storing both the data and the pointers. 

There is no index value in linked lists, so in order to access data from a particular node you must start with the head node and move through the list sequentially. This can result in a lengthy timeline to access data in a linked list because the data set isn't read in one continuous chunk. 

***Doubly Linked Lists*** are exactly the same as **singly linked lists** and first point to the next node in one direction, but also points back to the previous node. 



##### Resources
* This video is a part of HackerRank's Cracking The Coding Interview Tutorial with Gayle Laakmann McDowell
  * https://www.youtube.com/watch?v=njTh_OwMljA&feature=emb_logo
* Stackoverflow for when to use a linked list over an array
  * https://stackoverflow.com/questions/393556/when-to-use-a-linked-list-over-an-array-array-list
