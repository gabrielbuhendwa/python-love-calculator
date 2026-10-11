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

love_score = str(true) + str(love) #convert them into string in order to concatenate them together

print(love_score)