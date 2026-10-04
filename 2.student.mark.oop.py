class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
    def input(self):
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter name: ")
        self.dob = input("Enter dob: ")
    def describe(self):
        print("Student ID: ", self.student_id)
        print("name: ", self.name)
        print("Date of Birth: ", self.dob)
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.dob}"
class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
    def input(self):
        self.course_id = input("Enter course ID: ")
        self.name = input ("Enter name: ")
    def list(self):
        print("Course ID: ", self.course_id)
        print("Name: ", self.name)
    def __str__(self):
        return f"{self.course_id} - {self.name} "
class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark 
    def input (self):
        self.mark = input(float("Enter mark: "))
    def describe(self):
        print("Student_ID: ", self.student_id)
        print("Course_ID: ", self.course_id)
        print("Mark: ",self.mark)
    def __str__(self):
        return f"{self.student_id} - {self.course_id} - {self.mark}"

Students = []
Courses = []
Marks = []

while True:
    print("\n1.Input student information")
    print("2.Input course information")
    print("3.Input marks")
    print("4.List student")
    print("5.List courses")
    print("6.Show student marks for a course")
    print("0.Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        num_students = int(input("Enter number of students: "))
        for i in range (num_students):
            print("Student", i + 1)
            student = Student("", "", "")
            student.input()
            Students.append(student)
    elif choice == "2":
        num_course = int(input("Enter number of course: "))
        for i in range (num_course):
            print("Course", i+1)
            course = Course("", "")
            course.input()
            Courses.append(course)
    elif choice == "3":
        course_id = input ("Enter Course ID: ")
        found = False

        for course in Courses:
            if course.course_id == course_id:
                found = True
                break
        if not found:
            print("course not found!")
        else:
            print("Enter marks for course ", course_id )

            for student in Students:
                mark_value = float(input("Enter mark for " + student.name + ":" ))
                mark = Mark(student.student_id, course_id, mark_value)
                Marks.append(mark)

    elif choice == "4":
        for student in Students:
            student.describe()

    elif choice == "5":
        for course in Courses:
            course.describe()

    elif choice == "6":
        student_id = input("Enter student ID: ")
        for student in Students:
            if student.student_id == student_id:
                print("\n Student: ", student.name)
                for mark in Marks:
                    if mark.student_id == student_id:
                        print(
                            "Course: ", mark.course_id,
                            "Mark: ", mark.mark
                        )
    
    elif choice == "0" :
        print("End")
        break
   