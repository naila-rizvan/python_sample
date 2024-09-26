# Operator Overloading

class Name:
    def __init__(self):
        self.name = None

    def set_name(self,name):
        self.name =name

    def __add__(self, other):
        return self.name+other.name



f_name = Name()
s_name = Name()

f_name.set_name("Naila")
s_name.set_name("Rizvan")

full_name = f_name + s_name
print(full_name)



# Encapsulation
class Student:
    def __init__(self, name="Rajaram", marks=50):
        self.__name = name
        self.__marks = marks

    def student_data(self):
        print(f"Name: {self.__name} Marks: {self.__marks}")


s1 = Student()
s2 = Student("Bharat", 25)

s1.student_data()
s2.student_data()