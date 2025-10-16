def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error  Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"
    
a = float(input("Enter The First Number : "))
b = float(input("Enter The Second Number :  "))
operation = input("Enter The Operation : ").lower()
result = calculator(a, b, operation)
print(f"The Result :{result}")    
