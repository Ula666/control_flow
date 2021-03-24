# Control flow
# if, elif, else,
# Conditional statements are used to control the flow of our program

# Exercise:
# user input a age and display age back to a user
# casting implemented
# as a user I would like to sell tickets according to
# the age of user and category of the movie
# age = 12, PG, 15, 18

# age = input("Please enter your age: ")
# if int(age) >= 18:
#     print("You are:", age, "years old. You can purchase any ticket")
# elif int(age) >= 15:
#     print("You are:", age, "years old. You can purchase tickets for ratings: U, PG, 12 and 15")
# elif int(age) >= 12:
#     print("You are:", age, "years old. You can purchase tickets for ratings: U, PG and 12")
# else:
#     print("You are:", age, "years old. You can purchase tickets for ratings: U and PG")


# for loops and while loops
# syntax for is the keyword, variable then data collection
# shopping_list = ["bread", "eggs", "milk", "orange"]
# print(shopping_list)
# print(shopping_list[0]) # to print 1st thing
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

# for items in shopping_list:
#     print(items)
#
# # iterate through letters in a word
# for letter in "fruits":
#     print(letter)

# shopping_list = ["bread", "eggs", "milk", "orange"]
#
# for items in shopping_list:
#     print(items)
#     if items == "milk": # when the condition is tru the loop ends
#         break
        # end when milk is found, the loop will stop

food_bill = {1: {"name": "James", "bill": "£1"},
             2: {"name": "Bond", "bill": "£2"},
             3: {"name": "Shah", "bill": "£3"}} #3 keys(1,2,3)
# print(food_bill)
# iterate through this
# for items in food_bill.values():
#     print(items)

# print the names and the bill amount for each person
# for items in food_bill.values():
#     print("name:", items["name"] + ",", "bill:", items["bill"])
#
# # nested loop to iterate through the nested dict to get the value of bill by name
# for item in food_bill.values():
#     for name_bill in item.values():
#         print(name_bill)

# while loops:
# syntax: while condition value:
    # print()
# num = 0
# while num < 10: # while true continue, if false stop
#     print(f"it's working -> {num}")
#     num += 1

# second iteration
# num = 0
# while num < 10: # while true continue, if false stop
#     print(f"it's working -> {num}")
#     if num ==4: # if its true the loop ends
#         break
#     num += 1

# Use case as the 3rd iteration
# age = input("please enter you age")
# print(f"your age is {age}")

user_prompt = True
while user_prompt:
    age = input("please enter your age")
    if age.isdigit(): # checks if user entered age in digits
        user_prompt = False
    else:
        print("Please enter your age in digits")
print(f"your age is {age}") #this line of code only gets executed if the user enters age in digits

# ensure the loop conditions are in your control to avoid going into the iteration

