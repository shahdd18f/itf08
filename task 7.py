name = input('Enter Your Name : ')
age = int(input('Enter Your Age :'))
birth = input('Enter Your Birth Day :')

def file_info():

     with open("info.txt" , 'w') as file :
         file.write(f'Name : {name}\n')
         file.write(f'Age : {age}\n ')
         file.write(f'Birthday : {birth}\n')
     file.close()

file_info()