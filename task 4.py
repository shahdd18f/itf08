def circle ():
    radious = int(input("Enter Radius: "))
    area =  radious * radious * 3.14
    print(area)
circle()
def triangle ():
    base = int(input("Enter Base: "))
    height = int(input("Enter Height: "))
    area = base * height / 2
    print(area)
triangle()
def square():
    length = int(input("Enter Length : "))
    area = length * length
    print (area)
square()3






while True :
    selection = int(input =("1. Sum "
                              "2. Subtractc\n"
                              "3. Subtract\n"
                              "4. Division\n"
                              "5. Calculate triangle area\n"
                              "6. Calculate circle area\n"
                              "7. Calculate sequare area\n"
                              "8. Exit"))

    if selection == 1 :
        def add(number1, number2):
            return number1 + number2
    elif selection == 2 :
        def add(number1, number2):
            return number1 + number2
    elif selection == 3 :
        def division(number1, number2):
            return number1 / number2
    elif selection == 4 :
        def multipulation(number1, number2):
            return number1 * number2
    elif selection == 5 :
        def triangle ():
            base = int(input("Enter Base: "))
            height = int(input("Enter Height: "))
            area = base * height / 2
            print(area)

    elif selection == 6 :
        def circle():
            radious = int(input("Enter Radius: "))
            area = radious * radious * 3.14
            print(area)
    elif selection == 7 :
        def square():
            length = int(input("Enter Length : "))
            area = length * length
            print(area)
    elif selection == 8 :
        print (Bye)
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))