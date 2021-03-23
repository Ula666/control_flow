# Control flow
# if, elif, else,
# Conditional statements are used to control the flow of our program

# Exercise:
# user input a age and display age back to a user
# casting implemented
# as a user I would like to sell tickets according to
# the age of user and category of the movie
# age = 12, PG, 15, 18

age = input("Please enter your age: ")
if int(age) >= 18:
    print("You are:", age, "years old. You can purchase any ticket")
elif int(age) >= 15:
    print("You are:", age, "years old. You can purchase tickets for ratings: U, PG, 12 and 15")
elif int(age) >= 12:
    print("You are:", age, "years old. You can purchase tickets for ratings: U, PG and 12")
else:
    print("You are:", age, "years old. You can purchase tickets for ratings: U and PG")


# for loops and while loops
