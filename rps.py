from random import randint
from sys import exit


def computer_choice():
    choice = randint(1, 3)
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'scissors'


def player_choice():
    print "Enter your choice of rock, paper or scissors. Type exit to finish."
    choice = raw_input('>>')

    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return choice
    elif choice == 'exit':
        exit(0)
    else:
        print "I'm sorry but I don't understand that."


def play_round(computer, user):
    if computer == user:
        print "Draw!"
        return 'draw'
    elif computer == 'rock' and user == 'paper':
        print "Computer played rock, you win!"
        return 'win'
    elif computer == 'rock' and user == 'scissors':
        print "Computer played rock and wins!"
        return 'lose'
    elif computer == 'paper' and user == 'rock':
        print "Computer played paper and wins!"
        return 'lose'
    elif computer == 'paper' and user == 'scissors':
        print "Computer played paper, you win!"
        return 'win'
    elif computer == 'scissors' and user == 'rock':
        print "Computer played scissors, you win!"
        return 'win'
    elif computer == 'scissors' and user == 'paper':
        print "Computer played scissors and wins!"
        print 'lose'


def main():
    player_score = 0
    computer_score = 0
    while True:
        result = play_round(computer_choice(), player_choice())
        if result == 'win':
            player_score += 1
        elif result == 'lose':
            computer_score += 1
        print "Your score is %s " % player_score
        print "My score is %s " % computer_score


main()