import random


def get_winner():
    results = {}
    winner = ['', 0]

    for i in range(len(player_names)):
        name = player_names[i]
        total_score = game_result[i].get(9)[-1]
        results[name] = game_result[i]
        if winner[1] < total_score:
            winner[0] = name
            winner[1] = total_score

    return winner, results


class Bowling:

    spare_bonus = 5
    strike_bonus = 10
    all_pins = 10

    def __init__(self, *name):
        self.total_players = len(name)
        self.names = name
        self.result = {}
        for i in range(self.total_players):
            self.result[i] = {}

    def random_number_generator(self, start, end):
        return random.randrange(start, end)

    def get_names(self):
        return self.names

    def got_spare(self, previous_total):
        return previous_total + Bowling.all_pins + Bowling.spare_bonus

    def got_strike(self, previous_total):
        return previous_total + Bowling.all_pins + Bowling.strike_bonus

    def start_game(self):
        # Total rounds
        for i in range(10):
            # Total number of players
            for j in range(self.total_players):
                self.result[j][i] = []
                # Random_number_generator
                roll_number_1 = self.random_number_generator(0, 11)

                # if there is a strike but not the last round
                if roll_number_1 == 10 and i != 9:
                    self.result[j][i].append(10)
                    self.result[j][i].append(0)
                    if i != 0:
                        self.result[j][i].append(self.got_strike(self.result[j][i - 1][2]))
                    else:
                        self.result[j][i].append(self.got_strike(0))

                # if there is a strike and the last round
                if roll_number_1 == 10 and i == 9:
                    self.result[j][i].append(10)
                    self.result[j][i].append(0)
                    roll_number_3 = self.random_number_generator(0, 11)
                    self.result[j][i].append(roll_number_3)
                    self.result[j][i].append(self.got_strike(self.result[j][i - 1][2])+roll_number_3)

                # if it isn't a strike
                if roll_number_1 != 10:
                    self.result[j][i].append(roll_number_1)
                    roll_number_2 = self.random_number_generator(0, 11-roll_number_1)
                    self.result[j][i].append(roll_number_2)

                    # if it is a spare and not the last round
                    if roll_number_1 + roll_number_2 == 10 and i != 9:
                        if i != 0:
                            self.result[j][i].append(self.got_spare(self.result[j][i - 1][2]))
                        else:
                            self.result[j][i].append(self.got_spare(0))

                    # if it is a spare and the last round
                    if roll_number_1 + roll_number_2 == 10 and i == 9:
                        roll_number_3 = self.random_number_generator(0, 11)
                        self.result[j][i].append(roll_number_3)
                        self.result[j][i].append(self.got_spare(self.result[j][i - 1][2]) + roll_number_3)

                    # if it is not a spare nor a strike
                    elif roll_number_1 + roll_number_2 != 10:
                        if i != 0:
                            self.result[j][i].append(roll_number_2 + roll_number_1 + self.result[j][i - 1][2])
                        else:
                            self.result[j][i].append(roll_number_2 + roll_number_1)

        return self.result


if __name__ == '__main__':
    game = Bowling("Abc", "Pqr", "Xyz")
    game_result = game.start_game()
    player_names = game.get_names()

    winner, results = get_winner()

    print("Scoreboard - ")
    for i, j in results.items():
        print(i + " -> " + str(j))
    print("Winner of the game is " + winner[0] + ". With Score of " + str(winner[1]))
