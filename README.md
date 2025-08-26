# README.md

# SOUL DUNGEON: FROM ROCK BOTTOM TO GLORY - Text-Based Adventure Game

A Python text-based adventure game that uses various data structures to tell a meaningful story
of navigating through inner demons and finding hope.

## Overview

Soul Dungeon is more than just a game - it's a metaphorical journey representing the struggles
with depression, anxiety, and the path to healing.

## Data Structures Implemented

- **Week 1 (Lists & Matrices)**: The game map (2D matrix) and player inventory (1D list)
- **Week 2 (Recursion)**: Fog of war and pathfinding algorithms
- **Week 3 (Functions & Loops)**: Main game loop and command processing
- **Week 4 (Linked Lists)**: Memory/journal system tracking the player's journey
- **Week 5 (Stacks & Queues)**: Undo feature (stack) and turn-based events (queue)

## Controls

- **Arrow Keys**: Move in four directions
- **Command Keys**:
  - `l` - Look around
  - `i` - Check inventory
  - `t` - Take item (when available)
  - `f` - Face demon (when present)
  - `u` - Undo last move
  - `h` - Help menu
  - `s` - Save game

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required packages: `pip install colorama readchar`
3. Run the game: `python main.py`

## Project Structure

- `main.py` - Game entry point
- `content/` - Game content (demons, dialogues, items)
- `core/` - Core game components (player, world, game state)
- `data_structures/` - Custom implementations of required data structures
- `mechanics/` - Game systems (commands, battles, pathfinding)
- `utils/` - Utility functions (display, save system)