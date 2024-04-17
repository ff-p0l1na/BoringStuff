# Write a short program that prints the numbers 1 to 10 using a for loop.

for x in range(1,11):
    print(x)

# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

n = 0
while n < 10:
    n += 1
    print(n)

# Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, 
# and prints Greetings! if anything else is stored in spam.

while True:
    spam = input("Type 1, 2, or anything:")
    if spam == '1':
        print("Hello")
    elif spam == '2':
        print("Howdy")
    elif spam == 'anything':
        break    
    else:
        print("Greetings!")


