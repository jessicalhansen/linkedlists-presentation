# Linked List

<p align="center">
 <img src="https://pbs.twimg.com/media/ETyy1VwX0AYPcV4.jpg" height="400">
</p>

## Introduction

In Computer Science, a linked list is a linear data structure where each element is a separate object.
Linked list elements are not stored at a contiguous location, meaning they are not adjacent to each other; the elements are linked using pointers. The key component of a linked list is a **node**. Each node of a list is made up of two items:
* A [Data](https://en.wikipedia.org/wiki/Data_(computing)) property that stores a value.
* A [Reference](https://en.wikipedia.org/wiki/Reference_(computer_science)) (in other words, a *link*) to the **next** node. This property can also be called the **Next** property, sometimes called a "pointer" that points to the next item in the list. <br> 

The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference. In the case of linked lists, the only exception to this rule is the very last node. It doesn’t need a pointer, so it’s known as a “null next node” (or more simply, “the tail”). <br>
> ***Shown below is a Linked List Representaion***: <br>

<p align="center">
 <img src="https://www.educative.io/api/edpresso/shot/5077575695073280/image/5192456339456000" height="300">
</p> 
<br>

**There are two types of Linked lists**:
* Singly linked list -
A singly linked list is a set of nodes where each node has two fields ‘data’ and ‘link’. The ‘data’ field stores actual piece of information and ‘link’ field is used to point to next node. Basically ‘link’ field is nothing but address only. <br>
<p align="center">
 <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png" height="300">
</p>
<br>

* Doubly linked list -
 A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list. <br>
 <p align="center">
 <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png" height="300">
</p>


### How a node stores data:

Linked lists start with a **head node** and grow by using pointers to other nodes in different parts of the computer's memory. Nodes allow the linked list to expand fairly easily, but requires more space than an array due to storing both the data and the pointers. There is no index value in linked lists, so in order to access data from a particular node you must start with the head node and move through the list sequentially. This can result in a lengthy timeline to access data in a linked list because the data set isn't read in one continuous chunk. 

***Doubly Linked Lists*** are exactly the same as **singly linked lists** and first point to the next node in one direction, but also another pointer that links back to the previous node. 


Data Structure	Access	Search	Insertion	Deletion
*    Array	      O(1)	   O(N)	  O(N)	    O(N)
* Linked list	   O(N)	   O(N)	  O(1)	    O(1)

#### Two examples of the assigned topic:
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

## Interview coming up?

Data structures are a vital part of any programming interview. Often times, Linked lists are a common topic that comes up in the technical interview process. Reviewing and practicing these [Linked List problems](https://www.geeksforgeeks.org/top-20-linked-list-interview-question/) will give you the confidence required to ace your interview while also making you a better programmer. <br>
Some highlights include:
1. ***Linked List Implementaion***
<details>
 <summary>Solution here</summary>
(https://www.techiedelight.com/linked-list-implementation-part-2/)
</details>

2. ***Rotate a Linked List***
<details>
 <summary>Solution here</summary>
(https://www.geeksforgeeks.org/rotate-a-linked-list/)
</details>

3. ***Write a function to delete a Linked list***
<details>
 <summary>Solution here</summary>
(https://www.geeksforgeeks.org/write-a-function-to-delete-a-linked-list/)
</details>

Often, these concepts will appear as whiteboarding problems, so you won’t need to know how to code a linked list - just how to draw it and explain it conceptually. [This tool](https://visualgo.net/bn/list?slide=1) can help you visualize adding, removing, and searching for values in a linked list.

If you're curious to learn more, please visit [All Articles on Linked Lists](https://www.geeksforgeeks.org/data-structures/linked-list/).

**Congrats! You're One Step Closer to Preparing For Your Coding Interview**

### Resources
* This video is a part of HackerRank's Cracking The Coding Interview Tutorial with Gayle Laakmann McDowell
  * https://www.youtube.com/watch?v=njTh_OwMljA&feature=emb_logo
* Stackoverflow for when to use a linked list over an array
  * https://stackoverflow.com/questions/393556/when-to-use-a-linked-list-over-an-array-array-list
