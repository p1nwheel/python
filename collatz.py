def collatz(numberIn):
    global number
    number = numberIn
    if number % 2 == 0:     # True if input is Even
        number = number // 2
        print(str(number))
    elif number % 2 == 1:   # True if input is Odd
        number = 3 * number + 1
        print(str(number))

def enterNum():
    global number
    while True:
        try:
            fail = 0
            print('Enter Number:')
            number = int(input())
        except ValueError:
            print('Enter whole number only!')
            fail = 1
        if fail == 0:
		return(number)
            	break

enterNum()
while True:
    collatz(number)
    if number == 1:
        break
