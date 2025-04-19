import random
secret_number = random.randint(1,1000)

success = False

for attempts in range(1,11,1):
    print(f'Attempt number: {attempts}')
    guessing_number = int(input('Enter the number to guess: '))
    if guessing_number > secret_number:
        print("High number")
    elif guessing_number < secret_number:
        print('Low number')
    else:
        print(f'CONGRATULATIONS!!, yout guest the number in the attempt number: {attempts}')
        success = True
        break
if attempts == 10 and not success:
    print(f'ERROR!!!... You cannot guess the number, the secret number was: {secret_number}')