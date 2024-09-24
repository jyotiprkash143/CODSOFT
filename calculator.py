
def add(a, b):
    return a + b
def sub(a, b):
    return  a- b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
print("**************welcome")
print("Select operation:[1 for add,2 for substract,3 for mult,4 for division]")


while True:
    
    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("not a valid number plz input correctly. Please enter a number")
            continue

        if choice == '1':
            print(f"addition of {num1} & {num2} is {add(num1, num2)}")
        elif choice == '2':
            print(f"substraction of {num1} - {num2} is {sub(num1, num2)}")
        elif choice == '3':
            print(f"multiplication of{num1} * {num2} is {mult(num1, num2)}")
        elif choice == '4':
            print(f"divison of {num1} / {num2} is {div(num1, num2)}")

        # Check if user wants another calculation
        next = input("you want more: (yes/no): ")
        if next.lower() == 'no':
            break
    else:
        print("Invalid Input")
