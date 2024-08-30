# Defining the Collatz Function
import sys
def collatz(number):
    rem = number % 2
    if rem == 0:
        even= number // 2
        print(even)
        return even
    else:
        odd= 3* number +1
        print (odd)
        return odd

try: # Try clause for the continuation of the code after the first run until user asks to stop
    while True: # Maintains a loop until value of the number reaches 1
        try: # To avoid any string inputs
            print('Enter a number')
            num=int(input()) # int() converts the users input to Integer
            while num !=1 :
                num =collatz(num)
        except :
            print('Enter an integer bozo')
except KeyboardInterrupt:
    sys.exit()

