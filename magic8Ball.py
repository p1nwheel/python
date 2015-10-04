import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    elif answerNumber == 10:
        return 'How about tea?' #This is Emily's answer

#r = 0
#howMany = 0
counting = 0
while True:
    r = 0
    howMany = 0
    counting = counting + 1
    while r != 10: #Dont forget to indent the below
        howMany = howMany + 1
        r = random.randint(1, 10)
        fortune = getAnswer(r)
        print(fortune)
    print('You took ' + str(howMany) + ' tries')
    if howMany > 25:
        print('Count was ' + str(counting))
        break
#print()
#print(getAnswer(random.randint(1, 10)))
