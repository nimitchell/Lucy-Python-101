

if __name__ == "__main__":
    # ask the user for a number and store it as a string
    x = input("enter a number:")
    print("your number:\n", x, type(x))

    # convert the string into an integer so you can do math with it
    int_x = int(x)
    print("converted to an int:\n", int_x, type(int_x))

    # multiply and divide the input string then print he results
    mult = int_x * 4
    div = mult/2
    # even though the number divides evenly, division results in the type 'float' in python
    print("multiply it by 4 and divide it by 2\n", div, type(div))

    # finally convert the float back to an integer
    int_div = int(div)
    print("now turn it back into an int\n", int_div, type(int_div))

    # demonstrate concatenation
    newNum = input("enter a new number:") # here I am using "camel case" for the variable names
    newNumPlusHello = newNum + 'hello'

    # python doesn't know the number is an int, so it uses it as a string and puts the string togather
    print(newNumPlusHello)
    print("Now I am using concatenation in a print statement. " + newNumPlusHello + " is my output string")
