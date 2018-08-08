# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

print("Please input a sentence:")
phrase = input()
splitted = phrase.split(" ")
sorted = sorted(splitted)

for word in sorted:
    n = sorted.count(word)
    print(word + " " + str(n))
    while n > 1:
        sorted.remove(word)
        n -= 1
