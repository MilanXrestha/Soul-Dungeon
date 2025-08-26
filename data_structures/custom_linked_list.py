# data_structures/custom_linked_list.py
"""Linked list implementation for memory tracking (Week 4)."""

class Node:
    """Node for the linked list, holding data and a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked list for storing memories (Week 4)."""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add a memory to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add a memory to the start of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def get_recent(self, n=5):
        """Retrieve the n most recent memories."""
        result = []
        current = self.head
        while current and len(result) < n:
            result.append(current.data)
            current = current.next
        return result
    
    def find_by_keyword(self, keyword):
        """Search memories containing the keyword (case-insensitive)."""
        results = []
        current = self.head
        keyword = keyword.lower()
        while current:
            if keyword in current.data.get('text', '').lower():
                results.append(current.data)
            current = current.next
        return results
    
    def display_all(self):
        """Return all memories in the list."""
        memories = []
        current = self.head
        while current:
            memories.append(current.data)
            current = current.next
        return memories