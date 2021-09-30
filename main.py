import random

print(
printchoose difficulty-easy,medium,hard")
difl= input().lower()if diflv == "easy":
uplim = 1
    sno = random.randrange(1, 100)
    uess = 8
if dilv == "medium":
    upim = 200
    sno= random.randrange(1, 200)
    gues = 8
if diflv = "hard":
    uplim  500
    sno = rndom.randrange(1, 500)
    guess = 
print()
print("you have choosen", diflv, "difficulty\n"
print("THE SECRET NUMBER IS AN INTEGER BETWEEN 1 AND", uplim)
while(1)
    print("YOU HAVE",guess,"GESSES LEFT!")
    print("ENTER YOUR NUMBER")
    userp = int(input())
    guess = guess - 1

    if gues == 0 and userinp != sno:
        prit("GAME OVER\nNO GUESSES LEFT\nTHE SECRET NUMBER WAS",sno)
        brea
    elif userinp < sno
        print("try something bigger"
        continue
    elif userinp > sno:
        print("try something smaller")
        continue
    elif userinp == sno:
        print("CONGRATIONS YOU WON, THE SECRET NUMBER WAS",sno,"GUESSES REMAINING =", guess)
        break
print("\n the end")
print("game made by pallav")
exit12 = input("press enter to exit")
