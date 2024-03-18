"""
######################################################################################################################################
Implement the two following functions to get a list of numbers from the user and then return the max
######################################################################################################################################
"""
def get_list_from_user():
    # implement code that asks the user for numbers until they type "done"
    # (hint: make sure to convert the input numbers to type int from type string)

    return ["user", "input", "goes", "here"]

def get_max_from_list(num_list):
    # use the get_list_from_user function you wrote above to get a list of numbers from the user

    # go through the num_list list and find the largest number, if the list is empty return the number 0
    # (hint: create a variable to store the largest value you've found)

    # return the largest number bellow
    return 0  # replace this zero with the max number from the list


"""
This function is already finished, it combines the 2 functions above and prints the output
"""
def get_max():
    # user get_list_from_user to get a list of numbers from the user
    user_numbers = get_list_from_user()
    # get the max number from this list
    max_num = get_max_from_list(user_numbers)
    # print out the max number
    print(max_num)

"""
######################################################################################################################################
Extra Credit, impliment get_max() using recursion (a fcuntion that calls itself
######################################################################################################################################
"""
def get_max_from_list_rec(num_list):
    # use the get_list_from_user function you wrote above to get a list of numbers from the user

    # use a similar process to what you did above but use recursion instead of a loop (this function call's itself)

    # return the largest number bellow
    return 0

def get_max_rec():
    # user get_list_from_user to get a list of numbers from the user
    user_numbers = get_list_from_user()
    # get the max number from this list
    max_num = get_max_from_list_rec(user_numbers)
    # print out the max number
    print(max_num)