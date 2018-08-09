# 1. Define a function that can accept two strings as input and concatenate them and then print it in console.
# 2. Define a function that can accept two strings as input and print the string with maximum length in console.
#    If two strings have the same length, then the function should print al l strings line by line.
# 3. Define a function that can accept an integer number as input and print the "It is an even number"
#    if the number is even, otherwise print "It is an odd number".

def merge():
    a = str(input("Type in first string: "))
    b = str(input("Type in second string: "))
    print(a + b)

# merge()

def wchichlonger():
    a = str(input("Type in first string: "))
    b = str(input("Type in second string: "))
    al = len(a)
    bl = len(b)
    if al > bl:
        print(a)
    if bl > al:
        print(b)
    else:
        print(a + "\n" + b)

# wchichlonger()

def doyoueven():
    while True:
        a = input()
        try:
            a = int(a)
            if a%2 == 0:
                print("This number is even")
            else:
                print("This number is odd")
            break
        except:
            print("give me integral number")

doyoueven()

