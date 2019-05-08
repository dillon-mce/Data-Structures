"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    self.length += 1
    

  def remove_from_head(self):
    value = self.head.value
    self.delete(self.head)
    return value
    

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      new_node = ListNode(value)
      self.tail = new_node
      self.head = new_node
    self.length += 1

  def remove_from_tail(self):
    value = self.tail.value
    self.delete(self.tail)
    return value

  def move_to_front(self, node):
    self.delete(node)
    self.add_to_head(node.value)
    

  def move_to_end(self, node):
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    if node is self.tail and node is self.head:
      self.head = None
      self.tail = None
    elif node is self.head:
      self.head = node.next
    elif node is self.tail:
      self.tail = node.prev
    
    node.delete()
    self.length -= 1 if self.length > 0 else 0

  def get_value(self, value):
    current = self.head
    while current:
      if current.value == value:
        return current
      current = current.next
    
  def get_max(self):
    if not self.head or not self.tail:
      return None
    current = self.head
    max_value = current.value
    while current:
      max_value = current.value if current.value > max_value else max_value
      current = current.next
    return max_value


class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.list = DoublyLinkedList()
    self.dict = {}

  def __str__(self):
    return f'{self.dict}'
  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    key_node = self.list.get_value(key)
    if key_node:
      self.list.move_to_front(key_node)
      return self.dict[key]
    else:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    key_node = self.list.get_value(key)
    if key_node:
      self.list.move_to_front(key_node)
    else:
      self.list.add_to_head(key)
      if self.list.length > self.limit:
        self._remove_last()
    
    self.dict[key] = value

  def _remove_last(self):
    key = self.list.tail.value
    self.list.remove_from_tail()
    del self.dict[key]