# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
# This function finds the square root of two numbers
def squareroot(x, y): 
    return x ** y   

print("Select operation.")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")
print("E Square Root")

while True:
    # Take input from the user
    choice = input("Enter choice(A/B/C/D/E): ")

    # Check if choice is one of the five options
    if choice in ('A', 'B', 'C', 'D', 'E'):
       if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

       elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

       elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

       elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))
      
       elif choice == 'E':
            print(num1, "**", num2, "=", squareroot(num1, num2))    
       break
    else:
        print("Invalid Input")
        
