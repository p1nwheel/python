def collatz(numberIn):
    if type(numberIn) == int:
        number = numberIn
        while not number == 1:
            if number % 2 == 0:     # True if input is Even
                number = number // 2
                print(str(number))
            elif number % 2 == 1:   # True if input is Odd
                number = 3 * number + 1
                print(str(number))
    else:
        print('Collatz requires integer value to execute')

def enterNum(maxTries):
    for attemptsTaken in range(1, (maxTries) + 1):
        try:
            fail = 0
            print('Enter Number:')
            number = int(input())
        except:
            print('Enter whole number only!')
            fail = 1
        if fail == 0:
            return(number)
            break
    print('No number entered after ' + str(maxTries) + ' attempts')

number = enterNum(3)
collatz(number)
print('And we are done!')

