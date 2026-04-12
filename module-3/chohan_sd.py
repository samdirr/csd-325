
"""Cho-Han, modified for CSD-325 Module 3.
Original program by Al Sweigart.
Changes by Sam Dirr:
1. Changed input prompts to initials: sd:
2. Changed house fee from 10% to 12%
3. Added intro notice for 2 or 7 dice roll bonus
4. Added 10 mon bonus when roll total is 2 or 7
5. Added comments documenting changes
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus Notice: If the dice total is 2 or 7, you receive a 10 mon bonus.
''')

purse = 5000

while True:
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('sd: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('sd: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    roll_is_even = roll_total % 2 == 0
    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    player_won = bet == correct_bet

    # Display the bet results:
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # Change: house fee changed from 10% to 12%.
        house_fee = int(pot * 0.12)
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # Change: bonus for rolling 2 or 7.
    if roll_total == 2 or roll_total == 7:
        print('Bonus! The total roll was', roll_total, 'and you got a 10 mon bonus!')
        purse = purse + 10

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()