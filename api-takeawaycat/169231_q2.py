class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade {grade} added for student {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print("No assignments recorded.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID: {student_id}")

    def display_students_and_grades(self):
        print(f"Students and grades for course '{self.course_name}':")
        for student in self.students:
            print(f"\n{student.name} (ID: {student.student_id}):")
            student.display_grades()



def main():
    
    instructor = Instructor("Dr. Smith", "Computer Science 101")

    
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    
    instructor.add_student(student1)
    instructor.add_student(student2)

    instructor.assign_grade("S001", "Assignment 1", 85)
    instructor.assign_grade("S001", "Assignment 2", 90)
    instructor.assign_grade("S002", "Assignment 1", 78)

    
    instructor.display_students_and_grades()

if __name__ == "__main__":
    main()