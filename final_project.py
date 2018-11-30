# this file was created by ziante
    # with help of https://www.youtube.com/watch?v=Dl9VAVO4EcY
    #https://stackoverflow.com/questions/37007009/typing-game-made-in-python-timer-multithreading-def-etc
import random
from threading import Timer

randint = (print(one[randint(0, len(one)-1)]+' '+two[randint(0, len(two)-1)]+' '+three[randint(0, len(three)-1)]+' '+four[randint(0, len(four)-1)]+' '+five[randint(0, len(five)-1)]+'.'))
one = ["The", "An", "Our", "Their"]
two = ["enthusiastic", "active" , "efficient", "archaic", "animalistic", "underrated"]
three = ["boy", "cat", "computer", "machine", "guy", "girl", "lion", "zebra", "car"]
four = ["eats nasty", "chases many", "makes very efficient", "produces a mass amount of", "jumps on", "cooks very good"]
five = ["chocolate bars", "mice throughout the zoo", "criminals in the park", "tools under the shed"]
score = 0

endgame = 0

def printover():
    print("game OVER")
    endgame = 1

def input():
    points = 0
    while(score >= 0):
        timeout = 10
        timer = Timer(timeout, printover)
        timer.start()
        if(points < 5):
            cs = print((print(one[randint(0, len(one)-1)]+' '+two[randint(0, len(two)-1)]+' '+three[randint(0, len(three)-1)]+' '+four[randint(0, len(four)-1)]+' '+five[randint(0, len(five)-1)]+'.')))
        print("Type this sentence:", ((one[randint(0, len(one)-1)]+' '+two[randint(0, len(two)-1)]+' '+three[randint(0, len(three)-1)]+' '+four[randint(0, len(four)-1)]+' '+five[randint(0, len(five)-1)]+'.')))
        user = "You have %d seconds to choose the correct answer...\n" % timeout
        answer = input(user)
        timer.cancel()
        if (answer == cs) and (endgame == 0):
            print("Keep going")
            points += 1
        else:
            print("Bye")
            exit()
input()