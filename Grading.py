def gradingStudents(grades):
    gradeadd = 0
    if grades < 38:
        print(grades)
    elif grades % 5 == 0:
        print (grades)
    elif grades % 5 != 0:
        while (grades + gradeadd) % 5 != 0 :
            # grades += 1
            gradeadd +=1
        if gradeadd < 3:
            # print ("Rounding Up!")
            print(grades + gradeadd)
        else:
            # print("Not Rounding")
            print(grades)

        # print (grades)
    # print (gradeadd)


# gradingStudents(6)
for x in range(0,101):
    print(f"x is currently {x}")
    gradingStudents(x)


# def gradingStudents(grades):
#     for x in grades:
#         gradeadd = 0
#         if grades[x] < 38:
#             print(grades[x])
#         elif grades[x] % 5 == 0:
#             print (grades[x])
#         elif grades[x] % 5 != 0:
#             while (grades[x] + gradeadd) % 5 != 0 :
#                 # grades += 1
#                 gradeadd +=1
#             if gradeadd < 3:
#                 # print ("Rounding Up!")
#                 print(grades[x] + gradeadd)
#             else:
#                 # print("Not Rounding")
#                 print(grades[x])
import array as arr
# gradingStudents([1,2,3,4,73])
numbers_array = arr.array('i', gradingStudents)
