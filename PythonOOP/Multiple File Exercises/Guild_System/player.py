# - player_info()
# o Returns the player's information, including their skills, in this format:
#
# "Name: {player_name}
# Guild: {guild_name}
# HP: {hp}
# MP: {mp}
# ==={skill_name_1} - {skill_mana_cost}
# ==={skill_name_2} - {skill_mana_cost}
# ...
# ==={skill_name_N} - {skill_mana_cost}"

class Player:
    def __init__(self, name: str, hp: int, mp: int, ):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        skills_str = [f"=== {skill_name} - {mana_cost}" for skill_name, mana_cost in self.skills.items()]
        return (
                f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n" +
                '\n'.join(skills_str)
        )

