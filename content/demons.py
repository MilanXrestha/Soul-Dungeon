# content/demons.py
"""Inner demons that the player must confront during their journey."""

class InnerDemons:
    """Detailed inner demon configurations"""
    
    DEMONS = {
        'self-doubt': {
            'name': 'The Voice of Doubt',
            'description': 'A shadow wearing your face, whispering every fear you have about yourself.',
            'power': 15,
            'attacks': {
                'whisper': {
                    'damage': 3,
                    'message': "It whispers your failures, each word a dagger."
                },
                'mirror': {
                    'damage': 5,
                    'message': "It shows you distorted reflections of your worst moments."
                }
            },
            'defeat_message': "The Voice quiets. It will return, but weaker each time you face it."
        },
        
        'regret': {
            'name': 'The Shadow of Regret',
            'description': 'A heavy presence that drags behind you, made of all the paths not taken.',
            'power': 20,
            'attacks': {
                'replay': {
                    'damage': 4,
                    'message': "It forces you to relive moments you wish you could change."
                },
                'weight': {
                    'damage': 6,
                    'message': "The weight of what-ifs crushes down on your shoulders."
                }
            },
            'defeat_message': "The Shadow loosens its grip. The past remains, but it no longer owns you."
        },
        
        'anxiety': {
            'name': 'The Storm of Tomorrow',
            'description': 'A swirling vortex of what-ifs and worst-case scenarios.',
            'power': 18,
            'attacks': {
                'overwhelm': {
                    'damage': 4,
                    'message': "A thousand terrible futures flash before your eyes."
                },
                'paralyze': {
                    'damage': 3,
                    'message': "The possibilities freeze you in place, unable to move forward."
                }
            },
            'defeat_message': "The Storm calms. The future is uncertain, but you can face it."
        },
        
        'shame': {
            'name': 'The Weight of Shame',
            'description': 'A heavy cloak that makes every step feel exposed.',
            'power': 25,
            'attacks': {
                'expose': {
                    'damage': 5,
                    'message': "It reveals your flaws to an invisible crowd."
                },
                'judgment': {
                    'damage': 4,
                    'message': "It whispers that you'll never be enough."
                }
            },
            'defeat_message': "The cloak lifts. You are more than your mistakes."
        },
        
        'loneliness': {
            'name': 'The Void of Isolation',
            'description': 'A cold emptiness that swallows all warmth.',
            'power': 22,
            'attacks': {
                'silence': {
                    'damage': 4,
                    'message': "The silence reminds you no one is there."
                },
                'abandon': {
                    'damage': 5,
                    'message': "It tells you everyone leaves in the end."
                }
            },
            'defeat_message': "The void shrinks. Connection is possible, even now."
        },
        
        'perfectionism': {
            'name': 'The Measure of Perfection',
            'description': 'A figure with a ruler and clipboard, judging your every move.',
            'power': 24,
            'attacks': {
                'compare': {
                    'damage': 5,
                    'message': "It shows you others who are doing better, achieving more."
                },
                'standard': {
                    'damage': 6,
                    'message': "It raises the bar just as you reach it, making success impossible."
                }
            },
            'defeat_message': "The measuring stops. Good enough becomes possible."
        },
        
        'anger': {
            'name': 'The Flame of Rage',
            'description': 'A burning figure that threatens to consume everything in its path.',
            'power': 23,
            'attacks': {
                'burn': {
                    'damage': 6,
                    'message': "It sets your thoughts ablaze, making rational thought impossible."
                },
                'fuel': {
                    'damage': 4,
                    'message': "It feeds on every slight, every injustice, growing hotter."
                }
            },
            'defeat_message': "The flames recede to a controlled burn, warming rather than destroying."
        },
        
        'apathy': {
            'name': 'The Gray Nothing',
            'description': 'A fog that drains color and feeling from everything it touches.',
            'power': 20,
            'attacks': {
                'numb': {
                    'damage': 5,
                    'message': "It dulls your senses, making joy and pain equally distant."
                },
                'drain': {
                    'damage': 4,
                    'message': "It saps your motivation, making effort seem pointless."
                }
            },
            'defeat_message': "The fog thins. Feeling returns, painful but vital."
        }
    }
    
    @staticmethod
    def get_demon(demon_type):
        """Returns a copy of the specified demon type, or self-doubt if type not found."""
        return InnerDemons.DEMONS.get(demon_type, InnerDemons.DEMONS['self-doubt']).copy()