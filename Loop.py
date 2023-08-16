student_count = int(input("Enter the number of students : "))
for i in range(0,student_count):
    mark_count = int(input(f"Enter the number of {i+1} marks : "))
    my_marks = []
    sum = 0
    for a in range (0,mark_count):
        mark = int(input(f"Enter mark {a+1} : "))
        my_marks.append(mark)
        sum += my_marks[a]
    # average = sum(my_marks) / len(my_marks)
    # average = round(average,2)
    print(my_marks)
    print("Average",round(sum / len (my_marks),2))
    print("MAx Mark = ", max(my_marks))
    print("MiN Mark = ", min(my_marks))