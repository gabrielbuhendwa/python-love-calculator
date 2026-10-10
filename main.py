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