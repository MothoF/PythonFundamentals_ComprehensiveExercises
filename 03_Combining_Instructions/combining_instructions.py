def max_three():
    """
    Write a Python function to find the Max of three numbers.
    Use the following as test input in STDIN

    Input:
    ```
    1
    8
    6
    ```
    """

    def max_of_two( x, y ):
        if x > y:
            return x
        return y
    def max_of_three( x, y, z ):
        #enter your code here
        numbers = [x,y,z]
        highest = max(numbers)
        return highest

    num1 = int(input("Please enter num1"))
    #enter your code here
    num2 = 5
    num3 = 20
    print(f"The max of the three numbers is: {max_of_three(num1,num2,num3)}")


def between_3_and_9(n):
    """
    Write a Python function to check whether a number falls between 3 and 9
    """

    if n in range(3,10):
        #enter code here
        print(f"{n} is in the range")
    else:
        print("The number is outside the given range.")


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    # max_three()
    max_three()
    # between_3_and_9(n)
    n = 6
    between_3_and_9(n)
