# utils/save_system.py
"""Save and load game functionality."""

import json
import os
from utils.display import Display

class SaveSystem:
    """System for saving and loading game state."""
    
    SAVE_DIR = "saves"
    
    @staticmethod
    def save_game(game_state, slot):
        """Save game state to a file."""
        if not os.path.exists(SaveSystem.SAVE_DIR):
            os.makedirs(SaveSystem.SAVE_DIR)
        
        try:
            # Convert game state to serializable format
            save_data = {
                'player': {
                    'name': game_state.player.name,
                    'position': game_state.player.position,
                    'hope': game_state.player.hope,
                    'strength': game_state.player.strength,
                    'clarity': game_state.player.clarity,
                    'burden': game_state.player.burden,
                    'inventory': game_state.player.inventory,
                    'memories': game_state.player.memories.display_all()
                },
                'world': {
                    'map': game_state.world.map
                },
                'game_phase': game_state.game_phase,
                'move_history': game_state.move_history.items,
                'demons_faced': game_state.demons_faced,
                'items_collected': game_state.items_collected
            }
            
            with open(f"{SaveSystem.SAVE_DIR}/save_slot_{slot}.json", 'w') as f:
                json.dump(save_data, f, indent=4)
            return f"Journey saved in slot {slot}"
        except Exception as e:
            return f"Failed to save journey: {str(e)}"
    
    @staticmethod
    def load_game(game_state, slot):
        """Load game state from a file."""
        try:
            with open(f"{SaveSystem.SAVE_DIR}/save_slot_{slot}.json", 'r') as f:
                save_data = json.load(f)
            
            # Restore player
            game_state.player.name = save_data['player']['name']
            game_state.player.position = save_data['player']['position']
            game_state.player.hope = save_data['player']['hope']
            game_state.player.strength = save_data['player']['strength']
            game_state.player.clarity = save_data['player']['clarity']
            game_state.player.burden = save_data['player']['burden']
            game_state.player.inventory = save_data['player']['inventory']
            
            # Restore memories
            game_state.player.memories = game_state.player.memories.__class__()
            for memory in save_data['player']['memories']:
                game_state.player.memories.append(memory)
            
            # Restore world
            game_state.world.map = save_data['world']['map']
            
            # Restore game state
            game_state.game_phase = save_data['game_phase']
            game_state.demons_faced = save_data.get('demons_faced', 0)
            game_state.items_collected = save_data.get('items_collected', 0)
            
            # Restore move history
            game_state.move_history = game_state.move_history.__class__()
            for move in save_data['move_history']:
                game_state.move_history.push(move)
            
            Display.print_message(f"Journey loaded from slot {slot}")
            
            return True
        except FileNotFoundError:
            Display.print_message(f"No journey found in slot {slot}")
            return False
        except Exception as e:
            Display.print_message(f"Failed to load journey: {str(e)}")
            return False