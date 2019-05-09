class Heap:
  def __init__(self, comparator = (lambda x, y: x > y)):
    self.storage = []
    self.comparator = comparator

  def __str__(self):
    return self.storage.__str__()

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    value = self.get_priority()
    if len(self.storage) > 1:
      new_value = self.storage.pop()
      self.storage[0] = new_value
      self._sift_down(0)
    else:
      self.storage.pop()

    return value

  def get_priority(self):
    try:
      return self.storage[0]
    except:
      return None

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    parent_index = ((index - 1) // 2)
    parent = self.storage[parent_index]
    if self.comparator(self.storage[index], parent):
      self._swap(index, parent_index)
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    child_1_index = 2*index + 1
    child_2_index = 2*index + 2
    if child_1_index >= len(self.storage):
      return
    child_1 = self.storage[child_1_index]
    
    if child_2_index >= len(self.storage):
      if self.comparator(child_1, self.storage[index]):
        self._swap(index, child_1_index)
        self._sift_down(child_1_index)
      return
    child_2 = self.storage[child_2_index]

    if self.comparator(child_1, self.storage[index]) and self.comparator(child_1, child_2):
      self._swap(index, child_1_index)
      self._sift_down(child_1_index)
    elif self.comparator(child_2, self.storage[index]):
      self._swap(index, child_2_index)
      self._sift_down(child_2_index)

  def _swap(self, a, b):
    (self.storage[a], self.storage[b]) = (self.storage[b], self.storage[a])
