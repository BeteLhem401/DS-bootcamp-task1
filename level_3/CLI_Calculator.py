def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    
    choice = input("Choose: ")

    if choice == "5":
        break

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == "1":
        print(add(n1, n2))
    elif choice == "2":
        print(sub(n1, n2))
    elif choice == "3":
        print(mul(n1, n2))
    elif choice == "4":
        print(div(n1, n2))
    else:
        print("Invalid choice")