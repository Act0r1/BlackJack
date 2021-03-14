from art import logo
import random
import os

print(logo)
print("Hello, it's BlackJack Game by <MrMistake> I hope you enjoy!")
points = [11,2,3,4,5,6,7,8,9,10,10,10,10]
ListOfPossiblePostiveAnswers = ['Yes', 'y', 'YES', 'yes']
ListOfPossibleNegativeAnswers = ['No', 'NO', 'n', 'N']


def deal_card():
    card = random.choice(points)
    return card


def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return'Draw'
    elif computer_score == 0:
        return 'Opponent has a BlackJacjk, you lose('
    elif user_score == 0:
        return 'You has a BlackJack. You won!!!'
    elif user_score > 21:
        return 'Your scores over 21, you lose!'
    elif computer_score > 21:
        return 'Your opponent has scores over 21. You won'
    elif user_score > computer_score:
        return 'You won!!!'
    else:
        return 'You lose'

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(user_cards)

        print(f"    Your score: {user_score}, your cards: {user_cards}")
        print(f'    Computer\'s first card {computer_cards[0]}')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Do you want to get another card ? Please type "y" or "no"')
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(compare(user_score,computer_score))


while input('Do you want play a BlackJack game ? Please type "y" or "n" \n') == 'y':
    play_game()
    
    clear = lambda: os.system('clear')
    clear()
else:
    print('Goodbye!!!')