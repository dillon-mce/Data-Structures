Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

**O(1)** No matter how long the queue is, enqueueing a new item will take the same amount of steps.

2. What is the runtime complexity of `dequeue`?

**O(1)** No matter how long the queue is, dequeueing a new item will take the same amount of steps.

3. What is the runtime complexity of `len`?

**O(1)** No matter how long the queue is, looking up the length will take the same amount of steps. (At the cost of one extra step in both the enqueue and dequeue methods.)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

Approximately **O(log(n))**, assuming the inserted data is relatively balanced. 

2. What is the runtime complexity of `contains`?

Approximately **O(log(n))**, assuming the data is relatively balanced. 

3. What is the runtime complexity of `get_max`?

Approximately **O(log(n))**, assuming the data is relatively balanced. 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

**O(1)** Inserting a new ListNode after another one will always take the same amount of steps. (Give or take 1)

2. What is the runtime complexity of `ListNode.insert_before`?

**O(1)** Inserting a new ListNode after another one will always take the same amount of steps. (Give or take 1)

3. What is the runtime complexity of `ListNode.delete`?

**O(1)** Deleting a ListNode will always take the same amount of steps. (Give or take 2)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

**O(1)** Adding a new ListNode at the head of a DoublyLinkedList will always take the same amount of steps. (Give or take a couple)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

**O(1)** Removing the ListNode at the head of a DoublyLinkedList will always take the same amount of steps. (Give or take a couple)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

**O(1)** Adding a new ListNode at the tail of a DoublyLinkedList will always take the same amount of steps. (Give or take a couple)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

**O(1)** Removing the ListNode at the tail of a DoublyLinkedList will always take the same amount of steps. (Give or take a couple)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

**O(1)** The complexity of `DoublyLinkedList.delete()` and `DoublyLinkedList.add_to_head()` are both O(1), and O(1) + O(1) = O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

**O(1)** The complexity of `DoublyLinkedList.delete()` and `DoublyLinkedList.add_to_tail()` are both O(1), and O(1) + O(1) = O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

**O(1)** Deleting a node from a DoublyLinkedList will always take roughly the same amount of steps.

- Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    I am not particularly familiar with Array.splice() in JS, but I would assume it is O(n), which is much worse than O(1).