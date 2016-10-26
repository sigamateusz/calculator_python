import os
os.system('clear')

def second_number():
    print("It's not correct sign.")
    try:
        n=int(input("Enter number again: "))
        return n
    except ValueError:
        second_number() # up trying input is integer

while 1:
    try: # try convert input to int
        a=int(input("Enter a number (or a letter to exit): "))
    except ValueError:
        exit() # if can't convert to int close the program
    a=str(a) # convert first number to string
    x=input("Enter an operation: ")
    while  x!='+' and x!='-' and x!='/' and x!='*': #checks sign of input
        x=input("It's invalid sign. Enter an operation again: ")
    try:
        b=int(input("Enter another number: ")) # probuje przerobic na inta
    except ValueError:
        b=second_number()
    b=str(b) # convert second number to string
    print("Result : %.0f\n" %eval(a+x+b) ) #
