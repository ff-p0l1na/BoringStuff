# Write a program to find out how often a streak of six heads 
# or a streak of six tails comes up in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts: 
# the first part generates a list of randomly selected 'heads' and 'tails' values, 
# and the second part checks if there is a streak in it. 
# Put all of this code in a loop that repeats the experiment 10,000 times 
# so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. 
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random
numberOfStreaks = 0
tosses = ('H', 'T')
experimentNumber = 0

for experimentNumber in range(10000):
    my_str = ''
    # Code that creates a list of 100 'heads' or 'tails' values.
    for x in range(100):
        random_toss = random.choice(tosses)
        my_str += random_toss
        list_of_tosses = list(my_str)
    # Code that checks if there is a streak of 6 heads or tails in a row.
        streak_H = ['H', 'H', 'H', 'H', 'H', 'H']
        streak_T = ['T', 'T', 'T', 'T', 'T', 'T']
        streak_counter = 0
        if streak_H or streak_T in list_of_tosses:
            streak_counter += 1
            experimentNumber +=1
        else:
            experimentNumber +=1

        

print(experimentNumber)
print(streak_counter)

    # if streak_H in my_str:
    #     streak_counter += 1
    # elif streak_T in my_str:
    #     streak_counter += 1
    # else:
    #     pass


# print(streak_counter)



# print(f'Chance of streak: {numberOfStreaks / 100} % .')

