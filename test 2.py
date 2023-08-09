def check_area (area):
    if area >=10 :
        print("Area is bigger than 10 ")
    elif area < 10 :
        print("Area is smaller than 10")
    else :
        print ("Invalid area")
def square():
    x = int(input("Enter number :"))
    area = x * x
    cal = x * 4
    print (area,cal)
    check_area(area)
square()
def triangle ():
    y = int(input("Enter len base: "))
    z = int(input("Enter height: "))
    a = int(input("Enter watar: "))
    cal = 0.5*y*z
    area = y+z+a
    print(cal,area)
    check_area(area)
triangle()

def ask_for_name (current_year:int):
    year_of_birth = input("Enter your year of birth : ")
    age = current_year - int(year_of_birth)
    print(age)
ask_for_name (2023)

def add_numbers(*args):
    total = sum(args)
    print(total)
add_numbers(10,20,30)


def add(num1,num2):
    total = num1 + num2
    return total
num1 = int(input("Enter num 1 :"))
num2 = int(input("Enter num 2 :"))
print(add(num1,num2))