import random
import json
from typing import List, Dict

class EncounterGen:
    def __init__(self, monster_dict: Dict):
        self.monster_dict = monster_dict
        self.encounter_difficulty = json.load(open("../data/encounter-difficulty.json", "r"))

    def xp_list_gen(self, xp):
        xp_factors = [i for i in range(10, xp + 1) if xp % i == 0]
        random_gen_factor = 0
        while random_gen_factor == 0 or (xp / random_gen_factor) > 20:
            random_gen_factor = random.choice(xp_factors)
        return random_gen_factor

    def get_xp_budget(self, difficulty: str, characters: List):
        total_xp = 0
        for i in characters:
            total_xp = total_xp + self.encounter_difficulty[difficulty][i - 1]
        return total_xp

