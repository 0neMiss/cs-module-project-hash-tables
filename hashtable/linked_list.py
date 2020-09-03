class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
    # reference to the tail of the list
    self.tail = None
  def add_to_head(self, value):
      new_node = Node(value, None)
      if not self.head:
        # if the list is initially empty, set both head and tail to the new node
        self.head = new_node
        self.tail = new_node
      else:
        # set the current head's next reference to our the current head
        new_node.set_next(self.head)
        # set the head to the new node
        self.head = new_node

  def add_to_tail(self, value):
    # wrap the input value in a node
    new_node = Node(value, None)
    # check if there is no head (i.e., the list is empty)
    if not self.head:
      # if the list is initially empty, set both head and tail to the new node
      self.head = new_node
      self.tail = new_node
    # we have a non-empty list, add the new node to the tail
    else:
      # set the current tail's next reference to our new node
      self.tail.set_next(new_node)
      # set the list's tail reference to the new node
      self.tail = new_node

  def remove_head(self):
    # return None if there is no head (i.e. the list is empty)
    if not self.head:
      return None
    # if head has no next, then we have a single element in our list
    if not self.head.get_next():
      # get a reference to the head
      head = self.head
      # delete the list's head reference
      self.head = None
      # also make sure the tail reference doesn't refer to anything
      self.tail = None
      # return the value
      return head.get_value()
    # otherwise we have more than one element in our list
    value = self.head.get_value()
    # set the head reference to the current head's next node in the list
    self.head = self.head.get_next()
    return value

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False