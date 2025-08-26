# data_structures/custom_stack.py
"""Stack implementation for move history (Week 5)."""

class Stack:
    """Stack for tracking move history with a max size of 10."""
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size
    
    def push(self, item):
        """Add a move to the stack, removing oldest if at max size."""
        if len(self.items) >= self.max_size:
            self.items.pop(0)  # Remove oldest move
        self.items.append(item)
        return "Move recorded."
    
    def pop(self):
        """Remove and return the most recent move."""
        if self.is_empty():
            return None, "No moves to undo."
        return self.items.pop(), "Move undone."
    
    def peek(self):
        """View the most recent move without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0