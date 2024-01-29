import math

# Dictionary to store custom functions
custom_functions = {}

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number!"
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number!"
    else:
        return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number!"
    else:
        return math.log10(x)

def natural_log(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number!"
    else:
        return math.log(x)

def define_function():
    name = input("Enter function name: ")
    expression = input("Enter function expression (using x): ")
    custom_functions[name] = expression

def evaluate_function(name, x):
    expression = custom_functions.get(name)
    if expression:
        try:
            result = eval(expression, {'x': x})
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Function not found!"

def print_custom_functions():
    print("Custom Functions:")
    for name, expression in custom_functions.items():
        print(f"{name}(x) = {expression}")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Factorial")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")
print("11. Logarithm (base 10)")
print("12. Natural Logarithm")
print("13. Define Custom Function")
print("14. Print Custom Functions")

while True:
    choice = input("Enter choice (1-14): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '4' and num2 == 0:
            print("Error! Division by zero!")
        else:
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))
    elif choice in ('6', '7'):
        num = int(input("Enter a non-negative integer: "))

        if num < 0:
            print("Error! Please enter a non-negative integer.")
        else:
            if choice == '6':
                print("Result:", square_root(num))
            elif choice == '7':
                print("Result:", factorial(num))
    elif choice in ('8', '9', '10'):
        angle = float(input("Enter an angle in degrees: "))
        
        if choice == '8':
            print("Result:", sin(angle))
        elif choice == '9':
            print("Result:", cos(angle))
        elif choice == '10':
            if abs(math.cos(math.radians(angle))) < 1e-9:
                print("Error! Tangent undefined for this angle.")
            else:
                print("Result:", tan(angle))
    elif choice in ('11', '12'):
        num = float(input("Enter a positive number: "))

        if num <= 0:
            print("Error! Please enter a positive number.")
        else:
            if choice == '11':
                print("Result:", log(num))
            elif choice == '12':
                print("Result:", natural_log(num))
    elif choice == '13':
        define_function()
    elif choice == '14':
        print_custom_functions()
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
