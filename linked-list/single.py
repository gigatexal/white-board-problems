class Node:
    def __init__(self, value):
        self._value = value
        self._next: Node = None
        
    @property
    def value(self):
        return self._value

    def link_node(self, next_node):
        self._next = next_node

    @property
    def nxt(self):
        return self._next

class LinkedList:
    def __init__(self):
        self._size = 0
        self._head: Node

    @property
    def size(self):
        return self._size
   
    # pop the first item, head item
    def popleft(self):
        if self.size:
            prev_head = self._head
            new_head = prev_head.nxt
            val = prev_head.value
            del self._head
            self._head = new_head
            self._size = self._size - 1
            return val

    # pop the tail or last item
    def pop(self):
        """
        iterate through the list until
        the final end node is found, it's
        .next will point to None
        while iterating keep track of:
        current and previous nodes
        when current.next points to nothing
        we stop, we return it's value
        delete it from the list
        and then set the previous.next to None
        """
        if self.size:
            previous, current = self._head, self._head
            while current.nxt:
                previous, current = current, current.nxt
            value = current.value
            previous._next = None
            del current
            return value
                

    def add(self, item):
        n = Node(value=item)
        if self.size:
            # LIFO - add item to the front
            # set the "old" list's head to the next of the new head
            former_head_node: Node = self._head
            n.link_node(next_node=former_head_node)
            self._head = n
            # list is empty so just add create the head
        else:
            self._head = n
        self._size = self._size + 1
        # no need to add head next since by default it's empty/set to None

    def print(self):
        _iter: Node  = self._head
        while _iter:
            print(_iter.value)
            _iter = _iter.nxt




