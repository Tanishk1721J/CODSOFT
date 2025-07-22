while True:
    num1 = input("Enter the first number (or type 'exit' to quit): ")
    if num1.lower() == 'exit':
        print("Goodbye! Calculator closing...")
        break

    num2 = input("Enter the second number (or type 'exit' to quit): ")
    if num2.lower() == 'exit':
        print("Goodbye! Calculator closing...")
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input! Please enter numeric values.\n")
        continue

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    op = input("Enter the symbol of the operation (+, -, *, /): ")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.\n")
            continue
        result = num1 / num2
    else:
        print("Invalid operation. Please try again.\n")
        continue

    print(f"Result: {result}\n")
