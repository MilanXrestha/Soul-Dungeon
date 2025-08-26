# mechanics/battle_system.py
"""Battle system for confronting inner demons."""

import random
from content.demons import InnerDemons
from content.dialogues import Dialogues
from utils.display import Display

class BattleSystem:
    """System for confronting inner demons."""
    
    def __init__(self, game_state):
        self.game = game_state
        self.player = game_state.player
    
    def create_demon(self, demon_type):
        """Create inner demon from template."""
        return InnerDemons.get_demon(demon_type)
    
    def battle_loop(self, demon_type):
        """Main battle loop for confronting demons."""
        demon = self.create_demon(demon_type)
        phase = self.game.game_phase
        
        # Scale demon power based on game phase to ensure challenge
        if phase == "struggle":
            demon['power'] = int(demon['power'] * 1.2)
        elif phase == "realization":
            demon['power'] = int(demon['power'] * 1.4)
        elif phase == "growth":
            demon['power'] = int(demon['power'] * 1.6)
        elif phase == "glory":
            demon['power'] = int(demon['power'] * 1.8)
            
        demon_power = demon['power']
        demon_name = demon['name']
        
        Display.clear_screen()
        Display.print_centered_title(f"CONFRONTING {demon_name.upper()}")
        Display.slow_print(Dialogues.DEMON_ENCOUNTERS[phase][demon_type]['appearance'])
        Display.pause()
        
        while demon_power > 0 and self.player.hope > 0:
            # Show battle state
            Display.clear_screen()
            Display.print_centered_title(f"CONFRONTING {demon_name.upper()}")
            Display.print_divider()
            
            print(f"{demon_name} power: {demon_power}")
            print(f"Your hope: {self.player.hope}")
            print(f"Your strength: {self.player.strength}")
            print(f"Your clarity: {self.player.clarity}")
            Display.print_divider()
            
            # Demon attack
            attack = random.choice(list(demon['attacks'].keys()))
            Display.slow_print(f"\n{demon['attacks'][attack]['message']}")
            damage = demon['attacks'][attack]['damage']
            self.player.hope = max(0, self.player.hope - damage)
            Display.print_message(f"You lost {damage} hope")
            
            if self.player.hope <= 0:
                break
            
            # Player options
            Display.print_divider()
            Display.print_message("How do you respond?")
            print("1. Stand firm - Use strength to resist")
            print("2. Use memories - Recall past strength")
            print("3. Accept truth - Reduce burden by acknowledging reality")
            print("4. Retreat inward - Lose hope, gain clarity")
            print("5. Use item - Use an inventory item")
            
            Display.print_hint("Enter 1-5 to choose")
            
            valid_choice = False
            while not valid_choice:
                try:
                    choice = int(input())
                    if 1 <= choice <= 5:
                        valid_choice = True
                        if choice == 1:
                            demon_power = self.stand_firm(demon, demon_power)
                        elif choice == 2:
                            demon_power = self.use_memories(demon, demon_power)
                        elif choice == 3:
                            demon_power = self.accept_truth(demon, demon_power)
                        elif choice == 4:
                            demon_power = self.retreat_inward(demon_power)
                        elif choice == 5:
                            demon_power = self.use_item(demon, demon_power)
                    else:
                        Display.print_message("Please enter a number between 1 and 5")
                except ValueError:
                    Display.print_message("Please enter a valid number")
            
            Display.pause()
        
        # Battle outcome
        if demon_power <= 0:
            self.victory(demon, demon_type)
        else:
            self.defeat(demon)
    
    def stand_firm(self, demon, demon_power):
        """Use strength to resist."""
        damage = max(1, self.player.strength)
        demon_power -= damage
        Display.slow_print(f"\nYou stand your ground, drawing on your strength. The {demon['name']} weakens.")
        Display.print_message(f"Demon power reduced by {damage}")
        return demon_power
    
    def use_memories(self, demon, demon_power):
        """Use memories to fight back."""
        damage = max(1, self.player.clarity + 5)
        demon_power -= damage
        memories = self.player.memories.get_recent(1)
        if memories:
            Display.slow_print(f"\nYou recall: {memories[0]['text']}")
        else:
            Display.slow_print("\nYou try to recall something, anything, but the fog is too thick.")
        Display.print_message(f"Demon power reduced by {damage}")
        return demon_power
    
    def accept_truth(self, demon, demon_power):
        """Accept the demon's truth to reduce burden."""
        damage = 10
        demon_power -= damage
        self.player.burden = max(0, self.player.burden - 5)
        Display.slow_print(f"\nYou nod, accepting the painful truth in the {demon['name']}'s words.")
        Display.print_message(f"Demon power reduced by {damage}, burden decreased by 5")
        return demon_power
    
    def retreat_inward(self, demon_power):
        """Retreat, losing hope but gaining clarity."""
        self.player.hope = max(0, self.player.hope - 5)
        self.player.clarity += 3
        demon_power -= 3
        Display.slow_print("\nYou turn inward, shielding yourself but losing some light.")
        Display.print_message(f"Lost 5 hope, gained 3 clarity, demon power reduced by 3")
        return demon_power
    
    def use_item(self, demon, demon_power):
        """Use an inventory item to gain hope or damage demon."""
        if not self.player.inventory:
            Display.slow_print("\nYou have no items to use.")
            return demon_power
        
        Display.clear_screen()
        Display.print_centered_title("USE AN ITEM")
        print("\nAvailable items:")
        for i, item in enumerate(self.player.inventory, 1):
            print(f"{i}. {item['name']} ({item['type']}: +{item['value']})")
        print(f"{len(self.player.inventory) + 1}. Cancel")
        
        Display.print_hint(f"Enter 1-{len(self.player.inventory) + 1} to choose")
        
        try:
            choice = int(input())
            if 1 <= choice <= len(self.player.inventory):
                item = self.player.inventory.pop(choice - 1)  # Remove used item
                
                if item['type'] == 'hope':
                    hope_gain = item['value'] // 2  # Half effect in battle
                    self.player.hope += hope_gain
                    Display.slow_print(f"\nUsing {item['name']} restores your hope.")
                    Display.print_message(f"Hope increased by {hope_gain}")
                else:
                    damage = item['value']
                    demon_power -= damage
                    Display.slow_print(f"\nYou wield {item['name']} against the {demon['name']}.")
                    Display.print_message(f"Demon power reduced by {damage}")
            elif choice == len(self.player.inventory) + 1:
                Display.print_message("You decide not to use an item")
            else:
                Display.print_message("Invalid choice")
        except ValueError:
            Display.print_message("Please enter a valid number")
        
        return demon_power
    
    def victory(self, demon, demon_type):
        """Handle victory over a demon."""
        phase = self.game.game_phase
        
        Display.clear_screen()
        Display.print_centered_title("DEMON FACED")
        Display.slow_print(Dialogues.DEMON_ENCOUNTERS[phase][demon_type]['defeat'])
        
        # Rewards scale with game phase
        hope_gain = 10
        burden_decrease = 10
        
        if phase == "struggle":
            hope_gain = 12
            burden_decrease = 12
        elif phase == "realization":
            hope_gain = 15
            burden_decrease = 15
        elif phase == "growth":
            hope_gain = 18
            burden_decrease = 18
        elif phase == "glory":
            hope_gain = 20
            burden_decrease = 20
        
        self.player.hope += hope_gain
        self.player.burden = max(0, self.player.burden - burden_decrease)
        self.player.add_memory(f"You faced and overcame {demon['name']}.", hope_gained=hope_gain)
        
        Display.print_message(f"Hope increased by {hope_gain}, burden decreased by {burden_decrease}")
        Display.pause()
        
        # Clear demon from room
        x, y = self.player.position
        self.game.world.map[y][x] = 1
        self.player.face_demon(self.game)
    
    def defeat(self, demon):
        """Handle defeat by a demon."""
        Display.clear_screen()
        Display.print_centered_title("RETREAT")
        Display.slow_print(f"\nThe {demon['name']} overwhelms you.")
        Display.slow_print("Sometimes, survival is victory enough.")
        
        phase = self.game.game_phase
        hope_loss = 5
        
        # In later phases, defeat is less punishing
        if phase == "realization":
            hope_loss = 4
        elif phase == "growth":
            hope_loss = 3
        elif phase == "glory":
            hope_loss = 2
        
        self.player.hope = max(0, self.player.hope - hope_loss)
        self.player.add_memory(f"You fled from {demon['name']}, but it lingers.", hope_gained=-hope_loss)
        
        Display.print_message(f"Hope decreased by {hope_loss}")
        Display.pause()