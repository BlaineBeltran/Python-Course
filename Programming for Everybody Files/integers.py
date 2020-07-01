# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

lst = []
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        lst.append(int(user_input))
    except ValueError:
        print('Invalid input')

if lst:
    print('max:', max(lst))
    print('Min:', min(lst))
