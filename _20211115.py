# python inheritance

# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)
    
# x = person("Michael", "Krause")
# x.printname()

# class Student(person):
#     pass
# x = Student("Mike","Oisen")
# x.printname()



# super function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.birthyear = year

x = Student("Micael", "Krause", 1994)
print(x.firstname + " " +x.lastname+" "+str(x.birthyear))




