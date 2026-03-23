"""
https://www.codewars.com/kata/5941c545f5c394fef900000c/python

Create a class called Warrior which calculates and keeps track of their level and skills, and ranks them as the warrior
they've proven to be.

Business Rules:
A warrior starts at level 1 and can progress all the way to 100.
A warrior starts at rank "Pushover" and can progress all the way to "Greatest".
The only acceptable range of rank values is "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite",
"Conqueror", "Champion", "Master", "Greatest".
Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
The experience earned from the battle is relative to what the warrior's current level is compared to the level of the
enemy.
A warrior's experience starts from 100. Each time the warrior's experience increases by another 100, the warrior's level
rises to the next level.
A warrior's experience is cumulative, and does not reset with each rise of level. The only exception is when the warrior
reaches level 100, with which the experience stops at 10000
At every 10 levels, your warrior will reach a new rank tier. (ex. levels 1-9 falls within "Pushover" tier, levels 80-89
fall within "Champion" tier, etc.)
A warrior cannot progress beyond level 100 and rank "Greatest".

Battle Progress Rules & Calculations:
If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return "Invalid level".
Completing a battle against an enemy with the same level as your warrior will be worth 10 experience points.
Completing a battle against an enemy who is one level lower than your warrior will be worth 5 experience points.
Completing a battle against an enemy who is two levels lower or more than your warrior will give 0 experience points.
Completing a battle against an enemy who is one level higher or more than your warrior will accelerate your experience
gaining. The greater the difference between levels, the more experience your warrior will gain. The formula is
20 * diff * diff where diff equals the difference in levels between the enemy and your warrior.
However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot
fight against an enemy that strong and must instead return "You've been defeated".
Every successful battle will also return one of three responses: "Easy fight", "A good fight", "An intense fight".
Return "Easy fight" if your warrior is 2 or more levels higher than your enemy's level. Return "A good fight" if your
warrior is either 1 level higher or equal to your enemy's level. Return "An intense fight" if your warrior's level is
lower than the enemy's level.

Logic Examples:
If a warrior level 1 fights an enemy level 1, they will receive 10 experience points.
If a warrior level 1 fights an enemy level 3, they will receive 80 experience points.
If a warrior level 5 fights an enemy level 4, they will receive 5 experience points.
If a warrior level 3 fights an enemy level 9, they will receive 720 experience points, resulting in the warrior rising
up by at least 7 levels.
If a warrior level 8 fights an enemy level 13, they will receive 0 experience points and return "You've been defeated".
(Remember, difference in rank & enemy level being 5 levels higher or more must be established for this.)
If a warrior level 6 fights an enemy level 2, they will receive 0 experience points.

Training Rules & Calculations:
In addition to earning experience points from battles, warriors can also gain experience points from training.
Training will accept an array of three elements: the description, the experience points your warrior earns, and the
minimum level requirement.
If the warrior's level meets the minimum level requirement, the warrior will receive the experience points from it and
store the description of the training. It should end up returning that description as well.
If the warrior's level does not meet the minimum level requirement, the warrior does not receive the experience points
and description and instead returns "Not strong enough", without any archiving of the result.

Code Examples:
bruce_lee = Warrior()
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
"""


class Warrior:
    RANKS = [
        "Pushover",
        "Novice",
        "Fighter",
        "Warrior",
        "Veteran",
        "Sage",
        "Elite",
        "Conqueror",
        "Champion",
        "Master",
        "Greatest",
    ]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.rank_num = 1
        self.achievements = []

    def set_level_and_experience(self, exp_earned: int):
        self.experience = self.clamp(self.experience + exp_earned, 10000)
        self.level = self.clamp(self.experience // 100, 100)

    def set_rank_and_rank_num(self, level: int):
        self.rank, self.rank_num = self.get_rank_and_rank_num(level)

    # Accepts an array of three elements: The description, the experience points your warrior earns, and the minimum
    # level requirement
    def training(self, arr: list[str | int]) -> str:
        description: str = arr[0]
        exp_earned: int = arr[1]
        min_level_requirement: int = arr[2]

        if self.level < min_level_requirement:
            return "Not strong enough"

        self.achievements.append(description)
        self.set_level_and_experience(exp_earned)
        self.set_rank_and_rank_num(self.level)
        return description

    def battle(self, enemy_level: int) -> str:
        if not 1 <= enemy_level <= 100:
            return "Invalid level"

        enemy_rank_num = self.get_rank_and_rank_num(enemy_level)[1]
        rank_num_diff = enemy_rank_num - self.rank_num
        level_diff = enemy_level - self.level
        exp_earned = 0

        if rank_num_diff >= 1 and level_diff >= 5:
            return "You've been defeated"

        elif level_diff > 0:
            exp_earned += 20 * level_diff * level_diff
            self.set_level_and_experience(exp_earned)
            self.set_rank_and_rank_num(self.level)
            return "An intense fight"

        elif level_diff <= 0:
            level_diff = self.level - enemy_level

            if level_diff == 0:
                exp_earned += 10
                self.set_level_and_experience(exp_earned)
                self.set_rank_and_rank_num(self.level)
                return "A good fight"

            elif level_diff == 1:
                exp_earned += 5
                self.set_level_and_experience(exp_earned)
                self.set_rank_and_rank_num(self.level)
                return "A good fight"

        return "Easy fight"

    def display_stats(self):
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
        print(f"Rank: {self.rank}")
        print(f"Rank Number: {self.rank_num}")
        print(f"Achievements: {self.achievements}")

    # Returns the rank and rank number as a tuple
    @staticmethod
    def get_rank_and_rank_num(level: int) -> tuple[str, int] | str:
        match level:
            case _ if 1 <= level <= 9:
                return Warrior.RANKS[0], 1
            case _ if 10 <= level <= 19:
                return Warrior.RANKS[1], 2
            case _ if 20 <= level <= 29:
                return Warrior.RANKS[2], 3
            case _ if 30 <= level <= 39:
                return Warrior.RANKS[3], 4
            case _ if 40 <= level <= 49:
                return Warrior.RANKS[4], 5
            case _ if 50 <= level <= 59:
                return Warrior.RANKS[5], 6
            case _ if 60 <= level <= 69:
                return Warrior.RANKS[6], 7
            case _ if 70 <= level <= 79:
                return Warrior.RANKS[7], 8
            case _ if 80 <= level <= 89:
                return Warrior.RANKS[8], 9
            case _ if 90 <= level <= 99:
                return Warrior.RANKS[9], 10
            case 100:
                return Warrior.RANKS[10], 11
            case _:
                return "Invalid level: Level should be between 1 and 100 inclusive"

    @staticmethod
    def clamp(value: int, max_value: int) -> int:
        if value > max_value:
            return max_value

        return value


if __name__ == "__main__":
    bruce_lee = Warrior()
    assert bruce_lee.level == 1
    assert bruce_lee.experience == 100
    assert bruce_lee.rank == "Pushover"
    assert bruce_lee.achievements == []
    # bruce_lee.display_stats()
    # print()

    assert (
        bruce_lee.training(["Defeated Chuck Norris", 9000, 1])
        == "Defeated Chuck Norris"
    )
    assert bruce_lee.experience == 9100
    assert bruce_lee.level == 91
    assert bruce_lee.rank == "Master"
    # bruce_lee.display_stats()
    # print()

    assert bruce_lee.battle(-4) == "Invalid level"
    assert bruce_lee.battle(90) == "A good fight"
    assert bruce_lee.experience == 9105
    assert bruce_lee.achievements == ["Defeated Chuck Norris"]
    # bruce_lee.display_stats()
