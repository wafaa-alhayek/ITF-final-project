class Course:
    counter = 1

    def __init__(self, course_name, course_level):
        self.course_id = Course.counter
        Course.counter += 1
        self.course_name = course_name
        self.course_level = course_level


class Student:
    counter = 1

    def __init__(self, student_name, student_level):
        self.student_id = Student.counter
        Student.counter += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == course.student_level:
            self.student_courses.append(course)
            print("course added successfully")
        else:
            print("your level doesn't match the course's level")

    def student_details(self):
        print("Name:", self.student_name)
        print("Class:", self.student_level)
        print("Course:", self.student_courses)


students = []
while True:
    print("Select Choice Please:")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display All Students")
    print("5. Create New Course")
    print("6. Add Course to Student")
    print("0. Exit")
    choice = input("Enter your choice")

    if choice == "1":
        input("Enter Student Name")
        level = input("Enter Student Level").upper()
        if level not in ["A", "B", "C"]:
            print("Please Enter a Valid Student Level")
            continue

        print("Student saved successfully")

    elif choice == "2":
        student_id = int(input("Enter Your Student ID"))
        if 0 <= student_id <= len(students):
            student_removed = students.pop(student_id - 1)
            print(f"Student '{student_removed.student_name}' removed successfully.")
        else:
            print("Enter a Valid student ID")
            continue

    elif choice == "3":
        student_id = int(input("Enter Your Student ID"))
        if 0 <= student_id <= len(students):
            input("Enter Your Updated Name")
            level = input(f"Enter Your Updated Level")
            if level not in ["A", "B", "C"]:
                print("Please Enter a Valid Student Level")
                continue

        else:
            print("Student doesn't exist")








