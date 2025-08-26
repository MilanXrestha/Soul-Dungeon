# core/player.py
"""Player character module."""

from data_structures.custom_linked_list import LinkedList
from datetime import datetime

class Player:
    """Player character with emotional stats and inventory."""
    
    def __init__(self, name="Lost Soul"):
        self.name = name
        self.position = [0, 0]  # Starting position
        
        # Emotional stats instead of traditional HP/MP
        self.hope = 10  # Very low at start
        self.strength = 5
        self.clarity = 0
        self.burden = 100  # Weight of depression
        
        # Inventory as a list (Week 1)
        self.inventory = []
        
        # Memory/Journal as linked list (Week 4)
        self.memories = LinkedList()
        
        # Current emotional state
        self.state = "broken"
    
    def add_memory(self, memory, hope_gained=0):
        """Add a significant memory/realization with timestamp."""
        self.memories.append({
            'text': memory,
            'hope_gained': hope_gained,
            'timestamp': datetime.now().isoformat()
        })
    
    def gain_item(self, item, game_state=None):
        """Add an item to inventory and apply its effects."""
        self.inventory.append(item)
        
        if item['type'] == "hope":
            self.hope += item['value']
        elif item['type'] == "clarity":
            self.clarity += item['value']
        elif item['type'] == "strength":
            self.strength += item['value']
            
        if game_state:
            game_state.items_collected += 1  # Update milestone counter
    
    def face_demon(self, game_state=None):
        """Track confronting inner demons."""
        if game_state:
            game_state.demons_faced += 1  # Update milestone counter
    
    def get_status_description(self):
        """Return emotional state description based on hope level."""
        if self.hope < 20:
            return "You feel hollow, like a shadow of who you once were."
        elif self.hope < 40:
            return "A faint spark flickers within you, fragile but present."
        elif self.hope < 60:
            return "You're beginning to remember what it feels like to feel."
        elif self.hope < 80:
            return "Light is breaking through the cracks in your armor."
        else:
            return "You stand tall, scars and all, radiating quiet strength."