
import random, sys, shelve

streak = 0
personalBest = 0

def generate():
    global streak, personalBest
    x = random.randint(3,9)
    y = random.randint(3,9)

    while True:
        try:
            print(x,"x",y, "= ")
            answer = input()

            if answer == "quit":
                sys.exit()

            elif int(answer) == (x*y):
                print("correct!")
                streak += 1
                generate()

            else:
                if streak > personalBest:
                    personalBest = streak
                print("Incorrect.. streak:",streak,"PB:", personalBest)
                streak = 0

        except SystemExit: # catch exception from if statement sys.exit()
            shelfFile.close()
            sys.exit()
        except:
            print("Enter an integer")


generate()
