def gradeBook(studentGrade):
    if studentGrade >= 60 and studentGrade <=69:
        print('this student has D.')
    elif studentGrade >= 70 and studentGrade <=79:
        print('This student has a C.')
    elif studentGrade >= 80 and studentGrade <=89:
        print('this student has a B.')
    elif studentGrade >= 90 and studentGrade <=99:
        print('this student has a A.')
    elif studentGrade >= 50 and studentGrade <= 59:
        print('this student has a F.')

gradeBook(99)