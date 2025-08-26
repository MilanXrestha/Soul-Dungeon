# main.py
"""
Soul Dungeon: A Journey Through Inner Darkness
==============================================

A text-based adventure exploring emotional growth through
the metaphor of navigating a dungeon of inner demons.

Uses data structures to represent the journey of healing:
- Lists & Matrices: The dungeon map and inventory
- Recursion: Fog of war and pathfinding
- Functions & Loops: Game progression and player commands
- Linked Lists: Memory and experience tracking
- Stacks & Queues: Undo feature and event management
"""

import os
import readchar
from core.game_state import GameState
from utils.display import Display
from utils.save_system import SaveSystem

def display_menu():
    """Display the main menu with keyboard navigation"""
    Display.clear_screen()
    Display.print_centered_title("SOUL DUNGEON: FROM ROCK BOTTOM TO GLORY")
    Display.print_centered("A journey from darkness to light")
    Display.print_divider()
    
    print("\n1. New Journey")
    print("2. Continue Journey")
    print("3. Settings")
    print("4. Exit")
    
    Display.print_hint("Press 1-4 to select")
    
    while True:
        key = readchar.readkey()
        if key in ['1', '2', '3', '4']:
            return key

def settings_menu():
    """Menu for adjusting game settings"""
    Display.clear_screen()
    Display.print_centered_title("SETTINGS")
    Display.print_divider()
    
    print("\nText Speed:")
    print("1. Fast")
    print("2. Normal")
    print("3. Slow")
    print("4. Back")
    
    Display.print_hint("Press 1-4 to select")
    
    while True:
        key = readchar.readkey()
        if key == '1':
            Display.set_text_speed(0.01)
            Display.print_message("Text speed set to fast")
            return
        elif key == '2':
            Display.set_text_speed(0.03)
            Display.print_message("Text speed set to normal")
            return
        elif key == '3':
            Display.set_text_speed(0.06)
            Display.print_message("Text speed set to slow")
            return
        elif key == '4':
            return

def load_game():
    """Interface for loading saved games"""
    Display.clear_screen()
    Display.print_centered_title("LOAD JOURNEY")
    Display.print_divider()
    
    # Check for save files
    save_dir = SaveSystem.SAVE_DIR
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    save_files = [f for f in os.listdir(save_dir) if f.startswith("save_slot_")]
    
    if not save_files:
        Display.print_message("No saved journeys found")
        Display.pause()
        return None
    
    print("\nSelect a save file:")
    
    # Show only up to 3 save slots
    for i in range(1, 4):
        save_path = f"{save_dir}/save_slot_{i}.json"
        if os.path.exists(save_path):
            print(f"{i}. Save Slot {i}")
        else:
            print(f"{i}. Empty Slot")
            
    print("4. Back")
    
    Display.print_hint("Press 1-4 to select")
    
    while True:
        key = readchar.readkey()
        if key in ['1', '2', '3']:
            slot = int(key)
            save_path = f"{save_dir}/save_slot_{slot}.json"
            if os.path.exists(save_path):
                game = GameState()
                SaveSystem.load_game(game, slot)
                return game
            else:
                Display.print_message("No save file in this slot")
                Display.pause()
                return None
        elif key == '4':
            return None

def main():
    """Main program entry point"""
    while True:
        choice = display_menu()
        
        if choice == '1':
            # New game
            game = GameState()
            game.start_new_game()
            
        elif choice == '2':
            # Load game
            game = load_game()
            if game:
                game.resume_game()
                
        elif choice == '3':
            # Settings
            settings_menu()
            
        elif choice == '4':
            # Exit
            Display.clear_screen()
            Display.print_centered_title("FAREWELL")
            Display.slow_print("\nRemember that even in darkness, there is always a path forward.")
            Display.print_divider()
            Display.pause()
            break

if __name__ == "__main__":
    main()