# core/game_state.py
"""Main game state controller."""

import random
from core.player import Player
from core.world import World
from data_structures.custom_stack import Stack
from data_structures.custom_queue import Queue
from content.dialogues import Dialogues
from utils.display import Display

class GameState:
    """Manages the overall game state and progression."""
    
    def __init__(self):
        self.player = Player()
        self.world = World()
        self.game_phase = "rock_bottom"
        self.running = True
        self.demons_faced = 0  # Milestone tracking
        self.items_collected = 0  # Milestone tracking
        self.npcs_visited = 0   # Track NPC interactions
        
        # Initialize data structures
        self.move_history = Stack()  # For backtracking (Week 5)
        self.event_queue = Queue()   # For turn-based events (Week 5)
        
        # Command processor needs to be imported here to avoid circular imports
        from mechanics.commands import CommandProcessor
        self.command_processor = CommandProcessor(self)
        
    def start_new_game(self):
        """Begin a new journey."""
        Display.clear_screen()
        Display.slow_print(Dialogues.INTRO_SEQUENCES['awakening'])
        Display.pause()
        Display.clear_screen()
        
        # Brief tutorial
        Display.print_centered_title("WELCOME TO YOUR JOURNEY")
        Display.slow_print("""
        Use the arrow keys to move through the dungeon of your mind.
        Press 'h' at any time to see all available commands.
        
        Find fragments of hope and face your inner demons.
        Each step forward is a victory, no matter how small.
        """)
        Display.print_hint("Press ENTER to begin")
        Display.pause()
        
        self.game_loop()
    
    def resume_game(self):
        """Resume a saved game."""
        Display.print_message("Continuing your journey...")
        Display.pause()
        self.game_loop()
    
    def game_loop(self):
        """Main game loop."""
        while self.running:
            if self.player.hope <= 0:
                self.game_over()
                break
                
            # Display current state
            self.display_current_state()
            
            # Get player input
            self.command_processor.process_input()
            
            # Process queued events
            self.process_events()
            
            # Check for phase transitions
            self.check_progression()
    
    def display_current_state(self):
        """Show current game state and available actions."""
        Display.clear_screen()
        Display.print_centered_title(f"SOUL DUNGEON: FROM ROCK BOTTOM TO GLORY - {self.game_phase.upper().replace('_', ' ')}")
        Display.print_status_bar(self.player.hope, self.player.burden)
        
        # Display revealed map
        from mechanics.pathfinding import PathFinder
        pathfinder = PathFinder(self.world.map)
        revealed_map = pathfinder.reveal_fog_of_war(self.player.position[0], self.player.position[1])
        Display.display_map(self.world.map, self.player.position[0], self.player.position[1], revealed_map)
        
        # Display player position with room type
        x, y = self.player.position
        room_type = self.world.map[y][x]
        Display.print_position(x, y, room_type)
        
        # Room description
        Display.print_divider()
        Display.print_message(self.world.get_room_name(x, y))
        Display.print_message(self.world.get_room_description(x, y))
        
        # Player status
        Display.print_message(self.player.get_status_description())
        
        # Available actions hint
        Display.print_divider()
        available_actions = self.get_available_actions()
        Display.print_actions(available_actions)
    
    def get_available_actions(self):
        """Get list of available actions in current room."""
        x, y = self.player.position
        actions = []
        
        # Movement options
        if y > 0 and self.world.map[y-1][x] != 0:
            actions.append(("↑", "Move Up"))
        if y < 4 and self.world.map[y+1][x] != 0:
            actions.append(("↓", "Move Down"))
        if x < 4 and self.world.map[y][x+1] != 0:
            actions.append(("→", "Move Right"))
        if x > 0 and self.world.map[y][x-1] != 0:
            actions.append(("←", "Move Left"))
        
        # Standard actions
        actions.extend([
            ("l", "Look around"),
            ("i", "Inventory"),
            ("u", "Undo move"),
            ("s", "Save game"),
            ("h", "Help")
        ])
        
        # Room-specific actions
        room_type = self.world.map[y][x]
        if room_type == 3:  # Demon room
            actions.append(("f", "Face demon"))
        elif room_type == 4:  # Item room
            actions.append(("t", "Take item"))
        elif room_type == 5:  # Mirror room
            actions.append(("x", "Examine mirror"))
        elif room_type in [6, 7, 8]:  # NPC rooms
            actions.append(("k", "Talk to person"))
        
        return actions
    
    def process_events(self):
        """Process queued events."""
        if not self.event_queue.is_empty():
            event = self.event_queue.dequeue()
            
            if event['type'] == 'memory':
                self.trigger_memory_event(event.get('text', ''), event.get('hope_gained', 0))
            elif event['type'] == 'demon_encounter':
                self.trigger_demon_event()
            elif event['type'] == 'inner_voice':
                self.trigger_inner_voice(event['message'])
            elif event['type'] == 'encouragement':
                self.trigger_encouragement()
    
    def trigger_memory_event(self, memory_text='', hope_gained=0):
        """Trigger a memory that surfaces."""
        if not memory_text:
            memories = [
                "A hand reaching out to help you up. You can't remember whose.",
                "The taste of your favorite meal. Someone made it just for you.",
                "A song that made you feel understood. The melody lingers.",
                "A place where you felt safe. It might still exist somewhere.",
                "Words someone said that made you feel seen. They meant it.",
                "A moment when you surprised yourself with your own strength.",
                "The first time you realized you could survive this darkness.",
                "A small act of kindness you once showed someone else.",
                "A time when you stood up for yourself, even though it was hard.",
                "A genuine smile that reached your eyes. It can happen again."
            ]
            memory_text = random.choice(memories)
            hope_gained = 2
        
        Display.clear_screen()
        Display.print_centered_title("A MEMORY SURFACES")
        Display.slow_print(memory_text)
        
        self.player.add_memory(memory_text, hope_gained)
        self.player.hope += hope_gained
        
        if hope_gained > 0:
            Display.print_message(f"Hope increased by {hope_gained}")
        
        Display.pause()
    
    def trigger_demon_event(self):
        """Trigger encounter with inner demon."""
        demons = ['self-doubt', 'regret', 'anxiety', 'shame', 'loneliness', 
                 'perfectionism', 'anger', 'apathy']
        demon = random.choice(demons)
        
        Display.clear_screen()
        Display.print_centered_title("PRESENCE FELT")
        Display.slow_print(f"You feel the presence of {demon.replace('-', ' ')} surrounding you.")
        Display.print_hint("Press 'f' to confront it, or any other key to continue")
        Display.pause()
    
    def trigger_inner_voice(self, message):
        """Inner voice events - can be positive or negative."""
        Display.clear_screen()
        Display.print_centered_title("A VOICE WITHIN")
        Display.slow_print(message)
        Display.pause()
    
    def trigger_encouragement(self):
        """Random positive encouragement."""
        encouragements = [
            "You're stronger than you know. Keep going.",
            "Every step forward is a victory, no matter how small.",
            "You've made it this far. That's something to be proud of.",
            "Healing isn't linear, but you're still making progress.",
            "Your journey matters. You matter.",
            "The darkness doesn't last forever. Hold on.",
            "Sometimes, survival itself is a triumph.",
            "You're doing the hardest work there is. Be gentle with yourself."
        ]
        Display.clear_screen()
        Display.print_centered_title("A MOMENT OF CLARITY")
        Display.slow_print(random.choice(encouragements))
        
        self.player.hope += 1
        Display.print_message("Hope increased by 1")
        Display.pause()
    
    def check_progression(self):
        """Check if player has progressed to next phase."""
        old_phase = self.game_phase
        
        if self.game_phase == "rock_bottom" and self.player.hope >= 30:
            self.transition_to_phase("struggle")
        elif self.game_phase == "struggle" and self.player.hope >= 50:
            self.transition_to_phase("realization")
        elif self.game_phase == "realization" and self.player.hope >= 70:
            self.transition_to_phase("growth")
        elif self.game_phase == "growth" and self.player.hope >= 90:
            self.transition_to_phase("glory")
            self.complete_journey()
        
        # If phase changed, regenerate the map to ensure demons in all phases
        if old_phase != self.game_phase and self.game_phase != "glory":
            current_pos = self.player.position
            self.world.regenerate_map_for_phase(self.game_phase)
            # Ensure player's location is still valid
            self.world.map[current_pos[1]][current_pos[0]] = 1
    
    def transition_to_phase(self, phase):
        """Transition to a new phase of the journey."""
        self.game_phase = phase
        
        Display.clear_screen()
        Display.print_centered_title(f"PHASE: {phase.upper()}")
        Display.slow_print(Dialogues.PHASE_TRANSITIONS[phase])
        Display.pause()
    
    def game_over(self):
        """Handle game over state."""
        Display.clear_screen()
        Display.print_centered_title("DARKNESS OVERWHELMS")
        Display.slow_print("""
        The darkness becomes too much.
        You sink to the ground, unable to continue.
        
        But even now, a faint spark remains within you.
        A chance to try again.
        """)
        
        Display.print_hint("Press 'l' to load game or any other key to return to main menu")
        key = input().lower()
        
        if key == 'l':
            from main import load_game
            load_game()
        
        self.running = False
    
    def complete_journey(self):
        """Complete the journey."""
        Display.clear_screen()
        Display.print_centered_title("JOURNEY COMPLETE")
        Display.slow_print(Dialogues.EPILOGUE)
        
        Display.pause()
        self.show_final_stats()
        self.running = False
    
    def show_final_stats(self):
        """Show journey summary."""
        Display.clear_screen()
        Display.print_centered_title("YOUR JOURNEY")
        Display.print_divider()
        
        print(f"\nYou started with {10} hope. You ended with {self.player.hope}.")
        print(f"You began carrying {100} burden. You now carry {self.player.burden}.")
        print(f"You found {self.items_collected} fragments of yourself.")
        print(f"You faced {self.demons_faced} inner demons.")
        print(f"You connected with {self.npcs_visited} others along the way.")
        
        print("\nMost importantly:")
        print("You survived.")
        print("You grew.")
        print("You chose to keep going.")
        
        # Hope progression chart
        memories = self.player.memories.display_all()
        hope_history = [10]
        current_hope = 10
        
        for memory in memories:
            if memory.get('hope_gained', 0) != 0:
                current_hope += memory.get('hope_gained', 0)
                hope_history.append(current_hope)
        
        if len(hope_history) > 1:
            print("\nYour Hope Over Time:")
            max_value = max(hope_history)
            bar_width = 30
            for i, hope in enumerate(hope_history):
                bar = "█" * int(hope * bar_width / max_value)
                print(f"Step {i:<2} {bar} {hope}")
        
        Display.pause()