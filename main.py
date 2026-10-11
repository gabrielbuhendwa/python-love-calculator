print("Welcome to the Love calculator")

#user required questions
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#challenge code logic
combined_string = name1 + name2

#transforming every user's input into lower case
lower_case_string = combined_string.lower()

#checking compatibility with the first word (TRUE)
t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true = t + r + u + e

#checking compatibility with the first word (LOVE)
l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")

love = l + o + v + e

#convert them into string in order to concatenate them together
#then convert them into integer in order to do a calculation because 2 and 5 was (25) instead of (7)
love_score = int(str(true) + str(love))

#score interpretation Message logic
if (love_score < 10) or (love_score > 90): #in pyton we can use () or not in those if/else logic
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) or (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else :
    print(f"Your score is {love_score}.")