from random import randint

secret = randint(0, 20)
guess = 0

while guess != secret:

    guess = int(raw_input("Guess the number between 1 and 20: "))

    if guess == secret:
        print "Congratulations, you guessed the number! It's {0}." .format(secret)
    elif guess > secret:
        print "Your guess is not correct... try something smaller"
    elif guess < secret:
        print "Your guess is not correct... try something bigger"
    else:
        print "Sorry, it's not {guess_val}." .format(guess_val=guess)

# for i in range(5):
#     guess = int(raw_input("Guess the number between 1 and 50: "))
#
#     if guess == secret:
#         print "Congratulations, you guessed the number! It's {0}." .format(secret)
#         break
#     else:
#         print "Sorry, it's not {secret_val}." .format(secret_val=guess)