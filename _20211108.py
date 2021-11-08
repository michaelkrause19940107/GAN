# i=0
# while i<100:
#     print(i)
#     i += 1

# def my_function():
#     print("hello from a function")

# my_function()

# Lambdaaaa
# x = lambda a : a+10
# print(x(5))

# f = lambda x : x**2
# i=0
# while i<100:
#     i += 1
#     if f(i) == 100:
#         continue
#     print(f(i))

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i=-1
# while i<100:
#     i += 1
#     if i % 2 == 1:
#         continue
#     print(i)

# for x in range(100):
#     if x == 2:
#         continue
#     print(x**2)


# # coding: utf-8

# # for文で、breakしない
# for x in range(3):
#     print(x)
# else:
#     print('else')

# # for文で、breakする
# for x in range(3):
#     if x == 2:
#         break
#     print(x)
# else:
#     print('else')


# create a CLASS
# class myclass:
#     x=5

# p1=myclass()
# print(p1.x)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1=person("john", 36)

# print(p1.name)
# print(p1.age)

# class person2:
#     name = "john"
#     age = 36
# p2 = person2
# print(p2.name)
# print(p2.age)


# class person:
#     def __init__(michael, name , age):
#         michael.name = name
#         michael.age = age
#     def myfunc(michael):
#         print("hello my name is " + michael.name + " and i'm " + str(michael.age))

# p1=person("michael", 16)
# p1.myfunc()

class Person:
  pass

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname + self.lastname)
    
    def printname2(self):
        print(self.lastname, self.firstname)

x = person("michael","krause")
y = person("smith","onozaki")
x.printname()
y.printname2()
