"""
Implements a doubly-linked-list data structure.
"""


class Node:
    """Creates a Node instance
    
    Args:
        data (str): The data that the node will hold.
        next_node (Node): The next node in the doubly linked list.
        previous_node (Node): The previous node in the doubly linked list.
    """
    def __init__(self, key: str, data: str, next_node: 'Node' = None, previous_node: 'Node' = None):
        # Initialize the key from the Map that points to the node
        self._key = key

        # Initialize the data that is stored within the node
        self._data = data

        # Initialize the next node in the doubly linked list or default to null
        self._next_node = next_node

        # Initialize the previous node in the doubly linked list or default to null
        self._previous_node = previous_node

    @property
    def key(self):
        """
        Getter for the key internal variable
        """
        return self._key

    @property
    def data(self):
        """
        Getter for the data internal variable
        """
        return self._data

    @data.setter
    def data(self, new_data: str):
        """Setter for the data internal variable
        
        Args:
            new_data (str): The new data for the node
        """
        self._data = new_data

    @property
    def next_node(self):
        """
        Getter for the next node internal variable

        Returns:
            (Node): The next node in the doubly linked list
        """
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: 'Node'):
        """Setter for the next node internal variable
        
        Args:
            next_node (Node): The next node in the doubly linked list
        """
        self._next_node = next_node

    @property
    def previous_node(self):
        """
        Getter for the previous node internal variable

        Returns:
            (Node): The previous node in the doubly linked list
        """
        return self._previous_node
    
    @previous_node.setter
    def previous_node(self, previous_node: 'Node'):
        """Setter for the previous node internal variable
            
        Args:
            previous_node (Node): The previous node in the doubly linked list
        """
        self._previous_node = previous_node


class DoublyLinkedList:
    """Creates a Doubly Linked List instance
    
    Args:
        first_node (Node): The first node in the doubly linked list.
        last_node (Node): The last node in the doubly linked list.
    """
    def __init__(self, first_node: Node = None, last_node: Node = None):
        # Initialize the first node in the doubly linked list or default to null
        self._first_node = first_node

        # Initialize the last node in the doubly linked list or default to null
        self._last_node = last_node

    @property
    def first_node(self) -> Node:
        """
        Getter for the first node internal variable.

        Returns:
            (Node): The first node is the doubly linked list.
        """
        return self._first_node

    @first_node.setter
    def first_node(self, first_node: Node):
        """
        Setter for the first node internal variable.

        Args:
            first_node (Node): The first node in the doubly linked list.
        """
        self._first_node = first_node

    @property
    def last_node(self) -> Node:
        """
        Getter for the last node internal variable.

        Returns:
            (Node): The last node is the doubly linked list.
        """
        return self._last_node

    @last_node.setter
    def last_node(self, last_node: Node):
        """
        Setter for the last node internal variable
        """
        self._last_node = last_node

    def insert_at_front(self, key: str, value: str) -> Node:
        """Adds a new node to the beginning of the doubly linked list.
        
        Args:
            value (str): The value that is stored in the new node.
        """
        new_node = Node(key=key, data=value)

        # If there are no elements yet in the doubly linked list:
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else: # If the doubly linked list already has at least one node:
            new_node.next_node = self.first_node
            self.first_node.previous_node = new_node
            self.first_node = new_node

        return new_node

    def move_to_front(self, target_node: Node):
        """Moves a node from anywhere in the doubly linked list to the front.
        
        Args:
            target_node (Node): The node that is to be moved to the front of the doubly linked
            list.
        """
        # If there are no elements yet in the doubly linked list:
        if not self.first_node:
            self.first_node = target_node
            self.last_node = target_node
        # If the targeted node is already the first node in the doubly linked list:
        elif target_node == self.first_node:
            return
        else: # If the targeted node is coming from elsewhere in the doubly linked list:
            target_node.next_node = self.first_node
            self.first_node.previous_node = target_node
            self.first_node = target_node

    # CONSIDER(david): remove_arbitrary_node trusts that target_node belongs to
    # *this* DoublyLinkedList instance. It catches a node that was never linked
    # (or was already removed, since we now null out its pointers on removal)
    # and returns None for those. It does NOT catch a node that's a legitimate
    # middle node of a DIFFERENT DoublyLinkedList — that case silently corrupts
    # the OTHER list's pointers instead of erroring, since the guard only checks
    # "does this node have both neighbors set," not "is it reachable from *my*
    # first_node." Confirmed via manual testing on 2026-07-22.
    #
    # Full validation would mean walking the list to confirm membership, which
    # is O(n) and defeats the reason this method exists (O(1) removal via a
    # direct node reference). For now this is an accepted precondition: callers
    # (Cache) must only ever pass node references they own. Revisit if this
    # library is ever used somewhere that precondition might not hold.
    def remove_node(self, target_node: Node) -> Node:
        """Removes a targeted node that could be anywhere in the doubly linked list.

        Args:
            target_node (Node): The targeted node to be removed.
        
        Returns:
            (Node): The node that was removed from the doubly linked list.
        """
        # If there are no elements yet in the doubly linked list:
        if not self.last_node and not self.first_node:
            return None
        else: # If the doubly linked list already has at least one node:
            # If the target node is the only node in the doubly linked list:
            if target_node == self.first_node and target_node == self.last_node:
                self.last_node = None
                self.first_node = None
                target_node.next_node = None
                target_node.previous_node = None
            elif target_node == self.first_node: # If the target node is the first node:
                self.first_node = target_node.next_node
                self.first_node.previous_node = None
                target_node.next_node = None
            elif target_node == self.last_node: # If the target node is the last node:
                self.last_node = target_node.previous_node
                self.last_node.next_node = None
                target_node.previous_node = None
            # If the target node is in the middle of the doubly linked list:
            elif target_node.next_node and target_node.previous_node:
                target_node.next_node.previous_node = target_node.previous_node
                target_node.previous_node.next_node = target_node.next_node
                target_node.next_node = None
                target_node.previous_node = None
            else:
                return None

            return target_node

    def clear_doubly_linked_list(self):
        """
        Clears the doubly linked list by setting the first and last node values to null

        Notes:
            We are intentionally leaving the rest of the nodes to be picked up by Python's garbage
            collector as to maintain O(1) time complexity.
        """
        self.first_node = None
        self.last_node = None
