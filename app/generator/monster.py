from typing import List

class Monster:
    """Class used to rename values in the monsters.cr_dict dictionary."""
    def __init__(self, id, name: str, cr: float, xp: float, environment: List):
        self.id = id
        self.name = name
        self.cr = cr
        self.xp = xp
        self.environment = environment