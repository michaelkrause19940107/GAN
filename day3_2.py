# fruits = ["apple","banana","cherry"]
# for x in fruits:
#     print(x)

# for y in "banana":
#     print(y)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

#   関数の使い方
# def my_function():
#     print("hello")
# my_function()

# def michael(fname):
#     print(fname + "michael")

# michael("krause ")

# def f_l_name(fname, lname):
#     print(fname + " " + lname)
# f_l_name("krause","michael")

# def my_function(*kids):
#     print("the youngest child is " + kids[0])

# my_function("Emil","tobias","Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def tri_recursion(k):
#   if (k > 0) :
#     result = tri_recursion(k-1) * k
#     print(result)
#   else:
#     result = 1
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(10)

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a ** n

# for j in range(5):
#     mydoubler = myfunc(j)
#     for i in range(6):
#         print(mydoubler(i))
# mytripler = myfunc(3)

# for i in range(6):
#     print(mydoubler(i))
#     i += 1

def michael(n):
    return lambda a : a + n

x = michael(1)
print(x(2))