class Monster:
    """Class used to rename values in the monsters.cr_dict dictionary."""
    def __init__(self, id, name, cr, xp, environment):
        self.id = id
        self.name = name
        self.cr = cr
        self.xp = xp
        self.environment = environment