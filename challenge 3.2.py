'''
2. Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
'''

class Student:
  
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the students by their CGPA in descending order.
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)

    # Return the sorted list of students.
    return sorted_students


# Test the function with different input lists of students.
students = [
    Student("Badri", "123456", 9.8),
    Student("Abdul", "654321", 9.6),
    Student("Tharun", "789012", 8.4),
    Student("Dhanush", "789012", 8.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))

