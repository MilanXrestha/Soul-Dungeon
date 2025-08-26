# core/world.py
"""World map and room management."""

import random

class World:
    """Manages the dungeon map and room descriptions."""
    
    def __init__(self):
        # 2D matrix representing the dungeon (Week 1)
        self.map = self._create_emotional_map()
        self.current_room = None
        
    def _create_emotional_map(self):
        """Create a 5x5 dungeon where each room represents an emotional state."""
        return self.generate_emotional_journey_map()
    
    def generate_emotional_journey_map(self):
        """Generate a map with randomized item, demon, and NPC locations."""
        # Create a more open map with fewer walls
        # 0 = Wall, 1 = Empty, 3 = Demon, 4 = Item, 5 = Mirror, 6 = Therapist, 7 = Loved One, 8 = Stranger
        base_map = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        
        # Ensure at least one path through the map
        valid_positions = [(x, y) for y in range(5) for x in range(5) if base_map[y][x] == 1 and (x, y) != (0, 0)]
        
        # Place special rooms
        item_count = 4  # More items
        demon_count = 3  # More demons
        npc_count = 3   # Three NPCs (therapist, loved one, stranger)
        
        # Place items
        item_locations = random.sample(valid_positions, item_count)
        remaining_positions = [p for p in valid_positions if p not in item_locations]
        
        # Place demons
        demon_locations = random.sample(remaining_positions, demon_count)
        remaining_positions = [p for p in remaining_positions if p not in demon_locations]
        
        # Place mirror
        mirror_location = random.choice(remaining_positions)
        remaining_positions = [p for p in remaining_positions if p != mirror_location]
        
        # Place NPCs
        npc_locations = random.sample(remaining_positions, npc_count)
        
        # Apply to map
        for x, y in item_locations:
            base_map[y][x] = 4  # Item room
        
        for x, y in demon_locations:
            base_map[y][x] = 3  # Demon room
            
        base_map[mirror_location[1]][mirror_location[0]] = 5  # Mirror room
        
        # Set NPC rooms (6=Therapist, 7=Loved One, 8=Stranger)
        for i, (x, y) in enumerate(npc_locations):
            base_map[y][x] = 6 + i  # 6, 7, 8
        
        return base_map
    
    def regenerate_map_for_phase(self, game_phase):
        """Generate a new map when phase changes to ensure challenges in all phases."""
        new_map = self.generate_emotional_journey_map()
        
        # Keep player's current position clear
        current_position = (0, 0)  # Default starting position
        new_map[current_position[1]][current_position[0]] = 1
        
        self.map = new_map
        return new_map
    
    def get_room_name(self, x, y):
        """Get emotional room names based on room type."""
        room_type = self.map[y][x]
        
        if (x, y) == (0, 0):
            return "The Void of Beginning"
        if room_type == 1:
            return f"Chamber of Shadows"
        elif room_type == 2:
            return f"Memory Glade"
        elif room_type == 3:
            return f"Den of Darkness"
        elif room_type == 4:
            return f"Haven of Light"
        elif room_type == 5:
            return f"Mirror of Truth"
        elif room_type == 6:
            return f"Therapist's Office"
        elif room_type == 7:
            return f"Familiar Presence"
        elif room_type == 8:
            return f"Kindred Spirit"
        return "Unknown Place"
    
    def get_room_description(self, x, y):
        """Return emotionally charged room descriptions."""
        room_type = self.map[y][x]
        
        descriptions = {
            0: "A solid wall blocks your path.",
            1: [
                "The walls here whisper your failures.",
                "Empty. Like how you feel inside.",
                "The silence here is deafening.",
                "Shadows dance where memories once lived."
            ],
            2: "A fragment of your past glimmers here, painful but important.",
            3: "Something dark lurks here. A piece of yourself you've been running from.",
            4: "A gentle warmth emanates from something in this room.",
            5: "A mirror stands before you. Do you dare look at yourself?",
            6: "Someone sits here patiently. Their presence feels safe, non-judgmental.",
            7: "A familiar figure waits here. Someone who knows you, who cares for you.",
            8: "A fellow traveler rests here. Someone who understands the journey."
        }
        
        if room_type == 1:
            return random.choice(descriptions[1])
        return descriptions.get(room_type, "You shouldn't be here.")
    
    def get_detailed_room_description(self, x, y, player):
        """Get room description with emotional coloring based on player state."""
        base_desc = self.get_room_description(x, y)
        room_name = self.get_room_name(x, y)
        
        if not player:
            return f"{base_desc}"
            
        # Add emotional coloring based on player's hope
        if player.hope < 20:
            emotional_filter = "\nEverything here feels heavy, oppressive."
        elif player.hope < 50:
            emotional_filter = "\nYou notice small details you missed before."
        else:
            emotional_filter = "\nThe space feels different now. Lighter somehow."
        
        return f"{base_desc}{emotional_filter}"