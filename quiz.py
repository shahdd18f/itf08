def circle ():
    x = int(input("Enter number : "))
    area =  x*x*3.14
    Calculators = 2*3.14*x
    print(area,Calculators)
    if area >=10 :
        print ("circle big")
    elif area < 10 and 10 and area >0 :

        print ("circle small")
    elif area <= 0 :
        print ("error")
circle()

def triangle ():
    y = int(input("Enter len base: "))
    z = int(input("Enter height: "))
    a = int(input("Enter watar: "))
    area = 0.5*y*z
    sp = y+z+a
    print(sp,area)
    if area >= 10:
        print(" big")
    elif area < 10 and 10 and area>0:

        print(" small")
    elif area <= 0:
        print("error")
triangle()
def square():
    x = int(input("Enter number :"))
    t = x * x
    a = x * 4
    print (t,a)
    if a >= 10:
        print(" big")
    elif a < 10 and a>0:

        print(" small")
    elif a <= 0:
        print("error")
square()