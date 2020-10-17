"""
@Author: ZHANG Mofan
"""


import random
import collections
from domino_class import Domino
from multi_sum import two_sum, three_sum
from exception import *


class Solitaire:
    # base class
    def __init__(self):
        self._deck = [Domino(j, i) for i in range(7) for j in range(i+1)]
        self._hand = []

    def shuffle_with_random_seed(self, random_seed):
        random.seed(random_seed)
        random.shuffle(self._deck)

    def shuffle(self):
        for i in range(self.check_nbr_deck()-1, 0, -1):
            p = random.randrange(0, i+1)
            self._deck[i], self._deck[p] = self._deck[p], self._deck[i]

    def check_nbr_deck(self):
        return len(self._deck)

    def check_nbr_hand(self):
        return len(self._hand)

    def draw_domino(self, nbr_max=7):
        """ draw dominoes from the top of the deck (from the end of the deck list)

        Parameters
        ----------
        nbr_max

        Returns
        -------

        """
        nbr_in_deck = self.check_nbr_deck()
        nbr_in_hand = self.check_nbr_hand()
        nbr_to_draw = max(nbr_max - nbr_in_hand, 0)
        print(f"Number of dominoes to draw: {nbr_to_draw}.")
        while (nbr_to_draw > 0) and (nbr_in_deck > 0):
            # add one domino to hand
            self._hand.append(self._deck.pop())
            nbr_to_draw -= 1
            nbr_in_deck -= 1

    def pull_out_domino(self, idx_to_delete):
        """ pull out dominoes from hand

        Parameters
        ----------
        idx_to_delete

        Returns
        -------

        """
        if self.check_points(map(self._hand.__getitem__, idx_to_delete)):
            print("Valid input. Dominoes chosen pulled out!")
            self._hand = [self._hand[i] for i in range(self.check_nbr_hand()) if i not in idx_to_delete]
        else:
            raise PointsNotTwelveException

    @staticmethod
    def check_points(dominoes):
        # check whether sum of dots is equal to 12
        total_points = 0
        for domino in dominoes:
            total_points += domino.point
        if total_points == 12:
            return True
        else:
            return False

    def show_domino_in_hand(self):
        idx = 1

        for domino in self._hand:
            index_part = [' '*3]*2 + [f'({idx})'] + [' '*3]*2
            domino_str = domino.__str__()
            str_list = domino_str.split("\n")

            for i in range(len(str_list)):
                print(index_part[i] + str_list[i])

            idx += 1

    def is_game_won(self):
        # check whether the player won
        if (self.check_nbr_deck() == 0) and (self.check_nbr_hand() == 0):
            return True
        else:
            return False

    def is_game_lost(self):
        # 2 sum, 3 sum, 4 sum (3 sum), 5 sum (2 sum), 6 sum (check 1 domino)
        points_list = [domino.point for domino in self._hand]
        total_points = sum(points_list)

        # first of all, check if the domino of 12 points is in hand
        # and then check the sum of every 6 dominoes
        for point in points_list:
            if point == 12:
                return False  # the game can continue
            if (total_points - point) == 12:
                return False

        # check the sum of every 2 dominoes
        # and check the sum of every 5 dominoes
        if two_sum(points_list, 12) or two_sum(points_list, total_points-12):
            return False

        # check the sum of every 3 dominoes
        # and check the sum of every 4 dominoes
        if three_sum(points_list, 12) or three_sum(points_list, total_points-12):
            return False

        return True  # the game can not continue


