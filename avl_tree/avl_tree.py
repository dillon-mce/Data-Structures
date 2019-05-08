"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = 0 if self.node else -1
    self.balance = 0

  def __str__(self):
    return f'{self.node.key}, right: {self.node.right}, left: {self.node.left}'

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]")
      if self.node.left != None: 
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    if self.node.right and self.node.left:
      self.node.right.update_height()
      self.node.left.update_height()
      if self.node.left.height >= self.node.right.height:
        self.height = 1 + self.node.left.height
      else:
        self.height = 1 + self.node.right.height
    elif self.node.right:
      self.node.right.update_height()
      self.height = 1 + self.node.right.height
    elif self.node.left:
      self.node.left.update_height()
      self.height = 1 + self.node.left.height
    else:
      self.height = 0
  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    if self.node.right and self.node.left:
      self.node.right.update_balance()
      self.node.left.update_balance()
      self.balance = self.node.left.height - self.node.right.height
    elif self.node.left:
      self.node.left.update_balance()
      self.balance = self.node.left.height
    elif self.node.right:
      self.node.right.update_balance()
      self.balance = -self.node.right.height
    else:
      self.balance = 0

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def _left_rotate(self):
    old_self = self.node
    old_left = self.node.right.node.left
    self.node = self.node.right.node
    old_self.right = old_left
    self.node.left = AVLTree(old_self)

    self.update_height()
    return self
  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def _right_rotate(self):
    old_self = self.node
    old_right = self.node.left.node.right
    self.node = self.node.left.node
    old_self.left = old_right
    self.node.right = AVLTree(old_self)

    self.update_height()
    return self
  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):

    self.update_height()
    self.update_balance()

    if self.balance > 1 and self.node.left.balance >= 0:
      self.node.left = self.node.left._right_rotate() 
    elif self.balance < -1 and self.node.right.balance <= 0: 
      self.node.right = self.node.right._left_rotate() 
    elif self.balance > 1 and self.node.left.balance < 0:
      self.node.left = self.node.left._left_rotate()
      self = self._right_rotate()
    elif self.balance < -1 and self.node.right.balance > 0: 
      self.node.right = self.node.right._right_rotate()
      self = self._left_rotate()
    
  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):  
    if not self.node: 
      self.node = Node(key)
    elif key > self.node.key:
      if self.node.right:
        self.node.right.insert(key)
      else:
        self.node.right = AVLTree(Node(key))
    else:
      if self.node.left:
        self.node.left.insert(key)
      else:
        self.node.left = AVLTree(Node(key))

    self.rebalance()