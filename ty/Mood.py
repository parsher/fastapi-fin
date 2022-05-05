from enum import Enum

class Mood(str, Enum):
    sad = 'sad'
    grin = 'grin'
    smile = 'smile'
    evil = 'evil'
    frustrated = 'frustrated'
    shocked = 'shocked'
    baffled = 'baffled'
    crying = 'crying'