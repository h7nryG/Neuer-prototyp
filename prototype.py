import content
"""
Ein Dictionary, das die einzelnen Abschnitte des Kapitels enthält.
Jeder Abschnitt enthält:
Dieses Dictionary soll den Ablauf von dem Ablauf Pfad für den zweiten Prototyp (Schritt 2) sein

- content: den Text des Abschnitts
- options: die möglichen nächsten Abschnitte
- text_options: die Textoptionen für den Benutzer
"""
chapter = {
    'abs1': {
        'content': content.abs1,
        'options': {
            '1': 'abs72'
        },
        'text_options': {
            '1': 'Versuche zu fliehen'
        }
    },
    'abs72': {
        'content': content.abs72,
        'options': {
            '1': 'abs76'
        },
        'text_options': {
            '1': 'Fliehe durch den Gang',
        }
    },
    'abs76': {
        'content': content.abs76,
        'options': {
            '1': 'abs55',
        },
        'text_options': {
            '1': 'Fliehe durch die Tür'
        }
    },
    'abs55': {
        'content': content.abs55,
        'options': {
            '1': 'abs92',
        },
        'text_options': {
            '1': 'Fliehe durch das Fenster'
        }
    },
    'abs92': {
        'content': content.abs92,
        'options': {
            '1': 'abs35',

        },
        'text_options': {
            '1': 'Fliehe durch den Hof',
        }
    },
    'abs35': {
        'content': content.abs35,
        'options': {
            '1': 'abs40',
            '2': 'abs97'
        },
        'text_options': {
            '1': 'Fliehe durch den Tempel',
            '2': 'Verstecke dich'
        }
    },
    'abs97': {
        'content': content.abs97,
        'options': {
            '1': 'abs71',
            '2': 'abs42',
            '3': 'abs40',
        },
        'text_options': {
            '1': 'Kapitel 71',
            '2': 'Kapitel 42',
            '3': 'Kapitel 40',
        }
    },
    'abs40': {
        'content': content.abs40,
        'options': {
            '1': 'abs71',
        },
        'text_options': {
            '1': 'Verstecke dich'
        }
    },
    'abs42': {
        'content': content.abs42,
        'options': {
            '1': 'abs77',
        },
        'text_options': {
            '1': 'Kapitel 77'
        }
    },
    'abs71': {
        'content': content.abs71,
        'options': {
            '1': 'abs90',
        },
        'text_options': {
            '1': 'Untersuche die Verletzung'
        }
    },
    'abs77': {
        'content': content.abs77,
        'options': {
            '1': 'abs7',
        },
        'text_options': {
            '1': 'Untersuche die Verletzung'
        }
    },
    'abs7': {
        'content': content.abs7,
        'options': {
            '1': 'abs90',
        },
        'text_options': {
            '1': 'Untersuche die Verletzung'
        }
    },
    'abs90': {
        'content': content.abs90,
        'options': {
            '1': 'abs65',
        },
        'text_options': {
            '1': 'Untersuche das Brandmal'
        }
    },
    'abs65': {
        'content': content.abs65,
        'options': {
            '1': 'abs11'
        },
        'text_options': {
            '1': 'Fliehe durch den Tempel'
        }
    },
    'abs11': {
        'content': content.abs11,
        'options': {
            '1': 'abs60',
        },
        'text_options': {
            '1': 'Fliehe zum Tempel'
        }
    },
    'abs60': {
        'content': content.abs60,
        'options': {
            '1': 'abs16'
        },
        'text_options': {
            '1': 'Betrete den Tempel'
        }
    },
    'abs16': {
        'content': content.abs16,
        'options': {
            '1': 'abs89',
        },
        'text_options':{
            '1': 'Verstecke dich',
        }
    },
    'abs89': {
        'content': content.abs89,
        'options': {
            '1': 'abs58',
        },
        'text_options': {
            '1': 'Untersuche die Orgel',
        }
    },
    'abs58': {
        'content': content.abs58,
        'options': {
            '1': 'abs33',
        },
        'text_options': {
            '1': 'Untersuche die Orgel'
        }
    },
    'abs33': {
        'content': content.abs33,
        'options': {
            '1': 'abs13'
        },
        'text_options': {
            '1': 'Untersuche den Bolzen',
        }
    },
    'abs13': {
        'content': content.abs13,
        'options': {
            '1': 'abs38',
        },
        'text_options': {
            '1': 'Untersuche die Särge'
        }
    },
    'abs38': {
        'content': content.abs38,
        'options': {
            '1': 'abs100'
        },
        'text_options': {
            '1': 'Stelle dich dem Feind'
        }
    },
    'abs100': {
        'content': content.abs100,
        'options': {
            '1': 'abs1',
        },
        'text_options': {
            '1': 'Beginne von vorne',
        }
    }
}