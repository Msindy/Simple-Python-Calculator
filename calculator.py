# Simple CLI Calculator

# Addition 
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Division
def divide(x, y):
    return x / y

# Multiplication
def multiply(x, y):
    return x * y

#Modulus
def modulus(x,y):
    return(x%y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")
print("5.Modulus")

while True:
    # Accept input from  user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))   
    
        # Check if user wants to perform another operation
        # Break the elif loop if answer is no 
        next_calculation = input("Do you want to proceed with another Calculation? (yes/no): ")
        if next_calculation == "no":
             break
        
       