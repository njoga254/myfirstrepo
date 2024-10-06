class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_details(self):
        student_name = f"{self.name} is {self.age} years old."
        return student_name
    
#instances
my_students = student("Lawrence", 25)
print(my_students.student_details())