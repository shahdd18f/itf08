def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

def rectangle_area(length, width):
    return length * width

def main_menu() :
    while True:
        print("\nMain menu")
        print("1. Sum")
        print("2. Subtrack")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate triangle area")
        print("6. Calculate circle area")
        print("7. Calculate square area")
        print("8. Exit")

        num = input("Enter your choice (1-8) : ")
        if num == "1" :
             num1 = int(input("Enter Number 1 : "))
             num2 = int(input("Enter Number 2 : "))
             result = num1+num2
             print(result)
        elif num == "2" :
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            result = num1-num2
            print(result)
        elif num == "3":
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            result = num1 * num2
            print(result)
        elif num == "4":
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            result =num1/ num2
            print(result)
        elif num == "5" :
            base = int(input("Enter the base: "))
            height = int(input("Enter the height: "))
            result = triangle_area(base, height)
            print("Triangle Area:", result)
        elif num == "6":
            radius = int(input("Enter the radius : "))
            result = circle_area(radius)
            print("Circle Area:", result)
        elif num == "7":
            radius = int(input("Enter the radius of the circle: "))
            result = circle_area(radius)
            print("Circle Area:", result)

        elif num == "8":
            exit()

        else:
           num = input("Invalid input , Enter valid Again :")


main_menu()