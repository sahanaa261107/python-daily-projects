print("Calculator")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ") 
num2 = float(input("Enter second number: "))        
if op == "+":
    result = num1 + num2
    print("The result is:", result)     
elif op == "-":
    result = num1 - num2
    print("The result is:", result) 
elif op == "*":
    result = num1 * num2
    print("The result is:", result) 
elif op == "/": 
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result) 
    else:
        print("Error: Division by zero is not allowed.")  
else:
    print("Error: Invalid operator.")