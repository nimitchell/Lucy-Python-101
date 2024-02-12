


if __name__ == "__main__":
    num = input("please input a number")
    num = int(num)
    result = ""  # define result in main global scope

    if num == 0:
        result = "A"  # update the value of result to A

    elif num < 5:  # use an elif here to avoid result being set to B when num == 0
        if num >= 0:
            result = "B"
        else:
            result = "c"

    else:
        print("number is too big")
        exit()  # stop the program before it prints out result

    print(result)  # Print the updated value of result
