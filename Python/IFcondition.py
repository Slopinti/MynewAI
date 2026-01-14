print("Select the options:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = int(input("Enter option (1 or 2 or 3 or 4): "))

if option == 1:
    print("You selected addition.")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = a + b
    print(f"The sum of a and b is: {result}")

elif option == 2:
    print("You selected subtraction.")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = a - b
    print(f"The result of a - b is: {result}")

elif option == 3:
    print("You selected multiplication.")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = a * b
    print(f"The result of a * b is: {result}")

elif option == 4:
    print("You selected division.")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = a / b
    print(f"The result of a / b is: {result}")

else:
    print("Invalid option selected.")