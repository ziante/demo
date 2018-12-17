# this file was created by Ziante

# with the help from:
'''https://stackoverflow.com/questions/29938804/generate-random-sentences-in-python'''
'''https://www.youtube.com/watch?v=sRULB7Dcys0'''

# this is a typing game which challenges the user to type faster than the computer time.

'''Typing Game
    Challenging, Fun, Useful, and Creative (requires a decent typing speed)
   
    Gameplay Ideas: Have a random text generator that the user must type correctly while also trying to beat the computer time
    
    Bugs and Struggles: Sometimes the code calls on the same sentence, would be better if it could choose the sentences in order
                        
                            Wanted a boundary because for some of the longer texts it is hard to type because it goes to the very end of the screen
                       
                        Tried to get my code to turtle but I didnt want to go through the whole windows photoshop downloads on my mac, I figured I can just spend more time perfecting my code
                        
                        I also wanted to get code that could calculate the words per minute typed but when I typed it in the code it was not running. I spent a couple of days trying to get this to work but it was hard because the time I was using was seconds and I would have to do a ratio to go from seconds to minutes in the words per minute calculator
                          
                            Towards the ending weeks I realized that I wanted my code to actually work so I did some fishing for how to code a timer and found one that seemed easy and a nice addition to the game. It simply calculated how long the user took to type the text from start to end.
    
    Gameplay fixes: Sort of fixed the problem sentence problem by adding more sentences and expanding the range so it would be rare that the same sentence gets printed
                    
                    Took a lot of tests to get the timer right, did not want to give too much or too little time
                    
                    About 2 weeks in I had to restart because I tried adding code that I found for a different sentence generator but the code had many bugs
                        
                        The new sentences actually made sense and were easy to change. Also, it required less code which was easier for me to actually understand the code'''
from timeit import default_timer
import random
from turtle import Turtle
from turtle import done

# function for each round

# this includes the speed which they need to beat, which varies throughout the game

# it also includes the text and score for the game

def gameround(speed,text,score):

# this is what the user is going to see before he is ready to start typing

    variable = input("Start whenever you are ready. Press enter to begin".format(speed))

# the timer starts when the player presses enter and begins typing

    starttime = default_timer()

# when the user is ready to begin he will be told to type the random text which is selected

    theirAnswer = input("Type this text: {}\n".format(text))

# when the user is done the timer will stop and will also calculate the time

    stoptime = default_timer()

    totalTime = stoptime - starttime
    
    print("it took you {} seconds".format(totalTime))

# this is the code that runs at the end of each round. It calculates the faster time between the user and the computer

    if totalTime <= speed and theirAnswer == text:
        print("there we go")
        
        score[0] = score[0] + 1
    else:
        print("That was terrible!")
        
        score[1] = score[1] +1

# this is nearing the end of the round for the score
    return score

#finally, this is the score board

score = [0,0]

# this is the list of random sentences that will be selected for the user to begin typing

# the sentences vary in length because I wanted some rounds to be more challenging than others

masterlist = ['He did not want to go to the store to get groceries but his mom made him. She gave him her card so he decided to buy a gift card.', 
'I saw many new animals at the zoo but one stood out to me. The elephants really caught my attention because of their massive size.', 
'We walked to the beach with my dog after we ate breakfast. My friends bet me 10 dollars to go into the water, but it was too cold. ', 
'She did not want to go into the water because she heard there were sharks. After watching Jaws, she never wanted to go near any beaches.',
'When my dad went to the bathroom, my brother put salt in his water. I wanted to tell him when he got back, but it was too late. He was already running to the bathroom.',
'I never believed in ghosts, but when I was home alone and heard a pot fall downstairs my beliefs changed. I stayed under my blankets until my parents got home.',
'I loved camping but was not looking forward to the long car ride. We were on the road for 5 hours and I was also car sick for 5 hours.',
'When I asked my teacher why she assigns so much homework, she responded, "When I was in school I never liked homework either, but I realized that it is very important".',
'I always had my sisters back, but when she decided to start an argument with my dad, I was not getting in the middle of it.']

# now this is the actual game loop code

# Most of the code below is not mine but I made many minor adjustments because I did not want my game to run throughout the same boundaries as the code that I found
 # I made some changes to make the game more challenging, such as rounds, longer text, more time, a computer as an opponent
# I adjusted the rounds to 4 because I wanted to implement different rounds instead of first to 1

# Also I changed the times because I wanted longer text to write and that required more time for the user to keep up with the computer time
while True:
    # this is where I made the changes to how many rounds are needed to win because I wanted the game to last longer and add some variety
    if score[0] == 4 or score[1] == 4:
        # this is different from the code up top because this prints after the whole game is done and deteremines the winner of the whole game. The code above only prints who won that individual round
        if score[0] == 4:
            print("You won, GREAT JOB!!!")
        if score[1] == 4:
            print("You lost, KEEP PRACTICING!!!")
        break
    else:
        
        # below is the amount of seconds that the computer types the sentence in which the user has to type faster, to beat the time
       
        textspeed = random.randint(22,40)
        
        # I extended the list because I did not want to type the same sentence multiple times which also forced me to extend the range to match the list
        
        a = random.randint(0,8)
        textTocopy = masterlist[a]
        score = gameround(textspeed,textTocopy,score)
        print("your score is {}".format(score[0]))
        print("the computer score is {}".format(score[1]))

