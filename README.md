# SOUL DUNGEON: FROM ROCK BOTTOM TO GLORY 🕹️

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)
![Made with](https://img.shields.io/badge/made%20with-❤️-red)
![Purpose](https://img.shields.io/badge/purpose-mental%20health-purple)
![Experience](https://img.shields.io/badge/experience-emotional-orange)

## 🧠 What This Project Is About

Soul Dungeon is an interactive text-based adventure game that serves as a powerful metaphor for the journey through depression, anxiety, and emotional healing. Unlike traditional games focused on external enemies, this experience turns inward, asking players to navigate their own psychological landscape.

The game represents mental health struggles as a dungeon with various rooms containing:
- 👹 **Inner demons** (self-doubt, regret, anxiety, shame, etc.) that evolve as you progress
- 💎 **Items** representing fragments of hope and healing to be collected
- 🪞 **Mirrors** reflecting your evolving self-image across different phases
- 👥 **NPCs** (therapist, loved ones, strangers) offering phase-specific support and wisdom

Players progress through five emotional phases:
1. **Rock Bottom** - The beginning of the journey
2. **Struggle** - Taking first steps toward healing
3. **Realization** - Gaining clarity and insight
4. **Growth** - Building strength and resilience
5. **Glory** - Finding integration and acceptance

## 🌱 How It Helps

### Therapeutic Value

- **Externalization of Internal Struggles**: Represents abstract emotional states as tangible encounters
- **Safe Exploration**: Confront difficult emotions in a controlled environment
- **Progressive Narrative of Recovery**: Shows healing as an evolution, not elimination of struggles
- **Multiple Paths to Healing**: Demonstrates various coping strategies (confrontation, acceptance, support-seeking)
- **Normalization**: Portrays mental health struggles as a common human experience


## 🛠️ Data Structures Implemented

- **Lists & Matrices**: The game map (2D matrix) and player inventory (1D list)  
- **Recursion**: Fog of war and pathfinding algorithms  
- **Functions & Loops**: Main game loop and command processing  
- **Linked Lists**: Memory/journal system tracking the player's journey  
- **Stacks & Queues**: Undo feature (stack) and turn-based events (queue)  

## 🎮 Controls

- **Arrow Keys** → Move in four directions  
- **Command Keys**:  
  - `l` → Look around  
  - `i` → Check inventory  
  - `t` → Take item (when available)  
  - `f` → Face demon (when present)
  - `k` → Talk to NPCs (when present)
  - `x` → Examine mirror (when available)
  - `u` → Undo last move  
  - `h` → Help menu  
  - `s` → Save game  

## ⚙️ Installation

1. Ensure you have **Python 3.7+** installed  
2. Install required packages:  
   ```bash
   pip install colorama readchar
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## 📂 Project Structure

```
.
├── main.py                # Game entry point
├── content/               # Game content (demons, dialogues, items)
│   ├── demons.py          # Inner demon definitions
│   ├── dialogues.py       # Phase-specific conversations and narratives
│   └── items.py           # Collectible healing items
├── core/                  # Core game components
│   ├── game_state.py      # Main game controller
│   ├── player.py          # Player character and attributes
│   └── world.py           # World generation and management
├── data_structures/       # Custom implementations of required data structures
│   ├── custom_linked_list.py  # For memory tracking
│   ├── custom_queue.py    # For event management
│   └── custom_stack.py    # For move history
├── mechanics/             # Game systems
│   ├── battle_system.py   # Demon confrontation mechanics
│   ├── commands.py        # Player input processing
│   └── pathfinding.py     # Navigation algorithms
└── utils/                 # Utility functions
    ├── display.py         # UI and text presentation
    └── save_system.py     # Game saving/loading
```
✨ *"From rock bottom to glory – every step forward is a victory."*

---
