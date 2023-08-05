# To-do (Kirandeep): Create add() function here.


# To-do (Nimrta): Create subtract() function here.


# To-do (Stephen): Create multiply() function here.


# To-do (Soureen): Create divide() function here.


# To-do (Davi): Create exponentiate() function here.


# To-do (Thamal): Create squareRoot() function here.
def squareRoot(num):
    if num >= 0:
        return num ** 0.5
    else:
        return "Error: Cannot calculate the square root of a negative number."


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
        # To-do (Kirandeep): Call the add() function created above and initialize 'results' variable to it.
    elif choice == 2:
        # To-do (Nimrta): Call the subtract() function created above and initialize 'results' variable to it.
    elif choice == 3:
        # To-do (Stephen): Call the multiply() function created above and initialize 'results' variable to it.
    elif choice == 4:
        # To-do (Soureen): Call the divide() function created above and initialize 'results' variable to it.
    elif choice == 5:
        # To-do (Davi): Call the exponentiate() function created above and initialize 'results' variable to it.
    elif choice == 6:
        # To-do (Thamal): Call the squareRoot() function created above and initialize 'results' variable to it.
        result = squareRoot(number)
    else:
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
