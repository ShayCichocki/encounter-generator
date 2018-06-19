from typing import List
from json import JSONEncoder

class Monster(object):
    """Class used to rename values in the monsters.cr_dict dictionary."""
    def __init__(self, id: int, name: str, cr: float, xp: float, environment: List):
        self.id = id
        self.name = str(name)
        self.cr = float(cr)
        self.xp = float(xp)
        self.environment = environment

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cr': self.cr,
            'xp': self.xp,
            'environment': self.environment
        }