# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

i = 1000
while i <= 3000:
    t = i//1000
    s = i//100
    d = i//10
    if t%2 == 0 and s%2 == 0 and d%2 == 0 and i%2 == 0:
        print(i, end=", ")
    i +=1