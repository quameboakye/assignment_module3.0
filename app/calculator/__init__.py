from app.operations import addition, subtraction, multiplication, division


def calculator():
    print("Welcome to the calculator REPL! Type 'exit' to quit.")

    while True:
        user_input = input(
            "Enter an operation (add, subtract, multiply, divide, exit): "
        )

        if user_input.lower() == "exit":
            print("Exiting the calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

            if operation == "add":
                result = addition(num1, num2)
                print(result)

            elif operation == "subtract":
                result = subtraction(num1, num2)
                print(result)

            elif operation == "multiply":
                result = multiplication(num1, num2)
                print(result)

            elif operation == "divide":
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    result = division(num1, num2)
                    print(result)

            else:
                print("Unknown operation")

        except ValueError:
            print(
                "Invalid input. Please follow the format: "
                "<operation> <operand1> <operand2>"
            )