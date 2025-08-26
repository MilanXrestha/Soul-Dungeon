# content/dialogues.py
"""Dialogue and narrative content for the game."""

class Dialogues:
    """Collection of narrative texts for the game."""
    
    INTRO_SEQUENCES = {
        'awakening': """
        You don't remember how you got here.
        
        The last thing you recall is lying in bed,
        staring at the ceiling,
        wondering if tomorrow would be any different.
        
        It wasn't.
        
        And now you're here, in this place that feels
        both foreign and terrifyingly familiar.
        """,
        
        'first_steps': """
        Your legs feel like lead.
        Each step forward takes monumental effort.
        
        But you move anyway.
        
        Because even in this darkness,
        some part of you refuses to give up completely.
        """
    }
    
    # Phase-specific demon encounters
    DEMON_ENCOUNTERS = {
        'rock_bottom': {
            'self-doubt': {
                'appearance': """
                A figure emerges from the shadows.
                It looks exactly like you, but wrong.
                
                Its eyes are hollow, its smile cruel.
                
                "Why do you even try?" it whispers.
                "You know you'll fail. You always do."
                """,
                'defeat': """
                The shadow dissipates, but not before whispering:
                "I'll always be here. Part of you."
                
                And you know it's right.
                But maybe... maybe that's okay.
                Maybe acknowledging the doubt is the first step.
                """
            },
            'regret': {
                'appearance': """
                The air grows heavy with the weight of words unsaid,
                chances not taken, bridges burned.
                
                A specter forms from your memories,
                wearing the faces of everyone you've let down.
                
                Including yourself.
                """,
                'defeat': """
                The specter fades, leaving behind a strange lightness.
                
                You can't change the past.
                But you're still here.
                Still breathing.
                Still capable of tomorrow.
                """
            },
            'anxiety': {
                'appearance': """
                The air thickens, making it hard to breathe.
                A swirling storm of "what ifs" surrounds you.
                
                Every possible terrible outcome.
                Every way things could go wrong.
                
                "You'll never be ready," it howls.
                "Disaster waits around every corner."
                """,
                'defeat': """
                The storm subsides to a gentle breeze.
                
                The future is still uncertain.
                It always will be.
                
                But uncertainty doesn't have to mean catastrophe.
                It can also mean possibility.
                """
            },
            'shame': {
                'appearance': """
                A heavy cloak settles over you.
                Every flaw, every mistake, feels exposed to the world.
                
                "They all see you for what you really are," it sneers.
                """,
                'defeat': """
                The cloak lifts, and you stand a little taller.
                Your flaws are real, but they don't define you.
                You are enough.
                """
            },
            'loneliness': {
                'appearance': """
                The air grows cold, the silence deafening.
                A void opens before you, swallowing warmth.
                
                "You're always alone," it whispers.
                "And you always will be."
                """,
                'defeat': """
                The void shrinks, its cold grip loosening.
                You remember: connection exists.
                Even a single thread is enough.
                """
            }
        },
        
        'struggle': {
            'self-doubt': {
                'appearance': """
                The shadow emerges again, but this time you were expecting it.
                
                "This small progress means nothing," it says.
                "You'll slide back into darkness. You always do."
                
                But there's something different now - 
                you recognize its voice as just that. A voice. Not truth.
                """,
                'defeat': """
                The shadow steps back, surprised by your resistance.
                
                "I'll be back," it threatens.
                
                "I know," you reply. "And I'll be ready."
                """
            },
            'regret': {
                'appearance': """
                Memories rise up again, moments of failure and loss.
                
                "Look at all you've ruined," the specter moans.
                "Look at all the time you've wasted."
                
                But now you notice something - these are just pieces of your story.
                Not the whole of it.
                """,
                'defeat': """
                The memories don't disappear, but they settle.
                
                You can't erase what happened.
                But you're learning that your past isn't your future.
                And that's something.
                """
            },
            'anxiety': {
                'appearance': """
                The storm of possibilities whirls, faster now, more desperate.
                
                "You think you're making progress? Think of all that could go wrong!
                Think of how much worse the fall will be if you dare to hope!"
                
                Its voice is shrill, almost... afraid?
                """,
                'defeat': """
                The storm still swirls, but you stand in its center now.
                
                Anxiety doesn't simply vanish.
                But you're learning to weather it.
                To function despite it.
                """
            },
            'shame': {
                'appearance': """
                The cloak tries to wrap around you once more.
                
                "You're putting on a brave face," it hisses.
                "But underneath, you're still broken. Still flawed."
                
                The weight is familiar. But now, somehow, bearable.
                """,
                'defeat': """
                You shrug the cloak off your shoulders.
                
                "Yes," you say. "I am flawed."
                
                The admission doesn't crush you this time.
                It simply is.
                """
            },
            'loneliness': {
                'appearance': """
                The void appears, but smaller now. Less absolute.
                
                "These connections you're making are temporary," it says.
                "In the end, everyone leaves."
                
                You feel the pull of isolation, but it's not as strong.
                """,
                'defeat': """
                The void recedes further.
                
                Connection is still hard. Still scary.
                But you're beginning to see that the risk might be worth it.
                That some people stay, even when it's difficult.
                """
            }
        },
        
        'realization': {
            'self-doubt': {
                'appearance': """
                The shadow stands before you, but it looks less like you now.
                More like a caricature, a distortion.
                
                "You think you understand?" it scoffs. "You think knowing
                makes a difference? You'll still fail."
                
                Its words sound hollow, rehearsed.
                """,
                'defeat': """
                The shadow grows transparent.
                
                "I'm still right," it insists, but its voice wavers.
                
                "Sometimes," you admit. "But not always. And I'm learning
                to tell the difference."
                """
            },
            'regret': {
                'appearance': """
                The memories surface, but they've changed. You see not just
                what happened, but the context. Your youth, your fear,
                your limited understanding at the time.
                
                "You should have known better," the specter accuses.
                
                And for the first time, you think: Maybe I didn't.
                """,
                'defeat': """
                The specter becomes less solid, more like mist.
                
                You're starting to see your past with compassion.
                To understand that you did the best you could with what you had.
                
                That doesn't erase the consequences.
                But it changes how you carry them.
                """
            },
            'anxiety': {
                'appearance': """
                The storm gathers, but you see patterns in it now.
                Recognize the triggers, the spirals, the catastrophic thinking.
                
                "But what if—" it starts.
                
                "What if things work out?" you interrupt.
                The thought is so foreign it catches you both by surprise.
                """,
                'defeat': """
                The storm doesn't disappear, but it becomes more predictable.
                
                You're learning its rhythms, its warning signs.
                You're finding ways to prepare, to shelter, to endure.
                
                And sometimes, even to step outside it entirely.
                """
            },
            'perfectionism': {
                'appearance': """
                A figure with a ruler and checklist materializes.
                It measures everything about you with cold precision.
                
                "Not enough," it declares. "Not nearly enough.
                Look at everyone else, so much further along."
                
                For the first time, you recognize this voice as external.
                Not your own. Imposed upon you.
                """,
                'defeat': """
                You take the ruler from its hands. Snap it in half.
                
                "I define 'enough' now," you say.
                
                The figure looks shocked, then uncertain.
                Its power was always in your belief of it.
                """
            },
            'anger': {
                'appearance': """
                Heat rises as a figure of flame appears.
                
                "Look at all you've suffered," it rages. "Look at the
                injustice. Why shouldn't you burn it all down?"
                
                The fire is seductive, energizing. But you see now
                that it consumes the wielder first.
                """,
                'defeat': """
                The flames don't extinguish, but they gather into a torch.
                
                Anger isn't wrong. It has a purpose - to highlight injustice,
                to fuel change, to establish boundaries.
                
                But now it's a tool. Not your master.
                """
            }
        },
        
        'growth': {
            'self-doubt': {
                'appearance': """
                The shadow is barely recognizable now, a wisp of what it was.
                
                "You're still not good enough," it says, but its voice
                lacks conviction. It's speaking from habit, not belief.
                
                You almost feel sorry for it.
                """,
                'defeat': """
                "I know what you are now," you tell the fading shadow.
                
                "You're the voice that kept me small. That kept me safe
                by keeping me from trying, from risking, from living."
                
                "I don't need that kind of safety anymore."
                """
            },
            'regret': {
                'appearance': """
                The memories appear, but now you see them as if from a distance.
                Not reliving them, but observing them.
                
                "These moments defined you," the specter says.
                
                "They shaped me," you correct. "But they don't confine me."
                """,
                'defeat': """
                You reach out and touch the memories, acknowledging them.
                
                "Thank you," you say, surprising yourself.
                
                Because each mistake taught you something.
                Each loss revealed what mattered.
                Each failure was a step on this path to yourself.
                """
            },
            'perfectionism': {
                'appearance': """
                The figure returns, rebuilding its measuring tools.
                
                "You've made progress," it admits. "But look how far
                you still have to go. Look at all the flaws that remain."
                
                It's more reasonable now, more insidious. But you recognize it.
                """,
                'defeat': """
                "Perfection was never the goal," you say firmly.
                
                "Growth was. Change was. And look—" you gesture around you.
                "I'm not who I was. That's enough."
                
                The figure has no answer for this.
                """
            },
            'apathy': {
                'appearance': """
                A gray fog rolls in, dulling the edges of everything.
                
                "Why keep trying?" it murmurs. "Why keep feeling?
                Wouldn't it be easier to just... stop caring?"
                
                The numbness it offers is tempting, but hollow.
                """,
                'defeat': """
                You walk through the fog, refusing its comfort.
                
                "Feeling hurts sometimes," you acknowledge.
                "But feeling nothing hurts always, in a way so constant
                I stopped recognizing it as pain."
                
                The fog parts around you, grudgingly.
                """
            },
            'anger': {
                'appearance': """
                The flame appears, but contained now, focused.
                
                "You've learned restraint," it says, almost approving.
                "But don't forget me. Don't let them take advantage
                of your newfound peace."
                
                There's wisdom in its words, you realize.
                """,
                'defeat': """
                You cup the flame in your hands, neither extinguishing
                nor feeding it.
                
                "I won't forget you," you promise. "You have your place.
                Just not every place. Not anymore."
                
                The flame nods, accepting its new role.
                """
            }
        },
        
        'glory': {
            'self-doubt': {
                'appearance': """
                The shadow is barely a smudge now, a faint outline.
                
                "You know I'll never truly leave," it whispers.
                
                "I know," you say. "And that's okay."
                """,
                'defeat': """
                You offer your hand to the shadow, and after a moment, it takes it.
                
                "You were trying to protect me," you acknowledge.
                
                "I was," it agrees, surprised by your understanding.
                
                "But I'm stronger now. I can protect myself."
                """
            },
            'shame': {
                'appearance': """
                The cloak appears, thin and threadbare.
                
                "You still have things to be ashamed of," it reminds you.
                
                "Yes," you agree. "I'm still human."
                
                The admission doesn't strengthen it as it once would have.
                """,
                'defeat': """
                You take the cloak and fold it neatly, tucking it away.
                
                "Shame has its place," you acknowledge. "It tells us when
                we've violated our own values. But it's a visitor now.
                Not a resident."
                
                The cloak accepts this new arrangement with dignity.
                """
            },
            'apathy': {
                'appearance': """
                The fog makes one final attempt, curling around your feet.
                
                "Life will still hurt," it warns. "People will still disappoint you."
                
                "They will," you agree. "That's part of being alive."
                """,
                'defeat': """
                The fog dissipates in the warmth of your certainty.
                
                Not certainty that things will be easy. Or that pain won't come.
                But certainty that whatever comes, you can face it.
                
                You've proven that to yourself, step by painful step.
                """
            },
            'perfectionism': {
                'appearance': """
                The figure makes a last stand, desperate and defensive.
                
                "If you abandon me, you'll backslide," it warns.
                "You'll become complacent. Mediocre. Is that what you want?"
                
                Its fear is almost touching.
                """,
                'defeat': """
                "I'm not abandoning standards," you explain gently.
                
                "I'm abandoning the illusion that I can or should be without flaw.
                That's not complacency. That's humanity."
                
                The figure nods slowly, finally understanding.
                """
            },
            'anxiety': {
                'appearance': """
                The storm appears, smaller than ever, more like a rain cloud.
                
                "What about the future?" it asks, its voice uncertain.
                
                "What about it?" you reply, and realize you mean it.
                """,
                'defeat': """
                The cloud releases a gentle rain, no longer threatening.
                
                "I'll still worry sometimes," you acknowledge.
                "But I won't let worry stop me from living."
                
                The uncertainty of tomorrow no longer overshadows
                the possibility of today.
                """
            }
        }
    }
    
    ITEM_DISCOVERIES = {
        'fragment_of_hope': """
        In the corner, something glimmers.
        
        A small, warm light.
        It's barely anything, but in this darkness,
        it might as well be the sun.
        
        You cup it gently in your hands.
        [Gained: Fragment of Hope]
        """,
        
        'memory_of_joy': """
        A photograph, faded and torn.
        You can barely make out the image,
        but you remember the feeling.
        
        You were happy once.
        You could be again.
        
        [Gained: Memory of Joy]
        """,
        
        'shard_of_strength': """
        Something glints amid the shadows.
        A broken piece of something once whole.
        
        As you pick it up, you feel a familiar resolve.
        A reminder of challenges weathered.
        
        [Gained: Shard of Strength]
        """,
        
        'thread_of_connection': """
        A delicate thread catches your eye,
        stretching into the darkness, connecting to... something.
        
        As you touch it, you feel a warmth.
        Someone is on the other end.
        
        [Gained: Thread of Connection]
        """,
        
        'seed_of_tomorrow': """
        In a crack in the stone floor,
        impossibly, something green grows.
        
        A tiny seed, sprouting against all odds.
        Life, finding a way.
        
        [Gained: Seed of Tomorrow]
        """,
        
        'echo_of_laughter': """
        You hear it before you see it:
        The sound of your own laughter, echoing.
        
        It's been so long. Too long.
        The sound crystallizes before you.
        
        [Gained: Echo of Laughter]
        """,
        
        'piece_of_self': """
        Something familiar lies in the corner.
        A fragment that feels like... you.
        
        A piece of yourself you didn't realize was missing
        until you found it again.
        
        [Gained: Piece of Self]
        """,
        
        'courage_token': """
        A small token sits on the ground,
        warm to the touch, humming with quiet energy.
        
        It reminds you of a time you spoke up,
        despite the fear, despite the risk.
        
        Your voice matters.
        
        [Gained: Courage Token]
        """,
        
        'compass_of_purpose': """
        A compass, its needle spinning wildly
        until you pick it up. Then it settles,
        pointing not north but toward... something else.
        
        Direction. Purpose. Meaning.
        
        [Gained: Compass of Purpose]
        """,
        
        'forgiveness_feather': """
        A feather, impossibly light, that seems to
        lift the weight from your shoulders as you hold it.
        
        Not all burdens need to be carried forever.
        Some can be released, set free.
        
        [Gained: Forgiveness Feather]
        """
    }
    
    MIRROR_REFLECTIONS = {
        'rock_bottom': """
        You stand before the mirror.
        
        The reflection is hard to look at - 
        a hunched figure, eyes downcast, 
        shoulders bearing invisible weight.
        
        But you force yourself to look anyway.
        That's courage, even if you don't recognize it yet.
        """,
        
        'struggle': """
        The mirror shows someone fighting.
        
        Your reflection is battle-worn, exhausted,
        but standing. Still standing.
        
        There's a spark in your eyes that wasn't there before.
        Small, but undeniably present.
        """,
        
        'realization': """
        The mirror reflects someone in transformation.
        
        Parts of you are familiar, others strange and new.
        The scars are still there, but they're beginning to look
        less like wounds and more like a map of your journey.
        
        You're changing. Growing.
        """,
        
        'growth': """
        Your reflection surprises you.
        
        The person in the mirror stands straighter,
        eyes forward, meeting your gaze with steady clarity.
        
        The burdens haven't disappeared, but you've grown
        strong enough to carry them with dignity.
        
        You recognize yourself again.
        """,
        
        'glory': """
        The mirror shows you as you are.
        
        Not perfect. Not without pain or doubt or fear.
        But whole. Integrated. The darkness and light
        in balance, each with purpose, each with value.
        
        You see yourself with compassion.
        And that makes all the difference.
        """
    }
    
    # Phase-specific NPC encounters
    NPC_ENCOUNTERS = {
        'rock_bottom': {
            'therapist': {
                'greeting': """
                A figure sits nearby, calm and attentive.
                Something about their presence feels safe.
                
                "I've been waiting for you," they say quietly.
                "Would you like to talk about what you're carrying?"
                """,
                
                'conversations': [
                    """
                    "The weight you carry isn't your fault," they say,
                    "but healing is your responsibility. No one else
                    can do that work for you."
                    
                    The words sting, but you recognize their truth.
                    """,
                    
                    """
                    "Right now, you're surviving," they observe.
                    "And that's enough. Sometimes surviving is
                    the bravest thing we can do."
                    
                    Something in your chest loosens at the permission
                    to simply exist for now.
                    """,
                    
                    """
                    "Depression lies," they tell you. "It says things
                    will always feel this way. That you've always felt
                    this way. Neither is true."
                    
                    You want to believe them, even if you can't yet.
                    """
                ]
            },
            
            'loved_one': {
                'greeting': """
                Someone familiar waits ahead. Someone who knew you
                before the darkness, who saw you as you were.
                
                Their eyes shine with concern when they see you.
                No judgment, just worry.
                
                "I've been looking for you," they say.
                """,
                
                'conversations': [
                    """
                    "I don't know what to say," they admit. "I can see
                    you're hurting. I can't fix it. But I'm here."
                    
                    Their honesty is its own kind of comfort.
                    """,
                    
                    """
                    They sit with you in silence. Not trying to fill it
                    with platitudes or solutions. Just being present
                    in this moment, in this darkness.
                    
                    It doesn't fix anything. But it helps.
                    """,
                    
                    """
                    "I'm not going anywhere," they say firmly.
                    "No matter how long this takes. No matter how
                    many times you push me away."
                    
                    You don't believe them yet. But a tiny part of you wants to.
                    """
                ]
            },
            
            'stranger': {
                'greeting': """
                A traveler sits nearby, their face etched with
                the same exhaustion you feel in your bones.
                
                They nod in recognition when they see you.
                
                "Rough journey, isn't it?" they say simply.
                """,
                
                'conversations': [
                    """
                    "I was where you are," they tell you. "Maybe worse.
                    I didn't want to be alive anymore."
                    
                    They say it matter-of-factly, without drama.
                    
                    "But I kept going, one minute at a time. And eventually
                    those minutes became hours. Then days."
                    """,
                    
                    """
                    "The thing about rock bottom," they say, "is that it's
                    solid ground. You can't fall any further."
                    
                    They smile faintly.
                    
                    "And that means there's only one direction left to go."
                    """,
                    
                    """
                    "No one really talks about how physical depression is,"
                    they observe. "How it lives in your body. How it aches."
                    
                    You nod, surprised by their understanding.
                    
                    "Be gentle with yourself. Your body is fighting a war."
                    """
                ]
            }
        },
        
        'struggle': {
            'therapist': {
                'greeting': """
                The therapist looks up as you enter, eyes warm with recognition.
                
                "You're moving," they observe. "That's significant.
                What's changed since we last spoke?"
                """,
                
                'conversations': [
                    """
                    "What would you say to a friend who was going through
                    what you're experiencing?" they ask.
                    
                    You consider this. You'd be kind, understanding, patient.
                    Why is it so hard to give yourself the same grace?
                    """,
                    
                    """
                    "Progress isn't linear," they remind you. "There will be
                    setbacks. Days when it feels like you've lost ground.
                    That's part of the journey, not a detour from it."
                    
                    You nod, something lightening in your chest.
                    """,
                    
                    """
                    "You're starting to question the voices in your head,"
                    they observe. "That's crucial. Those thoughts aren't facts.
                    They're just thoughts."
                    
                    The distinction feels important, even if you don't fully grasp it yet.
                    """
                ]
            },
            
            'loved_one': {
                'greeting': """
                They look up as you approach, their face brightening.
                
                "I can see something's different," they say.
                "There's a spark in you that wasn't there before."
                """,
                
                'conversations': [
                    """
                    "I know it's been hard," they say, taking your hand.
                    "I can't pretend to understand completely. But I'm here.
                    I've always been here."
                    
                    You hadn't realized how much you needed to hear that.
                    """,
                    
                    """
                    "Remember when we..." they start, and share a memory
                    that makes you both laugh. It feels rusty, unfamiliar.
                    
                    But good. It feels good.
                    """,
                    
                    """
                    "I've missed you," they say simply. "Not who you used to be.
                    Just... you. However you are."
                    
                    The acceptance in their voice makes your eyes sting.
                    """
                ]
            },
            
            'stranger': {
                'greeting': """
                The traveler looks different somehow. Still weary,
                but with purpose in their movements.
                
                "Still here, huh?" they say with a small smile.
                "Good. That's the first victory."
                """,
                
                'conversations': [
                    """
                    "The hardest part for me," they say, "was starting to hope again.
                    Because hope means risking disappointment."
                    
                    They look at you steadily.
                    
                    "But a life without hope isn't really living. It's just existing."
                    """,
                    
                    """
                    They show you a small tattoo on their wrist. A semicolon.
                    
                    "It means my story isn't over," they explain. "That I chose
                    to continue when I could have ended my sentence."
                    
                    You understand the metaphor immediately.
                    """,
                    
                    """
                    "I still have bad days," they admit. "Days when the darkness
                    comes back. But now I know they're just days. Not my whole life."
                    
                    The distinction feels important. Profound, even.
                    """
                ]
            }
        },
        
        'realization': {
            'therapist': {
                'greeting': """
                The therapist smiles as you enter, noting the change in your posture.
                
                "You're seeing things more clearly now," they observe.
                "Tell me what you've discovered about yourself."
                """,
                
                'conversations': [
                    """
                    "What parts of yourself are you reclaiming?" they ask.
                    
                    It's a question you couldn't have answered before.
                    But now images come: your creativity, your empathy,
                    your capacity for joy. Things the darkness dimmed but
                    couldn't extinguish.
                    """,
                    
                    """
                    "You're starting to see the patterns," they note.
                    "The thoughts that trigger certain feelings. The
                    behaviors that follow. That awareness is powerful."
                    
                    You nod, recognizing the truth in their words.
                    """,
                    
                    """
                    "Who are you beneath the pain?" they ask. "Not who you
                    were before. But who you are now, having experienced what
                    you've experienced?"
                    
                    It's a question that lingers, demanding to be explored.
                    """
                ]
            },
            
            'loved_one': {
                'greeting': """
                They greet you with a genuine smile, noting the change in you.
                
                "You're coming back to yourself," they say.
                "But different. Stronger, somehow."
                """,
                
                'conversations': [
                    """
                    "You're seeing me more clearly now," they observe.
                    "Not just as a savior or a disappointment. But as a person,
                    with my own struggles and strengths."
                    
                    The observation surprises you, but it's true.
                    """,
                    
                    """
                    "I've been thinking about what you said last time," they tell you.
                    "About feeling disconnected from your old passions."
                    
                    They hand you something small - a token related to something
                    you once loved.
                    
                    "Maybe it's time to rediscover them. Or find new ones."
                    """,
                    
                    """
                    "I see you setting boundaries," they say with approval.
                    "It's good. Healthy. Even when those boundaries are with me."
                    
                    Their support of your growing sense of self feels significant.
                    """
                ]
            },
            
            'stranger': {
                'greeting': """
                The traveler sits cross-legged, looking more at peace than before.
                
                "The fog is lifting for you," they observe.
                "You're seeing the landscape more clearly now."
                """,
                
                'conversations': [
                    """
                    "It's strange, isn't it?" they say. "Realizing that the
                    narrative you've been telling yourself isn't the only story.
                    That there are other ways to interpret your life."
                    
                    You nod, understanding exactly what they mean.
                    """,
                    
                    """
                    "For me, the turning point was rage," they tell you.
                    "Rage at what had happened to me. Rage at the time lost."
                    
                    They smile faintly.
                    
                    "It was the first real emotion I'd felt in years. And it led to all the others."
                    """,
                    
                    """
                    "There's this myth," they say, "that healing means going back
                    to who you were before. But that's not how it works."
                    
                    They look at you intently.
                    
                    "You don't go back. You become something new. Something that
                    incorporates the wound, but isn't defined by it."
                    """
                ]
            }
        },
        
        'growth': {
            'therapist': {
                'greeting': """
                The therapist welcomes you with evident pride.
                
                "Look at you," they say warmly. "Standing in your truth.
                Owning your story. What's that been like?"
                """,
                
                'conversations': [
                    """
                    "What have you learned about resilience?" they ask.
                    
                    You consider this. That it's not about never falling.
                    It's about rising again. That it's built through small
                    choices, daily habits, consistent self-compassion.
                    
                    "I've learned it's a practice," you reply. "Not a trait."
                    """,
                    
                    """
                    "How are you nurturing yourself?" they inquire.
                    
                    The question would have confused you once. Self-care
                    seemed like a luxury you didn't deserve.
                    
                    Now you understand it's a necessity. A responsibility.
                    """,
                    
                    """
                    "You're becoming your own therapist," they observe,
                    smiling. "Questioning your thoughts. Challenging your
                    assumptions. Treating yourself with compassion."
                    
                    The realization fills you with quiet pride.
                    """
                ]
            },
            
            'loved_one': {
                'greeting': """
                They meet you with a hug that feels different now -
                not desperate or clingy, but a genuine connection
                between two whole people.
                
                "You look well," they say, meaning it.
                """,
                
                'conversations': [
                    """
                    "Our relationship has changed," they observe.
                    "In a good way. It's more... equal now."
                    
                    You nod, understanding. You're no longer drowning,
                    needing them to save you. You're swimming alongside them.
                    """,
                    
                    """
                    "I want to tell you something," they say. "When you
                    were in your darkest place, you were still a light for me.
                    Your kindness, your insight, your courage. They never left."
                    
                    The perspective shift moves something deep inside you.
                    """,
                    
                    """
                    "I'm proud of you," they say. "Not because you've overcome
                    this. But because of how you've faced it. With integrity.
                    With perseverance. Even with humor, sometimes."
                    
                    The recognition of your journey means more than they know.
                    """
                ]
            },
            
            'stranger': {
                'greeting': """
                The traveler greets you like an old friend, with warmth
                and recognition that goes beyond words.
                
                "You've walked the path," they say with respect.
                "It shows in how you carry yourself."
                """,
                
                'conversations': [
                    """
                    "I had this moment," they tell you, "when I realized
                    I was helping someone else through their darkness.
                    Using what I'd learned in my own journey."
                    
                    Their eyes meet yours meaningfully.
                    
                    "That's when I understood that my suffering hadn't been pointless.
                    It had given me the ability to truly see others. To help."
                    """,
                    
                    """
                    "The paradox," they say thoughtfully, "is that accepting
                    the darkness as part of life makes it less overwhelming."
                    
                    You nod, understanding completely.
                    
                    "When you stop fighting what is, you have more energy
                    to create what could be."
                    """,
                    
                    """
                    "I still have my demons," they admit. "But they're more
                    like difficult coworkers now than dictators. They have
                    opinions. Sometimes useful ones. But I don't have to
                    obey them."
                    
                    The metaphor makes you both laugh with its accuracy.
                    """
                ]
            }
        },
        
        'glory': {
            'therapist': {
                'greeting': """
                The therapist greets you with profound respect,
                one healer recognizing another.
                
                "You've integrated the pieces," they observe.
                "What will you do with your wholeness?"
                """,
                
                'conversations': [
                    """
                    "What will you take from this journey?" they ask.
                    
                    The question feels vast, but your answer comes easily.
                    
                    "Compassion," you say. "For myself. For others walking
                    this path. For the parts of me I once rejected."
                    """,
                    
                    """
                    "You understand now," they say, "that healing isn't a
                    destination. It's a direction. A practice that continues."
                    
                    You nod, no longer needing certainty or completion.
                    
                    "The journey itself is the point," you reply.
                    """,
                    
                    """
                    "Our work together is changing," they observe.
                    "You don't need me the same way anymore."
                    
                    There's pride in their voice, not loss. The pride
                    of a teacher whose student has found their own wisdom.
                    
                    "But I'll be here if you need a reminder," they add.
                    """
                ]
            },
            
            'loved_one': {
                'greeting': """
                They meet you with a gaze of quiet wonder,
                seeing the person you've become.
                
                "You're whole," they say simply.
                "Not fixed. Not perfect. But whole."
                """,
                
                'conversations': [
                    """
                    "I've been thinking about what you said," they tell you,
                    "about grief and gratitude existing together. About how
                    both can be true at the same time."
                    
                    They meet your eyes.
                    
                    "It's changed how I see my own struggles."
                    """,
                    
                    """
                    "Thank you," they say unexpectedly.
                    
                    "For what?" you ask.
                    
                    "For showing me what courage looks like," they reply.
                    "For letting me witness your journey. It's changed me too."
                    """,
                    
                    """
                    "What now?" they ask, not with worry but with curiosity.
                    
                    You consider the question.
                    
                    "Now we live," you say. "With all of it. The beauty and the pain.
                    The certainty and the doubt. All of it."
                    
                    They smile, understanding completely.
                    """
                ]
            },
            
            'stranger': {
                'greeting': """
                The traveler stands as you approach, a lightness
                in their movements that mirrors your own.
                
                "We made it," they say simply, extending a hand.
                """,
                
                'conversations': [
                    """
                    "I'm continuing on tomorrow," they tell you.
                    "There are others who need to hear that survival is possible.
                    That darkness isn't the end of the story."
                    
                    Their purpose resonates with something awakening in you.
                    """,
                    
                    """
                    "What will you do now?" they ask.
                    
                    The question doesn't overwhelm you as it once might have.
                    
                    "Live," you say. "Fully, honestly, vulnerably. And maybe,
                    when the time is right, help someone else find their way."
                    """,
                    
                    """
                    "I never believed in healing," they admit. "Not really.
                    I thought it was something people talked about to make
                    themselves feel better. To create false hope."
                    
                    Their eyes meet yours, filled with wonder.
                    
                    "I was wrong. And I've never been happier to be wrong."
                    """
                ]
            }
        }
    }
    
    HELP_TEXT = """
    CONTROLS:
    • Arrow keys - Move in four directions
    • l - Look around your current location
    • i - Check your inventory
    • t - Take an item (when available)
    • f - Face a demon (when confronted)
    • k - Talk to person (when present)
    • u - Undo your last move
    • s - Save your journey
    • h - Show this help menu
    • x - Examine mirror (when available)
    
    YOUR JOURNEY:
    Navigate the dungeon by moving between rooms.
    Find items to increase Hope and other attributes.
    Face inner demons to reduce your Burden.
    Talk to others for support and insight.
    Discover your own path to healing.
    """
    
    PHASE_TRANSITIONS = {
        'struggle': """
        Something shifts.
        
        The weight is still there, crushing and real.
        But you're moving despite it.
        
        That's... something.
        """,
        
        'realization': """
        You stop in the middle of a dark room.
        
        Something is different. 
        Not the dungeon. You.
        
        For the first time, you see this place clearly.
        These walls aren't prison cells.
        They're parts of yourself.
        
        And parts can be healed.
        """,
        
        'growth': """
        The burden lightens, not because it's gone,
        but because you've grown stronger.
        
        The demons still speak, but their voices
        no longer drown out your own.
        
        You've found something here in the darkness.
        Not salvation. Not escape.
        Something harder. Something real.
        
        Yourself.
        """,
        
        'glory': """
        You stand at the exit of the dungeon.
        
        The same person who entered... and completely different.
        
        The scars remain. They always will.
        The demons still whisper, but quieter now.
        
        You've learned the most important truth:
        
        Rock bottom isn't the end.
        It's a beginning.
        
        And you...
        You chose to begin.
        """
    }
    
    EPILOGUE = """
    The dungeon fades.
    
    You wake up in your bed.
    The ceiling looks the same.
    But you don't.
    
    The journey through your soul's dungeon...
    It wasn't a dream.
    It was the most real thing you've ever done.
    
    Tomorrow will come.
    And for the first time in so long...
    
    You're ready for it.
    
    
    [Thank you for playing]
    [Remember: It's okay to not be okay]
    [But it's also okay to heal]
    """