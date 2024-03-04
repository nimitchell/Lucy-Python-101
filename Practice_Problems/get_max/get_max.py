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
These test functions are used to test the code you write, you can ignore them, but when you run main these are the tests that will run
######################################################################################################################################
"""
def test_get_max_from_list():
    passed = ["FAILED", "PASSED"]
    # normal list
    test1 = get_max_from_list([1, 2, 3, 4, 5])
    print(f"test1 {passed[test1 == 5]}\n", f"expected:5", f"got:{test1}\n")

    # list with negative
    test2 = get_max_from_list([1, 2, 3, 4, -5])
    print(f"test2 {passed[test2 == 4]}\n", f"expected:4", f"got:{test2}\n")

    # list in descending order
    test3 = get_max_from_list([5, 4, 3, 2, 1])
    print(f"test3 {passed[test3 == 5]}\n", f"expected:5", f"got:{test3}\n")

    # empty list
    test4 = get_max_from_list([])
    print(f"test4 {passed[test4 == 0]}\n", f"expected:0", f"got:{test4}\n")

    # list with duplicates
    test5 = get_max_from_list([1, 8, 8, 4])
    print(f"test5 {passed[test5 == 8]}\n", f"expected:8", f"got:{test5}\n")


test_get_max_from_list()
get_max()