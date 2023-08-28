class Course:

    def __init__(self, course_id, course_name, course_level):
        self.course_id = course_id
        self.course_name = course_name
        self.course_level = course_level


class Student:

    def __init__(self, student_id, student_name, student_level):
        self.student_id = student_id
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


courses = []
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
        new_student_name = input("Enter Student Name")
        new_student_level = input("Enter Student Level").upper()
        new_student_id = len(students) + 1
        if new_student_level not in ["A", "B", "C"]:
            print("Please Enter a Valid Student Level")
            continue
        new_student = Student(new_student_id, new_student_name, new_student_level)
        students.append(new_student)

        print("Student saved successfully")

    elif choice == "2":
        student_id_r = int(input("Enter Your Student ID"))
        if 0 <= student_id_r <= len(students):
            student_removed = students.pop(student_id_r - 1)
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

    elif choice == "4":
        student_id_d = int(input("Enter your student ID : "))
        if 0 < student_id_d <= len(students):
            student = students[student_id_d - 1]
            student.student_details()

        else:
            print("Invalid ID")

    elif choice == "5":
        course_name_input = input("Enter the new course's name : ")
        course_level_input = input("Enter the new course's level : ")
        new_course_id = len(courses) + 1
        new_course = Course(new_course_id, course_name_input, course_level_input)
        courses.append(new_course)

    elif choice == "6":
        student_id_enroll = int(input("Enter your student ID : "))
        student_level_enroll = input("Enter your level : ")
        course_id_enroll = int(input("Enter your course ID : "))
        if 0 <= student_id_enroll < len(students) and 0 <= course_id_enroll < len(courses):
            student = students[student_id_enroll - 1]
            course = courses[course_id_enroll - 1]
            student.add_course(course)
            print(f"student'{student.student_name}' enrolled in '{course.course_name}' successfully!")
        else:
            print("Enter Valid IDs")

    elif choice == "0":
        print("exiting the program...")
        break

    else:
        print("Enter a valid option...")








