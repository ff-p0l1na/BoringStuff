# Write a function that takes a list value as an argument 
# and returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. 
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it. 
# Be sure to test the case where an empty list [] is passed to your function.

spam = ['apples', 'bananas', ['pins', 'needles'], 'tofu', 43, 'cats']
empty_spam = []

def CommaCode(list):
    try:
        my_str = ''
        for item in list[:-1]:
            my_str += str(item) + ', '
        my_str += f'and {list[-1]}.'
    except:
        if IndexError:
            print('List needs more elements!')
        
    return my_str
    
print(CommaCode(spam))
