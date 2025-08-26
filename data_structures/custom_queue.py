# data_structures/custom_queue.py
"""Queue implementation for event management (Week 5)."""

class Queue:
    """Priority queue for turn-based events."""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item, priority=2):
        """Add an event with a priority (1=high, 2=medium, 3=low)."""
        # Ensure item has a priority field
        item_with_priority = item.copy() if isinstance(item, dict) else {'data': item}
        item_with_priority['priority'] = priority
        
        # Insert into sorted position based on priority
        i = 0
        while i < len(self.items) and self.items[i]['priority'] <= priority:
            i += 1
        self.items.insert(i, item_with_priority)
    
    def dequeue(self):
        """Remove and return the highest-priority event."""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        """View the highest-priority event without removing it."""
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0