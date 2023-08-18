def is_palindrome (n):
    org_num = n
    rev_num = 0

    while n > 0 :
        digit = n % 10
        rev_num = rev_num *10 +digit
        n //= 10
        return org_num == rev_num
print(is_palindrome(131))


my_list = [50,450,200,300,150]
def list (my_list : list) :
    print("MAX NUM = " , max(my_list))
    print("MIN NUM = ", min(my_list))
    my_list.sort()
    print(my_list)

list(my_list)