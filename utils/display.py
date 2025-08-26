# utils/display.py
"""Display utilities for the game."""

import time
import sys
import os
from colorama import init, Fore, Style, Back

# Initialize colorama
init(autoreset=True)

class Display:
    """Display utilities for the game UI."""
    
    COLORS = {
        'hope': Fore.YELLOW,
        'danger': Fore.RED,
        'healing': Fore.GREEN,
        'memory': Fore.MAGENTA,
        'clarity': Fore.CYAN,
        'neutral': Fore.WHITE,
        'title': Fore.BLUE + Style.BRIGHT,
        'action': Fore.GREEN + Style.BRIGHT,
        'movement': Fore.YELLOW + Style.BRIGHT,
        'special': Fore.MAGENTA + Style.BRIGHT
    }
    
    _text_speed = 0.03  # Default delay per character in seconds
    
    @staticmethod
    def set_text_speed(speed):
        """Set text speed for slow_print."""
        Display._text_speed = max(0.0, min(speed, 0.1))
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_divider(char="-"):
        """Print a divider line."""
        width = min(os.get_terminal_size().columns, 80)
        print(char * width)
    
    @staticmethod
    def print_centered(text):
        """Center text in the terminal."""
        width = min(os.get_terminal_size().columns, 80)
        print(text.center(width))
    
    @staticmethod
    def print_centered_title(text):
        """Print a centered, colored title."""
        width = min(os.get_terminal_size().columns, 80)
        title = f"{Display.COLORS['title']}{text.center(width)}{Style.RESET_ALL}"
        print("\n" + title + "\n")
    
    @staticmethod
    def print_message(text):
        """Print a normal message with newline."""
        print(f"\n{text}")
    
    @staticmethod
    def print_hint(text):
        """Print a hint message in a subtle color."""
        print(f"\n{Fore.CYAN}{text}{Style.RESET_ALL}")
    
    @staticmethod
    def print_position(x, y, room_type):
        """Display the player's current position and room type."""
        room_descriptions = {
            0: "Wall (Impassable)",
            1: "Empty Room",
            2: "Memory Room",
            3: "Demon Room",
            4: "Item Room",
            5: "Mirror Room",
            6: "Therapist's Office",
            7: "Loved One",
            8: "Fellow Traveler"
        }
        room_desc = room_descriptions.get(room_type, "Unknown")
        
        # Color code based on room type
        color = Fore.WHITE
        if room_type == 3:  # Demon
            color = Fore.RED
        elif room_type == 4:  # Item
            color = Fore.GREEN
        elif room_type == 5:  # Mirror
            color = Fore.CYAN
        elif room_type in [6, 7, 8]:  # NPCs
            color = Fore.MAGENTA
        
        print(f"\n{Fore.CYAN}Current Position: [{x},{y}] - {color}{room_desc}{Style.RESET_ALL}")
    
    @staticmethod
    def print_actions(actions):
        """Print available actions in a formatted way."""
        print(f"\n{Style.BRIGHT}Available Actions:{Style.RESET_ALL}")
        
        # Group by type (movement vs other)
        movement = []
        special = []
        basic = []
        
        for key, desc in actions:
            if key in ["↑", "↓", "→", "←"]:
                movement.append((key, desc))
            elif key in ["f", "t", "x", "k"]:  # Special interactions
                special.append((key, desc))
            else:
                basic.append((key, desc))
        
        # Print movement keys with special formatting
        if movement:
            print(f"{Display.COLORS['movement']}Movement: {Style.RESET_ALL}", end="")
            move_text = ", ".join([f"{Display.COLORS['movement']}{key}{Style.RESET_ALL}: {desc}" for key, desc in movement])
            print(move_text)
        
        # Print special actions
        if special:
            print(f"{Display.COLORS['special']}Interactions:{Style.RESET_ALL}")
            for key, desc in special:
                print(f"  {Display.COLORS['special']}{key}{Style.RESET_ALL}: {desc}")
        
        # Print basic actions
        if basic:
            print(f"{Display.COLORS['action']}Basic Actions:{Style.RESET_ALL}")
            for key, desc in basic:
                print(f"  {Display.COLORS['action']}{key}{Style.RESET_ALL}: {desc}")
    
    @staticmethod
    def slow_print(text, delay=None):
        """Print text slowly for dramatic effect."""
        delay = Display._text_speed if delay is None else delay
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def pause(message="Press Enter to continue..."):
        """Pause for player input."""
        input(f"\n{message}")
    
    @staticmethod
    def print_status_bar(hope, burden):
        """Display hope and burden as visual meters."""
        width = min(os.get_terminal_size().columns, 80)
        bar_length = width // 2 - 10
        
        # Hope bar
        hope_filled = int(hope * bar_length / 100)
        hope_empty = bar_length - hope_filled
        hope_bar = "█" * hope_filled + "░" * hope_empty
        
        # Burden bar
        burden_filled = int(burden * bar_length / 100)
        burden_empty = bar_length - burden_filled
        burden_bar = "█" * burden_filled + "░" * burden_empty
        
        print(f"{Display.COLORS['hope']}Hope: [{hope_bar}] {hope}/100{Style.RESET_ALL}")
        print(f"{Display.COLORS['danger']}Burden: [{burden_bar}] {burden}/100{Style.RESET_ALL}")
    
    @staticmethod
    def display_map(world_map, player_x, player_y, revealed_map, path=None):
        """Display the game map with fog of war."""
        print("\nMap:")
        
        path_set = set(path) if path else set()
        
        for y in range(len(revealed_map)):
            row = ""
            for x in range(len(revealed_map[0])):
                if x == player_x and y == player_y:
                    row += Display.format_with_color("P ", "hope")
                elif (x, y) in path_set and revealed_map[y][x] != -1:
                    row += Display.format_with_color("· ", "clarity")
                elif revealed_map[y][x] == -1:
                    row += "? "
                elif revealed_map[y][x] == 0:
                    row += Display.format_with_color("# ", "danger")
                elif revealed_map[y][x] == 1:
                    row += ". "
                elif revealed_map[y][x] == 3:
                    row += Display.format_with_color("D ", "danger")
                elif revealed_map[y][x] == 4:
                    row += Display.format_with_color("I ", "healing")
                elif revealed_map[y][x] == 5:
                    row += Display.format_with_color("M ", "clarity")
                elif revealed_map[y][x] == 6:
                    row += Display.format_with_color("T ", "memory")
                elif revealed_map[y][x] == 7:
                    row += Display.format_with_color("L ", "memory")
                elif revealed_map[y][x] == 8:
                    row += Display.format_with_color("S ", "memory")
            print(row)
        
        print("\nP=Player D=Demon I=Item M=Mirror T=Therapist L=Loved One S=Stranger #=Wall ?=Unknown")
    
    @staticmethod
    def format_with_color(text, emotion):
        """Apply color based on emotional context."""
        color = Display.COLORS.get(emotion, Display.COLORS['neutral'])
        return f"{color}{text}{Style.RESET_ALL}"