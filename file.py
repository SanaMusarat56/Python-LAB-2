class Student:
    school_name = "City Public School"   

    def __init__(self, name, age):
        self.name = name       
        self.age = age         

# Objects banao
s1 = Student("Shazia", 21)
s2 = Student("Ali", 22)

print(s1.name)          
print(s1.school_name)   
print(s2.school_name)   