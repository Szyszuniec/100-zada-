# Napisz program, w którym użytkownik będzie wpisywał tekst po angielsku, a program policzy
# ile rodzajników jest w tekście. Rodzajniki to słowa 'a', 'an' i 'the'.

def articles(text):
    '''Function counts number of articles (a, and, the) in the given text'''
    words = text.split(" ")
    i = 0
    for word in words:
        word = word.strip(",")
        word = word.strip(".")
        if word == "a" or word == "and" or word == "the":
            i +=1
    print("Number of articles equals " + str(i))

articles(input())