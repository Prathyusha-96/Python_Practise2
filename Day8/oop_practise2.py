#Write a Python program to import built-in array module and display the namespace of the said module.
import array
for name in array.__dict__:
    print(name)

#Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class Student:
    def __init__(self, rollno, name, section):
        self.rollno = rollno
        self.name = name
        self.section = section

student =  Student(12345, 'nikhil', 'B')
print(student.rollno)
print(student.__dict__)

import json
data = {"key1" : "value1", "key2" : "value2"}
print(type(data))
new_data = json.dumps(data)
print(type(json.loads(new_data)))


from collections import namedtuple

Student = namedtuple('Student', ['age', 'name'])
s = Student('28', 'john')
print(s)

import builtins
help(builtins.abs)
print(builtins.abs(-155))

# Python function student(). Using function attributes display the names of all arguments.
def student(student_id, student_name, student_class):
    return f'student id:{student_id}\nStudent name:{student_name}\nstudent class: {student_class}'
print(student(12345, 'john', '10'))

class Student:
    pass
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(student1, Marks))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(issubclass(Student, object))  #built-in object


class Student:
    student_name = 'john'
    marks = 93
print( f"student name: {getattr (Student, 'student_name')}")
print( f"student marks: {getattr (Student, 'marks')}")
setattr(Student, 'student_name', 'JONY')
setattr(Student, 'marks', 100)
print( f"student name: {getattr (Student, 'student_name')}")
print( f"student marks: {getattr (Student, 'marks')}")






