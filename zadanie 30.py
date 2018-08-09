# Write a simple quiz game that has a list of the questions and a list of
# answers to those questions. The game should give the player four randomly selected
# questions to answer. It should ask the questions one by one, and tell the
# player whether they got the question right or wrong. At the end it should
# print out how many out of four they got right

'''This script needs "zadanie 30 Q and A" file to run'''

import random

start = open("zadanie 30 Q and A", "r")
question = []
a = []
b = []
c = []
d = []
correct = []
a_num = 1
q_num = 0

for line in start.readlines():
    try:
        line = line.strip()
        if line[0] == "#":
            if line[-1] == "?":
                question.append(line)
            else:
                x = line
        if line[-1] == "?" and x != 0:
            question.append(x + " " + line)
            x = 0
        if line[0] == "*" and a_num == 1:
            a.append(line[1:])
        if line[0] == "*" and a_num == 2:
            b.append(line[1:])
        if line[0] == "*" and a_num == 3:
            c.append(line[1:])
        if line[0] == "*" and a_num == 4:
            d.append(line[1:])
        a_num +=1
        if a_num == 5:
            a_num = 1
        if line[0:7] == "Answer:":
            correct.append(line[8:])
    except:
         continue

noq = int(input("How many questions would you like to answer? "))
points = 0

for i in range(noq):
    x = random.randint(0,1011)
    print(question[x])
    print("A: " + a[x])
    print("B: " + b[x])
    print("C: " + c[x])
    print("D: " + d[x])
    n = input("What is your answer? (A/B/C/D): ")
    if n == "A" and a[x] == correct[x]:
        print("Well done!")
        points += 1
    elif n == "B" and b[x] == correct[x]:
        print("Well done!")
        points += 1
    elif n == "C" and c[x] == correct[x]:
        print("Well done!")
        points += 1
    elif n == "D" and d[x] == correct[x]:
        print("Well done!")
        points += 1
    else:
        print("Wrong answer. Correct is: " + correct[x])

print("Congratulations! Your final score is {} out of {} points!".format(points,noq))