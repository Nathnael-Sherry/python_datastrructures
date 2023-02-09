#day_of_week = input("Enter Day of the Week")

#if day_of_week == "monday":
    #print("it's indeed monday")
#elif day_of_week == "tuesday":
    #print("its tuesday")
#else:
    #print("Thank you")

dial = int(input("Enter ussd code"))
if dial == 1:
    print("Enroll for bonga points")
elif dial == 2:
    print("Data Deals")
elif dial == 3:
    print("Fuliza")
elif dial == 98:
    print("More options")
else:
    print("Thanks")