import random

numberOfStreaks = 0
tosses = ('H', 'T')

for experimentNumber in range(10):
    my_str = ''
    # Code that creates a list of 100 'heads' or 'tails' values.
    for x in range(100):
        random_toss = random.choice(tosses)
        my_str += random_toss
    print(my_str)
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_H = 'H' * 6
    streak_T = 'T' * 6
    if streak_H in my_str or streak_T in my_str:
        numberOfStreaks += 1
        print(f'{my_str} streak')
    else:
        print(f'{my_str} no streak')

print(f'Chance of streak: {numberOfStreaks / 100} % .')