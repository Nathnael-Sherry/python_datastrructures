x = 10
y = 20
if x< y and x == 20:
    print("TRUE")
else:
    print("FALSE")

pi = 3.142
radius = 12
area = pi*radius*radius
if area < 1000:
    print("This is a small circle")
else:
    print("This is a big circle")

principle = 2000
rate = 5
time = 3
interest = (principle * rate * time)
if interest < 500:
    print("The loan is affordable")
elif interest < 1500:
    print("The loan is expensive")
else:
    print("The loan is a scam")

weight = 50
height = 15
BDM = weight/height*height
if  BDM < 18:
    print("underweight")
elif BDM >18:
    print("normal weight")
elif BDM > 24 and BDM < 29:
    print("Over weight")
else:
    print("Obese")

marks = 100
if marks < 40:
    print("D")
elif marks < 50:
    print("C")
elif marks < 60:
    print("B")
else:
    print("A")
a = 10
b = 20
if a > b:
    if b > 20:
        print("TRUE")
    else:
        print("FALSE")
else:
    if a > b:
        print("SECOND TRUE")
    else:
        print("SECOND FALSE")

# Given three variables "ageOne, ageTwo, age three"
# containing integer values, write efficient
# python statements to satisfy the following conditions
# 1. If ageOne is greater than ageTwo, proceed to check
#  i. if ageThree is greater than 18, display a
#  welcome message. Else, display a goodbye message.
# 2. If ageOne is less than ageTwo, proceed to check
# the following conditions on ageThree variable
#  i. if ageThree is greater than 15, display a
#  welcome message. Else, display a goodbye message.

ageOne = 10
ageTwo = 20
ageThree = 30
if ageOne> ageTwo:
    if ageThree > 18:
        print("WELCOME")
    else:
        print("GOODBYE")
else:
    if ageOne < ageTwo:
        if  ageThree > 15:
            print("WELCOME")
        else:
            print("GOODBYE")
