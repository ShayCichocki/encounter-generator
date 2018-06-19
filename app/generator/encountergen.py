import random
import json
from typing import List, Dict

class EncounterGen:
    def __init__(self, monster_dict: Dict, encounter_difficulty: Dict):
        self.monster_dict = monster_dict
        self.encounter_difficulty = encounter_difficulty

    def generate_encounter(self, encounter_data:List):
        xp_budget = self.get_xp_budget(encounter_data['difficulty'], encounter_data['characters'])
        xp_per_monster = self.xp_list_gen(xp_budget)
        output_monster = self.rnd_select_monster(xp_per_monster)

        return {
            'xpBudget': xp_budget,
            'output_monster': output_monster.serialize()
        }

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

    def rnd_select_monster(self, xp):
        nearest_monster_xp = min(self.list_monster_xp(xp), key=lambda x: abs(x - xp))
        monster_selections = [key for key in self.monster_dict if self.monster_dict[key].xp == nearest_monster_xp]
        output_monster = random.choice(monster_selections)
        return self.monster_dict[output_monster]

    def list_monster_xp(self, xp):
        monster_xp_list = []
        for key in self.monster_dict:
            if self.monster_dict[key].xp <= int(xp):
                monster_xp_list.append(self.monster_dict[key].xp)
        return monster_xp_list