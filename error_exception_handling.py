#Start with try except if

#As defined in readme, an error response method not dissimilar to if, elif, else

#Let's start throwing some errors around

# name = "devops"
# year = 2021
# print(name + year)
# #throws a TypeError - can't combine str and int
#
# file = open("order.txt")
# this would be a FileNotFoundError


#Let's try the same scenario, but with a try except block

try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    #creating aliases. The as portion defines the error message as a variable
    print("order.txt not found\n" + str(errmsg))
finally:
    print("Thank you for visiting, hope to see you again!")
    #This will run, regardless of whether the other blocks run.