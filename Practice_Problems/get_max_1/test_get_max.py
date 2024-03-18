from get_max import *
"""
######################################################################################################################################
These test functions are used to test the code you write, you can ignore them, but when you run main these are the tests that will run
######################################################################################################################################
"""


def test_get_max_from_list(name, func):
    print(f"===== {name} =====")
    passed = ["FAILED", "PASSED"]
    # normal list
    test1 = func([1, 2, 3, 4, 5])
    print(f"test1 {passed[test1 == 5]}\n", f"expected:5", f"got:{test1}")

    # list with negative
    test2 = func([1, 2, 3, 4, -5])
    print(f"test2 {passed[test2 == 4]}\n", f"expected:4", f"got:{test2}")

    # list in descending order
    test3 = func([5, 4, 3, 2, 1])
    print(f"test3 {passed[test3 == 5]}\n", f"expected:5", f"got:{test3}")

    # empty list
    test4 = func([])
    print(f"test4 {passed[test4 == 0]}\n", f"expected:0", f"got:{test4}")

    # list with duplicates
    test5 = func([1, 8, 8, 4])
    print(f"test5 {passed[test5 == 8]}\n", f"expected:8", f"got:{test5}")
    print()


test_get_max_from_list("With loops",get_max_from_list)
test_get_max_from_list("With Recursion", get_max_from_list_rec)
print("===== get max =====")
get_max()
