import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    def calculate_score(cards):
        ''' Take a list of cards os input and return the score calculated from it '''
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return 'Draw'
        elif computer_score == 0:
            return 'you lose, opponent has Black Jack'
        elif user_score == 0:
            return 'you win with a blackjack'
        elif user_score > 21:
            return 'bust computer wins'
        elif computer_score > 21:
            return 'bust user wins'
        else:
            if user_score > computer_score:
                return 'user wins'
            else:
                return 'computer wins'

    for d in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' your cards {user_cards} and {user_score}')
        print(f" computer's first card [{computer_cards[0]}, ?]")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_another_card = input('Do you want to draw another card type "y" for yes and "n" for no: ')
            if draw_another_card == "y":
                user_cards.append(deal_card())
                computer_cards.append(deal_card())

            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand {user_cards} and score: {user_score}")
    print(f" Your final hand {computer_cards} and score: {computer_score}")
    print(compare(user_score, computer_score))


while input('Do you want to play BlackJack type "y" to play and "n" to quit: ') == 'y':
    os.system('cls')
    play_game()
