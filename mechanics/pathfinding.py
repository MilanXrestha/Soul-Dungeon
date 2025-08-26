# mechanics/pathfinding.py
"""Pathfinding implementation using recursion (Week 2)."""

from data_structures.custom_queue import Queue

class PathFinder:
    """Pathfinding for navigating the dungeon."""
    
    def __init__(self, world_map):
        self.map = world_map
    
    def is_valid_position(self, x, y):
        """Check if position is valid and not a wall."""
        return 0 <= x < 5 and 0 <= y < 5 and self.map[y][x] != 0
    
    def find_path_to_hope(self, start_x, start_y, hope_x, hope_y):
        """Find shortest path to hope using BFS."""
        if not (self.is_valid_position(start_x, start_y) and self.is_valid_position(hope_x, hope_y)):
            return None
        
        queue = Queue()
        queue.enqueue(((start_x, start_y), [(start_x, start_y)]), priority=1)
        visited = {(start_x, start_y)}
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # North, South, East, West
        
        while not queue.is_empty():
            item = queue.dequeue()
            if not item:
                return None
                
            (x, y), path = item['data']
            
            if x == hope_x and y == hope_y:
                return path
                
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.is_valid_position(new_x, new_y) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.enqueue(((new_x, new_y), path + [(new_x, new_y)]), priority=1)
        
        return None
    
    def find_nearest_healing(self, start_x, start_y):
        """Find nearest healing location (item room)."""
        healing_locations = [(x, y) for y in range(5) for x in range(5) if self.map[y][x] == 4]
        
        shortest_path = None
        shortest_distance = float('inf')
        
        for x, y in healing_locations:
            path = self.find_path_to_hope(start_x, start_y, x, y)
            if path and len(path) < shortest_distance:
                shortest_distance = len(path)
                shortest_path = path
        
        return shortest_path
    
    def reveal_fog_of_war(self, start_x, start_y, radius=1):
        """Reveal map within radius using recursion."""
        revealed = [[-1 for _ in range(5)] for _ in range(5)]
        
        def reveal(x, y, r):
            """Recursive function to reveal map."""
            if not (0 <= x < 5 and 0 <= y < 5) or r < 0:
                return
            
            revealed[y][x] = self.map[y][x]
            
            if r == 0:
                return
                
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                reveal(x + dx, y + dy, r - 1)
        
        reveal(start_x, start_y, radius)
        return revealed