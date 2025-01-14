class Employee:
    def __init__(self):
        self.name = "Ji-Soo"
        self.age = 38
        self.position = "developer"
        self.salary = 1200


e = Employee()
print(e.__dict__)
