secret = 16

guess = int(raw_input("Guess the number between 1 and 50: "))

if guess == secret:
    print "Congratulations, you guessed the number!"
else:
    print "Sorry, wrong number. Try again!"
