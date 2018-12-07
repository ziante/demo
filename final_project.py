# this file was created by Ziante
# with the help from

from timeit import default_timer
import random

# function for each round

def gameround(speed,text,score):

# ready to begin?

    throwawayvariable = input("Start whenever you are ready. Press enter to begin".format(speed))

# start the timer

    starttime = default_timer()

# give them a text from the list to type

    theirAnswer = input("Type this text: {}\n".format(text))

# stop timer and calculate how they did

    stoptime = default_timer()

    totalTime = stoptime - starttime
    print("it took you {} seconds".format(totalTime))

# who won, update score

    if totalTime <= speed and theirAnswer == text:
        print("there we go")
        score[0] = score[0] + 1
    else:
        print("That was terrible!")
        score[1] = score[1] + 1

# return score
    return score

#score board

score = [0,0]

# different list of sentences to type

masterlist = ['He went to the store to get groceries for his family', 'She payed for his friend because his parents gave him 3 dollars.', 'We walked to the beach with my dog after we ate breakfast', 'She did not want to go into the water because she heard there were sharks.']

# game loop

# either feed or break the function

while True:
    if score[0] == 2 or score[1] == 2:
        if score[0] == 2:
            print("great job!!!")
        if score[1] == 2:
            print("keep practicing!")
        break
    else:
        textspeed = random.randint(10,20)
        a = random.randint(0,3)
        textTocopy = masterlist[a]
        score = gameround(textspeed,textTocopy,score)
        print("your score is {}".format(score[0]))
        print("the computer score is {}".format(score[1]))

