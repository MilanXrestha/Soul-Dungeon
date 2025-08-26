# mechanics/commands.py
"""Command processor for player input."""

import readchar
import random
from content.items import Items
from content.dialogues import Dialogues
from mechanics.battle_system import BattleSystem
from utils.display import Display
from utils.save_system import SaveSystem

class CommandProcessor:
    """Process player commands with simplified controls."""
    
    def __init__(self, game_state):
        self.game = game_state
    
    def process_input(self):
        """Get and process player input."""
        Display.print_hint("Use arrow keys to move or type a key command")
        
        key = readchar.readkey()
        
        # Handle arrow keys for movement
        if key == readchar.key.UP:
            self.move_up()
        elif key == readchar.key.DOWN:
            self.move_down()
        elif key == readchar.key.RIGHT:
            self.move_right()
        elif key == readchar.key.LEFT:
            self.move_left()
        
        # Handle command keys
        elif key.lower() == 'l':
            self.look()
        elif key.lower() == 'i':
            self.inventory()
        elif key.lower() == 't':
            self.take_item()
        elif key.lower() == 'f':
            self.face_demon()
        elif key.lower() == 'k':
            self.talk_to_npc()
        elif key.lower() == 'u':
            self.undo_move()
        elif key.lower() == 's':
            self.save_game()
        elif key.lower() == 'h':
            self.show_help()
        elif key.lower() == 'x':
            self.examine_mirror()
    
    def is_valid_move(self, direction):
        """Check if a move is valid."""
        x, y = self.game.player.position
        
        if direction == 'up' and y > 0 and self.game.world.map[y-1][x] != 0:
            return True
        if direction == 'down' and y < 4 and self.game.world.map[y+1][x] != 0:
            return True
        if direction == 'right' and x < 4 and self.game.world.map[y][x+1] != 0:
            return True
        if direction == 'left' and x > 0 and self.game.world.map[y][x-1] != 0:
            return True
        
        return False
    
    def move(self, direction):
        """Move in a specified direction."""
        if not self.is_valid_move(direction):
            Display.print_message("You can't go that way")
            return
            
        x, y = self.game.player.position
        new_x, new_y = x, y
        
        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'right':
            new_x += 1
        elif direction == 'left':
            new_x -= 1
        
        # Save current position for undo
        self.game.move_history.push((x, y))
        
        # Update position
        self.game.player.position = [new_x, new_y]
        
        # Trigger random events occasionally
        if random.random() < 0.15:  # 15% chance per move for events
            event_types = ['memory', 'inner_voice', 'encouragement']
            event_type = random.choice(event_types)
            
            if event_type == 'memory':
                self.game.event_queue.enqueue({'type': 'memory'})
            elif event_type == 'inner_voice':
                messages = [
                    "Keep going. This path has meaning.",
                    "Every step is a choice to continue.",
                    "The darkness isn't forever.",
                    "You've survived every bad day so far.",
                    "You are more than your darkest thoughts.",
                    "Growth happens in these small moments.",
                    "Healing isn't linear, but it is possible.",
                    "Your story isn't over yet."
                ]
                self.game.event_queue.enqueue({
                    'type': 'inner_voice',
                    'message': random.choice(messages)
                })
            elif event_type == 'encouragement':
                self.game.event_queue.enqueue({'type': 'encouragement'})
    
    def move_up(self):
        """Move up."""
        self.move('up')
    
    def move_down(self):
        """Move down."""
        self.move('down')
    
    def move_right(self):
        """Move right."""
        self.move('right')
    
    def move_left(self):
        """Move left."""
        self.move('left')
    
    def look(self):
        """Look around the current room in detail."""
        x, y = self.game.player.position
        
        Display.clear_screen()
        Display.print_centered_title("LOOKING AROUND")
        
        room_name = self.game.world.get_room_name(x, y)
        room_desc = self.game.world.get_detailed_room_description(x, y, self.game.player)
        
        Display.print_message(room_name)
        Display.print_message(room_desc)
        
        # Add situational details based on room type
        room_type = self.game.world.map[y][x]
        
        if room_type == 3:  # Demon room
            Display.print_message("You sense a presence here. Something you've been avoiding.")
            Display.print_hint("Press 'f' to face it")
        elif room_type == 4:  # Item room
            Display.print_message("There's something here that might help you.")
            Display.print_hint("Press 't' to take it")
        elif room_type == 5:  # Mirror room
            Display.print_message("The mirror reflects more than just your appearance.")
            Display.print_hint("Press 'x' to examine it")
        elif room_type == 6:  # Therapist
            Display.print_message("Someone waits patiently, offering a safe space to talk.")
            Display.print_hint("Press 'k' to talk to them")
        elif room_type == 7:  # Loved one
            Display.print_message("A familiar presence. Someone who knows and accepts you.")
            Display.print_hint("Press 'k' to connect with them")
        elif room_type == 8:  # Stranger
            Display.print_message("A fellow traveler on their own journey. There's understanding in their eyes.")
            Display.print_hint("Press 'k' to share experiences")
        
        Display.pause()
    
    def inventory(self):
        """Display inventory contents."""
        Display.clear_screen()
        Display.print_centered_title("INVENTORY")
        
        if not self.game.player.inventory:
            Display.print_message("Your hands are empty, but your heart carries weight.")
        else:
            for i, item in enumerate(self.game.player.inventory, 1):
                print(f"{i}. {item['name']}: {item['description']}")
                print(f"   Type: {item['type'].capitalize()}, Value: +{item['value']}")
        
        Display.pause()
    
    def take_item(self):
        """Take an item from the current room."""
        x, y = self.game.player.position
        
        if self.game.world.map[y][x] != 4:
            Display.print_message("There's nothing here to take")
            return
        
        item = Items.get_random_item()
        item_key = item['name'].lower().replace(' ', '_')
        
        Display.clear_screen()
        Display.print_centered_title("ITEM FOUND")
        Display.slow_print(Dialogues.ITEM_DISCOVERIES.get(item_key, "You found something valuable."))
        
        # Apply item effects
        self.game.player.gain_item(item, self.game)
        
        # Mark room as cleared
        self.game.world.map[y][x] = 1
        
        Display.print_message(f"You gained: {item['name']}")
        if item['type'] == 'hope':
            Display.print_message(f"Hope increased by {item['value']}")
        elif item['type'] == 'strength':
            Display.print_message(f"Strength increased by {item['value']}")
        elif item['type'] == 'clarity':
            Display.print_message(f"Clarity increased by {item['value']}")
        
        Display.pause()
    
    def face_demon(self):
        """Confront an inner demon in the current room."""
        x, y = self.game.player.position
        
        if self.game.world.map[y][x] != 3:
            Display.print_message("There are no demons to face here")
            return
        
        # Choose demon based on game phase for variety
        phase = self.game.game_phase
        
        # Get available demons for the current phase
        demons = list(Dialogues.DEMON_ENCOUNTERS[phase].keys())
        
        # Pick a random demon from the available options
        demon_type = random.choice(demons)
        
        # Initiate battle
        battle = BattleSystem(self.game)
        battle.battle_loop(demon_type)
    
    def talk_to_npc(self):
        """Talk to an NPC for insight and support."""
        x, y = self.game.player.position
        room_type = self.game.world.map[y][x]
        
        # Check if in an NPC room (6=Therapist, 7=Loved One, 8=Stranger)
        if room_type not in [6, 7, 8]:
            Display.print_message("There's no one here to talk to")
            return
        
        Display.clear_screen()
        
        # Determine NPC type
        npc_types = {6: 'therapist', 7: 'loved_one', 8: 'stranger'}
        npc_type = npc_types[room_type]
        
        # Get phase-specific dialogue
        phase = self.game.game_phase
        
        # Display greeting
        Display.print_centered_title(f"CONVERSATION")
        Display.slow_print(Dialogues.NPC_ENCOUNTERS[phase][npc_type]['greeting'])
        Display.pause()
        
        # Choose a random conversation
        conversation = random.choice(Dialogues.NPC_ENCOUNTERS[phase][npc_type]['conversations'])
        Display.slow_print(conversation)
        
        # Apply effects based on NPC and phase
        hope_gain = 5
        burden_decrease = 0
        
        # Adjust effects based on phase (stronger in later phases)
        if phase == "struggle":
            hope_gain += 2
            burden_decrease += 2
        elif phase == "realization":
            hope_gain += 4
            burden_decrease += 4
        elif phase == "growth":
            hope_gain += 6
            burden_decrease += 6
        elif phase == "glory":
            hope_gain += 8
            burden_decrease += 8
        
        # Adjust effects based on NPC type
        if npc_type == 'therapist':
            # Therapist helps with clarity and burden
            self.game.player.clarity += 3
            burden_decrease += 5
            Display.print_message(f"Clarity increased by 3, Burden decreased by {burden_decrease}")
            
        elif npc_type == 'loved_one':
            # Loved ones provide more hope
            hope_gain += 3
            Display.print_message(f"Hope increased by {hope_gain}")
            
        elif npc_type == 'stranger':
            # Strangers provide both hope and strength
            self.game.player.strength += 2
            Display.print_message(f"Hope increased by {hope_gain}, Strength increased by 2")
        
        # Apply effects
        self.game.player.hope += hope_gain
        self.game.player.burden = max(0, self.game.player.burden - burden_decrease)
        
        # Record the interaction
        self.game.player.add_memory(f"You connected with someone. {conversation.strip().split('.')[0]}.", hope_gained=hope_gain)
        self.game.npcs_visited += 1
        
        # Mark room as normal after conversation (NPC moves on)
        self.game.world.map[y][x] = 1
        
        Display.pause()
    
    def undo_move(self):
        """Undo the last move using the move history stack."""
        position, message = self.game.move_history.pop()
        
        if position:
            self.game.player.position = list(position)
            Display.print_message(f"{message} You return to where you were.")
        else:
            Display.print_message(message)
    
    def save_game(self):
        """Save the current game state."""
        Display.clear_screen()
        Display.print_centered_title("SAVE JOURNEY")
        Display.print_message("Choose a save slot (1-3):")
        
        key = readchar.readkey()
        if key in ['1', '2', '3']:
            slot_num = int(key)
            message = SaveSystem.save_game(self.game, slot_num)
            Display.print_message(message)
        else:
            Display.print_message("Invalid slot number")
        
        Display.pause()
    
    def show_help(self):
        """Show game help and controls."""
        Display.clear_screen()
        Display.print_centered_title("HELP")
        Display.print_message(Dialogues.HELP_TEXT)
        Display.pause()
    
    def examine_mirror(self):
        """Examine the mirror in a mirror room, with phase-specific messages."""
        x, y = self.game.player.position
        
        if self.game.world.map[y][x] != 5:
            Display.print_message("There's no mirror here to examine")
            return
        
        Display.clear_screen()
        Display.print_centered_title("MIRROR OF TRUTH")
        
        # Use phase-specific mirror messages
        phase = self.game.game_phase
        Display.slow_print(Dialogues.MIRROR_REFLECTIONS[phase])
        
        # Apply effects that increase with progression
        hope_gain = 5
        burden_decrease = 5
        
        # Mirrors become more powerful in later phases
        if phase == 'struggle':
            hope_gain = 7
            burden_decrease = 7
        elif phase == 'realization':
            hope_gain = 8
            burden_decrease = 10
        elif phase == 'growth':
            hope_gain = 10
            burden_decrease = 12
        elif phase == 'glory':
            hope_gain = 15
            burden_decrease = 15
        
        self.game.player.hope += hope_gain
        self.game.player.burden = max(0, self.game.player.burden - burden_decrease)
        self.game.player.add_memory(f"You faced yourself in the mirror during your {phase}.", hope_gained=hope_gain)
        
        Display.print_message(f"Hope increased by {hope_gain}, Burden decreased by {burden_decrease}")
        Display.pause()