import textwrap

this = {
    "name": "wizard",
    "gear": {
        "load": 7,
        "items": [
            {
                "name": "spellbook",
                "tags": [
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
        "choices": [
            {
                "num": 1,
                "options": [
                    [
                        {
                            "name": "leather armor",
                            "tags": [
                                {"type": "armor", "num": 1},
                                {"type": "weight", "num": 1},
                            ],
                        },
                    ],
                    [
                        {
                            "name": "bag of books",
                            "tags": [
                                {"type": "uses", "num": 5},
                                {"type": "weight", "num": 2},
                            ],
                        },
                        {
                            "name": "healing potions",
                            "tags": [
                                {"type": "quantity", "num": 3},
                                {"type": "weight", "num": 0}
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
                            "name": "dagger",
                            "tags": [
                                {"type": "hand"},
                                {"type": "weight", "num": 1},
                            ],
                        },
                    ],
                    [
                        {
                            "name": "staff",
                            "tags": [
                                {"type": "close"},
                                {"type": "two-handed"},
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
                            "name": "healing potions",
                            "tags": [
                                {"type": "quantity", "num": 1},
                                {"type": "weight", "num": 0},
                            ],
                        },
                    ],
                    [
                        {
                            "name": "antitoxins",
                            "tags": [
                                {"type": "quantity", "num": 3},
                                {"type": "weight", "num": 0},
                            ],
                        },
                    ],
                ]
            },
        ],
    },
    "bonds": [
        textwrap.dedent("""
            {name} will play an important role in the events to come. I
            have foreseen it!
        """),
        "{name} is keeping an important secret from me.",
        textwrap.dedent("""
            {name} is woefully misinformed about the world; I will teach
            them all that I can.
        """),
    ],
}
