# To-do: Create add() function here.


# To-do: Create subtract() function here.


# To-do: Create multiply() function here.


# To-do: Create divide() function here.


# To-do: Create exponentiate() function here.


# To-do: Create squareRoot() function here.


# main function
def main():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")

    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4, 5]:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
    elif choice == 6:
        number = float(input("Enter a number: "))
    else:
        print("Invalid choice.")
        return

    if choice == 1:
        # To-do: Call the add() function created above and initialize 'results' variable to it.
    elif choice == 2:
        # To-do: Call the subtract() function created above and initialize 'results' variable to it.
    elif choice == 3:
        # To-do: Call the multiply() function created above and initialize 'results' variable to it.
    elif choice == 4:
        # To-do: Call the divide() function created above and initialize 'results' variable to it.
    elif choice == 5:
        # To-do: Call the exponentiate() function created above and initialize 'results' variable to it.
    elif choice == 6:
        # To-do: Call the squareRoot() function created above and initialize 'results' variable to it.
    else:
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
