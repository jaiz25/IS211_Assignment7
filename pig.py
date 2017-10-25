#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 7 for IS211"""


import random


class Game:

    players = []
    total = []
    total2 = []
    dice = 0

    def __init__(self, players):
        self.players = list(players)
        self.running = False

    def decision(self):
        self.running = True
        total = self.total
        total2 = self.total2
        dice = self.dice
        current = self.players

        while self.running:

            ask = raw_input("What do you want to do " + str(current[0]) + " ? ")
            if ask == 'r':
                dice = random.randint(1, 6)
                if dice >= 2:
                    total.append(dice)
                    print "You rolled " + str(dice) + ". Your total is " + str(sum(total))

                elif dice == 1:
                    total.append(0)
                    print "You rolled " + str(dice) + ". Opponent's turn."
                    print "Your total is " + str(sum(total) * 0)
                    self.players.append(sum(total) * 0)
                    break

            elif ask == 'h':
                print "Holding: your current total is " + str(sum(total))
                self.players.append(sum(total))
                break

        while self.running:

            ask = raw_input("What do you want to do " + str(current[1]) + " ? ")
            if ask == 'r':
                dice = random.randint(1, 6)
                if dice >= 2:
                    total2.append(dice)
                    print "You rolled " + str(dice) + ". Your total is " + str(sum(total2))

                elif dice == 1:
                    print "You rolled " + str(dice) + ". Opponent's turn."
                    print "Your total is " + str(sum(total2) * 0)
                    total2.append(0)
                    self.players.append(sum(total2) * 0)
                    return self.winner()
                    break

            elif ask == 'h':
                print "Holding: your current total is " + str(sum(total2))
                self.players.append(sum(total2))
                return self.winner()

    def winner(self):

        if self.players[2] >= 20:
            print str(self.players[0]) + " wins!!!"
        elif self.players[3] >= 20:
            print str(self.players[1]) + " wins!!!"
        elif sum(self.total) == 0 or sum(self.total) < 20:
            self.decision()
        elif sum(self.total2) == 0 or sum(self.total2) < 20:
            self.decision()


class NewGame:

    question = raw_input("Do you want to play? ")

    def __init__(self):

        self.yes = 'yes'
        self.no = 'no'

    def play(self):
        self.question
        if self.question == self.yes:
            Game(['player1', 'player2']).decision()
        else:
            print "Goodbye!"


def main():

    new_game = NewGame()
    print new_game.play()


if __name__ == '__main__':
    main()
