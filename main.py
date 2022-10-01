import random


print("""
WELCOME TO MY GAME!

INSTRUCTIONS:

- You have to guess a secret number. 
- After each guess, I will tell you if your guess was lower/higher than the secret number.
- You have limited guesses before you lose.

GOOD LUCK!

""")
diflv = input("Choose a difficulty level: easy / medium / hard: ").lower()
if diflv == "easy":
    uplim = 100
    sno = random.randrange(1, 100)
    guess = 8
if diflv == "medium":
    uplim = 200
    sno = random.randrange(1, 200)
    guess = 8
if diflv == "hard":
    uplim = 500
    sno = random.randrange(1, 500)
    guess = 10
print()
print("YOU HAVE CHOSEN:", diflv, "difficulty\n")
print("THE SECRET NUMBER IS AN INTEGER BETWEEN 1 AND", uplim)

while (1):
    print("\nYOU HAVE", guess, "GUESSES LEFT!")

    userinp = int(input("Enter Your Number: "))
    guess = guess - 1

    if guess == 0 and userinp != sno:
        print("GAME OVER\nNO GUESSES LEFT\nTHE SECRET NUMBER WAS: ", sno)
        break
    elif userinp < sno:
        print("try something bigger")
        continue
    elif userinp > sno:
        print("try something smaller")
        continue
    elif userinp == sno:
        print("CONGRATULATIONS YOU WON, THE SECRET NUMBER WAS", sno,
              "\nGUESSES REMAINING = ", guess)
        break
print("\nTHE END!")
print("Game Made By Pallav")
exit12 = input("press ENTER to exit ")