class InteractiveSolitaire(Solitaire):
    def __init__(self):
        super().__init__()

    def choose_shuffle_method(self):
        shuffle_method = int(\
            input("Shuffle the deck. Please choose the method to use (1 for random shuffling, 2 for shuffling with seed): "))
        if shuffle_method == 1:
            self.shuffle()
            print("Shuffling done.")
        elif shuffle_method == 2:
            random_seed = input("Please enter an integer for the random seed: ")
            self.shuffle_with_random_seed(random_seed)
            print("Shuffling done.")
        else:
            print("No valid input. Game will begin without shuffling!")

    def request_input_string(self):
        nbr_in_hand = self.check_nbr_hand()
        while True:
            try:
                idx_str = input("Please input a string of number to select the dominoes to pull out: ")
                idx_to_delete = [int(i)-1 for i in idx_str]

                try:
                    # check if there are duplicate numbers in idx_to_delete
                    duplicate_idx_list = [idx+1 for idx, count in collections.Counter(idx_to_delete).items() if count > 1]
                    if duplicate_idx_list:
                        raise DuplicateIndexException(duplicate_idx_list)
                except DuplicateIndexException as e:
                    print(e.__str__())
                    delete_duplicate_choice = input("Do you want to delete duplicate index and continue [Y/N]?: ")
                    yes_list = {"Y", "y", "Yes", "YES", "yes"}
                    no_list = {"N", "n", "No", "NO", "no"}
                    if delete_duplicate_choice in yes_list:
                        idx_to_delete = list(set(idx_to_delete))
                        print(f"Duplicate index removed. Index of dominoes to pull out: {[idx+1 for idx in idx_to_delete]}. Continue ...")
                    if delete_duplicate_choice in no_list:
                        print("String of numbers abandoned.")
                        continue

                # check whether there is any index out of range
                invalid_idx_list = [idx+1 for idx in idx_to_delete if (idx < 0 or idx > (nbr_in_hand-1))]
                if invalid_idx_list:
                    raise InvalidHandIndexException(invalid_idx_list)

                return idx_to_delete

            except ValueError:
                print("Conversion fails! The input is not a string of integers.")
            except InvalidHandIndexException as e:
                print(e.__str__())

    def turn(self):
        # draw dominoes from the top of the deck
        print("Draw dominoes from the deck to hand.")
        self.draw_domino()

        print(f"Number of dominoes in deck: {self.check_nbr_deck()}; " +
              f"number of dominoes in hand: {self.check_nbr_hand()}.")

        # show dominoes in hand
        print("Show all dominoes in hand: ")
        self.show_domino_in_hand()

        # check whether the game can no longer continue
        if self.is_game_lost():
            print("No more legal move. Defeat!")
            return -1

        while True:
            try:
                # request player to select the dominoes to pull out
                idx_to_delete = self.request_input_string()

                # pull out selected dominoes
                self.pull_out_domino(idx_to_delete)

                break
            except PointsNotTwelveException as e:
                print(e.__str__()+" Please retry!")

        # check whether the player won
        if self.is_game_won():
            print("Victory!")
            return 1
        return

    def play(self):
        # begin a new game
        print("*"*60)
        print("Start a new game.")

        # first, verify that the deck is complete and no domino in hand
        print("Check that the deck is complete and no domino in hand:")
        if (self.check_nbr_deck() != 28) or (self.check_nbr_hand() != 0):
            print("Check failed! Please reinitiate an object of Solitaire class and retry!")
            return

        print("Check passed. Continue the game.")

        # shuffling
        self.choose_shuffle_method()

        # play
        print("Begin playing.")
        turn_nbr = 1

        while True:
            # player not won, continue
            print("-"*60)
            print(f"Turn {turn_nbr}")

            indicator = self.turn()
            if indicator:
                break

            print("Next turn.\n")
            turn_nbr += 1
        return


class AutoPlaySolitaire(Solitaire):
    def __init__(self):
        super().__init__()

    def find_solution_each_turn(self):
        points_list = [domino.point for domino in self._hand]
        res_idx = []

        # if domino whose point is 12 in hand, add it to solution
        if 12 in points_list:
            res_idx.append(points_list.index(12))
            # if domino(0, 0) in hand, add it to solution
            if 0 in points_list:
                res_idx.append(points_list.index(0))
            return res_idx
        # other cases
        # try 2 sum
        idx_2_sum = two_sum(points_list, 12)
        if idx_2_sum:
            res_idx += idx_2_sum
            # if domino(0, 0) in hand, add it to solution
            if 0 in points_list:
                res_idx.append(points_list.index(0))
            return res_idx
        # try 3 sum
        idx_3_sum = three_sum(points_list, 12)
        if idx_3_sum:
            res_idx += idx_3_sum
            # if domino(0, 0) in hand, add it to solution
            if 0 in points_list:
                res_idx.append(points_list.index(0))
            return res_idx

        return res_idx

    def autoplay(self):
        # begin a game

        print("*"*60)
        print("Start a new game.")

        # shuffle
        self.shuffle()

        # play
        turn_nbr = 1
        pull_out_domino_list = []
        while True:
            # player not won, continue
            print("-"*60)
            print(f"Turn {turn_nbr}")
            self.draw_domino()

            self.show_domino_in_hand()

            print("Find automatically a solution ...")
            res_idx = self.find_solution_each_turn()

            if res_idx:
                pull_out_dominoes = [self._hand[i] for i in res_idx]
                print("Dominoes chosen to be pulled out: ")
                for domino in pull_out_dominoes:
                    print(domino.__str__())
                pull_out_domino_list.append((turn_nbr, pull_out_dominoes))

                self.pull_out_domino(res_idx)
            else:
                print("Defeat!")
                break

            if self.is_game_won():
                print("Victory!")
                break

            print("Next turn.\n")
            turn_nbr += 1

"""
game1 = InteractiveSolitaire()
game1.play()

game2 = AutoPlaySolitaire()
game2.autoplay()
"""
