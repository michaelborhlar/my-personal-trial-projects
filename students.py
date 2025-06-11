class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def information(self):
        return f"Students INFORMATION:  NAME: {self.name}  AGE: {self.age}"
    
my_name = str(input('Enter your name: '))
my_age = str(input('Enter your age: '))
info = student(my_name, my_age)
print(info.information())