# ITF 08 Final Project
import random

# TODO 1 Enter your name and submission date

print("Shahd fayez kahlout ")

# in Global Scope
students_list = []


def add_newstd():
    std_name = input("Enter Student Name: ")
    while True:
        try:
            std_age = int(input("Enter Student Age: "))
            break
        except:
            print("Invalid Value")
    # Create student object and append
    student = Student(std_name, std_age, student_number)
    students_list.append(student)

    print("Student Added Successfully")


def removed_():
    input_student_num = input("Enter Student Number: ")
    found = False
    for student in students_list:
        if student.student_number == input_student_num:
            students_list.remove(student)
            print('Student Removed')
            found = True
            break

    if not found:
        print('Student not Exist')


# TODO 2 Define Course Class and define constructor with (course_id generated ,course name (user_input) and
# course mark

class Course:

    def __init__(self, course_name, course_mark):
        self.course_id = generate_course_id(self)
        self.course_name = course_name
        self.course_mark = course_mark


# a unique course ID as a counter
id_counter = 0


def generate_course_id(self):
    global id_counter
    id_counter += 1
    return id_counter


class Student:
    # static variable
    total_count = 1

    # a constructor
    def __init__(self, std_name, std_age, student_number):
        self.student_id = random.randint(1000, 9999)
        self.std_name = std_name
        self.std_age = std_age
        self.student_number = student_number
        self.courses_list = []
        self.total_count = Student.total_count
        Student.total_count += 1


# enroll new course to student courses list
def add_course():
    input_student_num = input("Enter Student Number: ")
    for student in students_list[:]:
        if student_number == input_student_num:
            course_name = input("Enter name of course: ")
            course_mark = float(input("Enter mark for course: "))
            course = Course(course_name, course_mark)
            student.courses_list.append(course)
            print("Course Added to Student Successfully")
            break
    else:
        print('Student not Exist')


# method to get_student_details as dict
def get_student_details(self):
    details = {
        "Student ID": self.student_id,
        "Name": self.std_name,
        "Age": self.std_age,
        "Student Number": self.student_number,
        "Courses": [course.course_name for course in self.courses_list]
    }
    return details


# method to get_student_courses
def get_student_courses(self):
    for crs in self.courses_list[:]:
        print(f"Course: {crs.course_name}, Mark: {crs.course_mark}")


# method to get student_average as a value
def get_student_average(self):
    if len(self.courses_list) == 0:
        return 0

    total = 0
    for course in self.courses_list[:]:
        total += course.course_mark

    average = total / len(self.courses_list)
    return average


def find_std(student_number):
    found = False
    if len(students_list) == 0:
        return found
    for student in students_list:
        if student.student_number == student_number:
            found = True

    return found


while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark\n"
                              "6.Exit"))
    except:
        print('Invalid input , enter a valid option:')
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        if not find_std(student_number):

            add_newstd()

        elif find_std(student_number):
            print("student already exists")

    elif selection == 2:
        removed_()


    elif selection == 3:

        # Display Student Details

        input_student_num = input("Enter Student Number: ")
        for student in students_list:
            if student_number == input_student_num:
                details = get_student_details(student)

                print('Student Details:', details)

                break

        else:

            print("Student not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list[:]:
            if student.student_number == student_number:
                average = get_student_average(student)
                print(f"Student Average: {average}")
                break
        else:
            print("Student not Exist")
    elif selection == 5:
        add_course()

    else:
        # TODO 15 call a function to exit the program
        exit()
        print("EXIT PROGRAM")

