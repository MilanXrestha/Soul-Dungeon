# content/items.py
"""Items the player can collect during their journey."""

import random

class Items:
    """Symbolic items representing pieces of healing."""
    
    ITEMS = {
        'fragment_of_hope': {
            'name': 'Fragment of Hope',
            'description': 'A tiny spark of light that refuses to die, no matter how dark it gets.',
            'type': 'hope',
            'value': 5,
            'pickup_message': "You cup the fragile light in your hands. It's warm."
        },
        
        'memory_of_joy': {
            'name': 'Memory of Joy',
            'description': 'A crystallized moment when you genuinely smiled.',
            'type': 'hope',
            'value': 7,
            'pickup_message': "The memory floods back. You had forgotten you could feel this way."
        },
        
        'shard_of_strength': {
            'name': 'Shard of Strength',
            'description': 'Proof that you survived something you thought would break you.',
            'type': 'strength',
            'value': 3,
            'pickup_message': "You remember: You've been strong before. You can be again."
        },
        
        'thread_of_connection': {
            'name': 'Thread of Connection',
            'description': 'A reminder that you are not, and have never been, truly alone.',
            'type': 'hope',
            'value': 6,
            'pickup_message': "Someone, somewhere, cares. The thread proves it."
        },
        
        'seed_of_tomorrow': {
            'name': 'Seed of Tomorrow',
            'description': 'A tiny promise that things can grow, can change, can bloom.',
            'type': 'clarity',
            'value': 4,
            'pickup_message': "In your palm, a seed. Small, but containing infinite possibility."
        },
        
        'echo_of_laughter': {
            'name': 'Echo of Laughter',
            'description': 'The ghost of a genuine laugh, yours from better days.',
            'type': 'hope',
            'value': 8,
            'pickup_message': "The sound surprises you. When did you last laugh like that?"
        },
        
        'piece_of_self': {
            'name': 'Piece of Self',
            'description': 'A part of you that got lost in the darkness, now found.',
            'type': 'strength',
            'value': 5,
            'pickup_message': "You feel a little more whole, a little more yourself."
        },
        
        'courage_token': {
            'name': 'Courage Token',
            'description': 'A reminder that you can speak up and your voice has power.',
            'type': 'strength',
            'value': 6,
            'pickup_message': "The weight of the token in your hand feels empowering."
        },
        
        'compass_of_purpose': {
            'name': 'Compass of Purpose',
            'description': 'A guide pointing toward what matters most to you.',
            'type': 'clarity',
            'value': 7,
            'pickup_message': "The needle steadies, showing a direction you recognize."
        },
        
        'forgiveness_feather': {
            'name': 'Forgiveness Feather',
            'description': 'Permission to release past mistakes and self-judgment.',
            'type': 'hope',
            'value': 9,
            'pickup_message': "As you hold it, some weight lifts from your shoulders."
        }
    }
    
    @staticmethod
    def get_random_item():
        """Return a copy of a random item from ITEMS."""
        item_key = random.choice(list(Items.ITEMS.keys()))
        return Items.ITEMS[item_key].copy()
    
    @staticmethod
    def get_item(item_key):
        """Get a specific item by key, returning a copy to prevent modification."""
        return Items.ITEMS.get(item_key, Items.ITEMS['fragment_of_hope']).copy()