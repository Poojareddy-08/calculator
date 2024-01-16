def calculator():
    print("Welcome to the simple calculator!")

    while True:
        # Get user input
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform the calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero")
                continue
            result = num1 / num2
        else:
            print("Invalid operation")
            continue

        # Display the result
        print(f"The result is: {result}")

        # Ask if the user wants to perform another calculation
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != "yes":
            break

calculator()
