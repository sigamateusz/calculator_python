while 1:
    try:
        a=int(input("Enter a number (or a letter to exit): ")) # probuje przerobic na inta
    except ValueError:
        exit() # jak nie wyjdzie to znaczy ze litera i zamyka program
    a=str(a) # zamienia na string zeby policzyc je wszystkie na koncu przez eval()
    print(a)
    x=input("Enter an operation: ")
    print(x)
    while x!="+" or x!="-" or x!="/" or x!="*": ####### nie chce sprawdzac kilku warunkow
        x=input("Enter an operation: ")
    print(x)
    b=input("Enter another number: ")
    result=a+x+b
    print(eval(result)) # oblicza wynik ze string
