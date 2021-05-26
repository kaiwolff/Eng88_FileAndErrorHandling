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
#
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     #creating aliases. The as portion defines the error message as a variable
#     print("order.txt not found\n" + str(errmsg))
# finally:
#     print("Thank you for visiting, hope to see you again!")
#     #This will run, regardless of whether the other blocks run.


# Second Iteration:
def open_using_with_and_print(file):

    try:
        with open("order.txt", "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print(f"{file} not found\n" + str(errmsg))

    finally:
        print("Thank you for visiting, hope to see you again!")
        #This will run, regardless of whether the other blocks run.


print(open_using_with_and_print("order.txt"))

#Mini-Task: Create a function called open_with_to_write_to_file to write/add/append
#display the data with the added items - item names - Pizza, Cake, Avocado, Biryani, Pasta

def open_with_to_write_to_file(file, item_list):
    try:
        with open("order.txt", "a") as file:
            for item in item_list:
                file.write(f"\n{item}")

    except FileNotFoundError as errmsg:
        print(f"{file} not found\n" + str(errmsg))

    finally:
        print("Thank you for adding to the order, hope to see you again!")
        #This will run, regardless of whether the other blocks run.

order_list = ["Pizza", "Cake", "Avocado", "Biryani", "Pasta"]

open_with_to_write_to_file("order.txt", order_list)