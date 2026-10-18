class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname )

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"welcome  {self.firstname} {self.lastname}to batched {self.graduationyear}")

x = Student("Mike","Oslen",2025)
x.printname()
x.welcome()