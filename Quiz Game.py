print ("Welcome to my quiz!")
playing =  input("Do you want to play?: ")
if playing != "yes":
    quit()

score = 0
streak = 0

print ("1. What is 4+19?")

print ("A.14")
print ("B.25")
print ("C.8.4")

ans = input("Enter your answer: ")

if ans == "B":
    print ("Correct!")
    score = score+1
    streak = streak+1
    if streak >= 3:
        print ("You are on a streak of",streak,"!")
    
else:
    print ("Wrong!")
    if ans != "B" and streak >= 3:
        print ("You just broke you streak!")
        streak = 0

print ("2. What is the capital of France?")

print ("A.Berlin")
print ("B.New Delhi")
print ("C.Paris")

ans = input("Enter your answer: ")

if ans == "C":
    print ("Correct!")
    score = score+1
    streak = streak+1
    if streak >= 3:
        print ("You are on a streak of",streak,"!")

else:
    print ("Wrong!")
    if ans != "C" and streak >= 3:
        print ("You just broke your streak!")
        streak = 0
    

print ("3. What is largest continent?")

print ("A.Europe")
print ("B.Antarctica")
print ("C.Asia")

ans = input("Enter your answer: ")

if ans == "C":
    print ("Correct!")
    score = score+1
    streak = streak+1
    if streak >= 3:
        print ("You are on a streak of",streak,"!")
else:
    print ("Wrong!")
    if ans != "C" and streak >= 3:
        print ("You just broke your streak!")
        streak = 0

print ("4. Find the average of the following list")
print (1,2,3,4,5)

list = (1,2,3,4,5)

average = sum(list)/len(list)

ans = input("Enter your answer: ")

if float(ans) == (average):
    print ("Correct!")
    score = score+1
    streak = streak+1
    if streak >= 3:
        print ("You are on a streak of",streak,"!")
else:
    print ("Wrong!")
    if ans != average and streak >= 3:
        print ("You just broke your streak!")
        streak = 0

print ("5. What is 5+3*(8+2)")

print ("A.80")
print ("B.75")
print ("C.32")
print ("D.Enter your own answer")

ans = input("Enter your answer: ")

if ans == "D":
    ans_D = input("Enter your answer: ")
    if ans_D == "35":
        print ("Correct!")
        score = score+1
        streak = streak+1
        if streak >= 3:
            print ("You are on a streak of",streak,"!")

else:
    print ("Wrong!")
    if ans != "ans_D" and streak >= 3:
        print ("You just broke your streak!")
        streak = 0

if score >= 3:
    print ("Congrats you got",score,"out of 5! which is better than most people!")

else:
    print ("Congrats your score is",score,"out of 5 which is worse than most...")














