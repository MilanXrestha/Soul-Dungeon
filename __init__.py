"""
Soul Dungeon: A Journey from Darkness to Light
==============================================

An emotional text-based adventure that uses data structures
to tell a story of overcoming depression and finding hope.

This is more than a game - it's a metaphor for the human journey
through despair, struggle, growth, and triumph.

Data Structures as Metaphors:
- Lists & Matrices: The landscape of the mind
- Recursion: Finding clarity through mental fog  
- Linked Lists: Chains of memories that define us
- Stacks: The weight of the past we carry
- Queues: Anxieties waiting to be processed

Remember: Even at rock bottom, growth is possible.
"""

__version__ = '1.0.0'
__author__ = 'A Developer Who Understands'
__email__ = 'hope@souldungeon.journey'

# Import main entry point
from main import main

# Emotional constants
STARTING_HOPE = 10
STARTING_BURDEN = 100
MAX_HOPE = 100
MIN_BURDEN = 0

# Game messages
WELCOME_MESSAGE = """
Welcome to Soul Dungeon.
This is your story.
Every choice matters.
Every step forward is victory.
"""

COMPLETION_MESSAGE = """
You've completed the journey.
But remember - healing is not a destination.
It's a continuous path.
Be proud of how far you've come.
"""

# Support resources (displayed at game end)
SUPPORT_RESOURCES = """
If you're struggling with depression or mental health:
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- SAMHSA National Helpline: 1-800-662-4357
- International Crisis Lines: findahelpline.com

You are not alone. Help is available.
"""

def get_stage_description(stage):
    """Get description for current emotional stage"""
    stages = {
        'rock_bottom': "The deepest darkness, where journey begins",
        'struggle': "Fighting against the weight of despair",
        'realization': "A spark of understanding emerges", 
        'growth': "Building strength, step by step",
        'glory': "Not perfection, but peace with yourself"
    }
    return stages.get(stage, "Unknown stage")

def show_resources():
    """Display mental health resources"""
    from utils.display import Display
    Display.clear_screen()
    Display.print_divider("=")
    Display.print_centered("RESOURCES FOR SUPPORT")
    Display.print_divider("=")
    print(SUPPORT_RESOURCES)
    Display.pause("Press Enter to continue...")

# Make key components easily importable
from core import GameState, Player, World
from utils import Display
from mechanics import CommandProcessor

__all__ = [
    'main',
    'GameState', 
    'Player',
    'World',
    'Display',
    'CommandProcessor',
    'WELCOME_MESSAGE',
    'COMPLETION_MESSAGE',
    'SUPPORT_RESOURCES',
    'show_resources'
]