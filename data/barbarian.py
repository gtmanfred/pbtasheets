import textwrap

this = {
    "name": "barbarian",
    "max_health_modifier": 10,
    "base_damage": "d10",
    "alignment": [
        {
            "type": "Neutral",
            "text": "Teach someone the ways of your people.",
        },
        {
            "type": "Chaotic",
            "text": "Eschew a convention of the civilized world.",
        },
    ],
    "gear": {
        "load": 8,
        "items": [
            {
                "name": "dungeon rations",
                "tags": [
                    {"type": "uses", "num": 5},
                    {"type": "weight", "num": 1},
                ],
            },
            {
                "name": "dagger",
                "tags": [
                    {"type": "hand"},
                    {"type": "weight", "num": 1},
                ],
            },
            {
                "name": "token",
            },
        ],
        "choices": [
            {
                "num": 1,
                "options": [
                    [
                        {
                            "name": "adventuring gear",
                            "tags": [
                                {"type": "uses", "num": 5},
                                {"type": "weight", "num": 1},
                            ],
                        },
                        {
                            "name": "dungeon rations",
                            "tags": [
                                {"type": "uses", "num": 5},
                                {"type": "weight", "num": 1},
                            ],
                        },
                    ],
                    [
                        {
                            "name": "chainmail",
                            "tags": [
                                {"type": "armor", "num": 1},
                                {"type": "worn"},
                                {"type": "weight", "num": 1},
                            ],
                        },
                    ],
                ]
            },
            {
                "num": 1,
                "options": [
                    [
                        {
                            "name": "axe",
                            "tags": [
                                {"type": "close"},
                                {"type": "weight", "num": 1},
                            ],
                        },
                    ],
                    [
                        {
                            "name": "two-handed sword",
                            "tags": [
                                {"type": "close"},
                                {"type": "damage", "num": "+1"},
                                {"type": "weight", "num": 2},
                            ],
                        },
                    ],
                ]
            },
        ],
    },
    "bonds": [
        "{name} is puny and foolish, but amusing to me.",
        "{name}'s ways are strange and confusing.",
        textwrap.dedent("""
            {name} is always getting into trouble - I must protect them
            from themselves.
        """),
        textwrap.dedent("""
            {name} shares my hunger for glory; the earth will tremble at
            our passage.
        """),
    ],
    "moves": [
        {
            "name": "Full Plate and Packing Steel",
            "text": "You ignore the clumsy tag on armor you wear.",
            "type": "simple",
            "move": "choice",
        },
        {
            "name": "Unencumbered, Unharmed",
            "text": textwrap.dedent("""
                So long as you are below your load and neither wear
                armor nor carry a shield, take +1 armor.
            """),
            "type": "simple",
            "move": "choice",
        },
        {
            "name": "Outsider (Race)",
            "text": textwrap.dedent("""
                You may be elf, dwarf, halfling, or human, but you and
                your people are not from around here. At the beginning
                of each session, the GM will ask you something about
                your homeland, why you left, or what you left behind. If
                you answer them, mark XP.
            """),
            "type": "race",
            "move": "starting",
        },
        {
            "name": "The Upper Hand",
            "text": textwrap.dedent("""
                You take +1 ongoing to last breath rolls. When you take
                your last breath, on a 7–9 you make an offer to Death in
                return for your life. If Death accepts he will return you
                to life. If not, you die.
            """),
            "type": "simple",
            "move": "starting"
        },
        {
            "name": "What Are You Waiting For?",
            "text": textwrap.dedent("""
                When you cry out a challenge to your enemies, roll+Con.
                • On a 10+ they treat you as the most obvious threat to be
                dealt with and ignore your companions, take +2 damage
                ongoing against them.
                • On a 7–9 only a few (the weakest or most foolhardy among
                them) fall prey to your taunting.
            """),
            "type": "simple",
            "move": "starting",
        },
        {
            "name": "Herculean Appetites",
            "text": textwrap.dedent("""
                Others may content themselves with just a taste of wine, or
                dominion over a servant or two, but you want more. Choose
                two appetites. While pursuing one of your appetites if you
                would roll for a move, instead of rolling 2d6 you roll
                1d6+1d8. If the d6 is the higher die of the pair, the GM
                will also introduce a complication or danger that comes
                about due to your heedless pursuits.
            """),
            "type": "choice",
            "move": "starting",
            "choices": [
                "Pure destruction Power over others",
                "Mortal pleasures",
                "Conquest",
                "Riches and property",
                "Fame and glory",
            ],
            "num": 2
        },
        {
            "name": "Musclebound",
            "text": "While you wield a weapon it gains the forceful and messy tags.",
            "type": "simple",
            "move": "starting",
        },
        {
            "name": "Still Hungry",
            "text": "Choose an additional appetite",
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Appetite For Destruction",
            "text": textwrap.dedent("""
                Take a move from the Fighter, Bard, or Thief class list.
                You may not take multiclass moves from those classes.
            """),
            "type": "class",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "My Love For You Is Like A Truck",
            "text": textwrap.dedent("""
                When you perform a feat of strength, name someone present whom you have
                impressed and take +1 forward to parley with them.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "What is Best in Life",
            "text": textwrap.dedent("""
                At the end of a session, if during this session you have
                crushed your enemies, seen them driven before you, or
                have heard the lamentations of their kinfolk mark XP.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Wide-Wanderer",
            "text": textwrap.dedent("""
                You’ve travelled the wide world over. When you arrive
                someplace ask the GM about any important traditions,
                rituals, and so on, they’ll tell you what you need to
                know.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Usurper",
            "text": textwrap.dedent("""
                When you prove yourself superior to a person in power,
                take +1 forward with their followers, underlings, and
                hangers on.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Khan Of Khans",
            "text": textwrap.dedent("""
                Your hirelings always accept the gratuitous fulfillment
                of one of your appetites as payment.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Samson",
            "text": textwrap.dedent("""
                You may take a debility to immediately break free of any
                physical or mental restraint.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Smash!",
            "text": textwrap.dedent("""
                When you Hack & Slash, on a 12+ deal your damage and
                choose something physical your target has (a weapon,
                their position, a limb): they lose it.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Indestructible Hunger",
            "text": textwrap.dedent("""
                When you take damage you can choose to take -1 ongoing
                until you sate one of your appetites instead of taking
                the damage.  If you already have this penalty you cannot
                choose this option.
            """),
            "type": "",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "",
            "text": textwrap.dedent("""
            """),
            "type": "",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "Eye For Weakness",
            "text": textwrap.dedent("""
                When you Discern Realities add "What here is weak or
                vulnerable?" to the list of questions you can ask.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "On The Move",
            "text": textwrap.dedent("""
                When you defy a danger caused by movement (maybe falling off a
                narrow bridge or rushing past an armed guard) take +1.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 2,
        },
        {
            "name": "A Good Day to Die",
            "text": textwrap.dedent("""
                As long as you have less than your CON in current HP (or 1,
                whichever is higher) take +1 ongoing.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "Kill ‘Em All",
            "text": textwrap.dedent("""
                Take another move fromt he Fighter, Bard, or Thief class list.
                You may not take multiclass moves from those classes.
            """),
            "type": "prereq",
            "move": "advanced",
            "level": 6,
            "requires": "Appetite for Destruction",
        },
        {
            "name": "War Cry",
            "text": textwrap.dedent("""
                When you enter the battle with a show of force, roll +CHA.
                • On a 10+ both
                • on a 7-9 one or the other.
                
                - Your allies are rallied and take +1 forward.
                - Your enemies feel fear and act accordingly (avoiding you,
                  hiding, attacking with fear-driven abandon)
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "Mark of Might",
            "text": textwrap.dedent("""
                When you take this move and spend some uninterrupted time
                reflecting on your past glories, you may mark yourself with a
                symbol of your power (a long braid tied with bells, ritual scars
                or tattoos, etc.) Any intelligent mortal creature who sees this
                symbol knows instinctively that you are a force to be reckoned
                with and treats you appropriately.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "More! Always More!",
            "text": textwrap.dedent("""
                When you satisfy an appetite to the extreme (destroying
                something unique and significant, gaining enormous fame, riches,
                power, etc.) you may choose to resolve it. Cross it off the list
                and mark XP. While you may pursue that appetite again, you no
                longer feel the burning desire you once did. In its place,
                choose a new appetite from the list or write your own.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "The One Who Knocks",
            "text": textwrap.dedent("""
                When you Defy Danger, on a 12+ you turn the danger back on
                itself, the GM will describe how.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "Healthy Distrust",
            "text": textwrap.dedent("""
                Whenever the unclean magic wielded by mortal men causes you to
                Defy Danger, treat any result of 6- as a 7–9.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
        {
            "name": "For the Blood God",
            "text": textwrap.dedent("""
                You are initiated in the old ways, the ways of sacrifice. Choose
                something your gods (or the ancestor spirits, or your totem,
                etc) value—gold, blood, bones or the like. When you sacrifice
                those things as per your rites and rituals, roll+WIS.
                • On a 10+ the GM will grant you insight into your current
                  trouble or a boon to help you.
                • On a 7-9 the sacrifice is not enough and your gods take of
                  your flesh as well, but still grant you some insight or boon.
                • On a miss, you earn the ire of the fickle spirits.
            """),
            "type": "simple",
            "move": "advanced",
            "level": 6,
        },
    ],
}
