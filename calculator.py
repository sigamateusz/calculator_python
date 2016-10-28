import os
os.system('clear') # clear screen

def second_number():
    print("It's not correct sign.")
    try:
        n=int(input("Enter number again: "))
        return n
    except ValueError:
        second_number() # up trying input is integer
def main():
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
            b=int(input("Enter another number: ")) # try convert input to int
        except ValueError:
            b=second_number() # uses function second_number() to try again
        b=str(b) # convert second number to string
        print("Result : %.2f\n" %eval(a+x+b)) # eval count result
if __name__=="__main__":
    main()
