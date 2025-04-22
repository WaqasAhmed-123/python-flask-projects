import sys

print(sys.version)

print("\n ----------- \n")

print("Hello, World!")

print("\n ----------- \n")

# if condition
if 5 > 2:
    print("Five is greater than two!")
    print("5 is greater than 2")


print("\n ----------- \n")


# variables
x = 5
x = '5'

y = "Hello, World!"
y = 'hello, world!'

print(x, y)


#comments
"""
This is a comment
written in
more than just one line
"""

print("\n ----------- \n")


#variable types
x = str(3)
y = int(3)  
z = float(3)

print("type of x is ", type(x))

print("\n ----------- \n")


# multiple variable assignments
x, y, z = "A", "B", "C"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "X"
print(x)
print(y)
print(z)


#Unpack a Collection
xx = ("A", "B", "C") #tuple data type
yy = {"name": "User 1", "age": 30} #dict (disctionary) data type
letters = ["A", "B", "C"] #list data type
x, y, z = letters
print(x)
print(y)
print(z)

print("\n ----------- \n")


# print outputs
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)

print("\n ----------- \n")

#functions
def func1():
  print("Line 1 of function")
  print("Line 2 of function")

func1()

def func2(x):
  print("Line 1 of function", x)
  print("Line 2 of function")

func2("hello")

print("\n ----------- \n")


#Global variables
def func3():
  global x
  x = "fantastic"

func3()

print("Python is " + x)



#Data types
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset (can not be changed)
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

print("\n ----------- \n")


#random number generation
import random

print("Random number is",random.randrange(1, 10)) #print 1-10 random number

print("\n ----------- \n")


#multiline string
a = """Lorem ipsum dolor sit ame
t,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(len(a))
print("Lorem" in a)

if "Lorem" in a:
  print("Yes, 'Lorem' is present.")

if "test" not in a:
  print("Not, 'test' is not present.")

#string slicing
print(a[2:5])
print(a[:5]) #show first 5
print(a[5:]) #remove 1st 5
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"

print(a.replace("L", "J")) #L will be replaced with J


print("\n ----------- \n")


#F-string (concatination)
age = 31
txt = f"My name is Waqas, I am {age}"
print(txt)

print("\n ----------- \n")


#List items
list = ["apple", "banana", "cherry", "apple", "cherry"]
print(list)
print(list[1])
print(list[-1]) #negative means start from last
print(list[2:5])

if "apple" in list:
  print("Yes, 'apple' is in the fruits list")

list[1] = "blackcurrant"
list.append("orange")
list.insert(1, "orange")
print(list)

tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print(list)

#removing elements from list
list.remove("orange")
list.pop(0)
del list[-1]
print(list)
list.clear()

print(list)



print("\n ----------- \n")

#Loops of list
list2 = ["apple", "banana", "cherry"]
for x in list2:
  print(x)

for i in range(len(list2)):
  print(list2[i])

i = 0
while i < len(list2):
  print(list2[i])
  i = i + 1


print("\n ----------- \n")

#sorting in list
list3 = [100, 50, 65, 82, 23]
list3.sort()
print(list3)

list3.sort(reverse = True)
print(list3)


print("\n ----------- \n")


#copy list
list4 = list3.copy()
print(list4)

list5 = list3[:]
print(list5)

print("\n ----------- \n")

#list joins
listX = ["a", "b", "c"]
listY = [1, 2, 3]

listZ = listX + listY
print(listZ)

listX.extend(listY)
print(listX)


print("\n ----------- \n")

#dictionar
dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(dict)
print(dict["brand"])
print(dict.keys())
print(dict.values())
print(dict.items())

for x in dict:
  print(x)

dict.update({"year": 2020})
dict["color"] = "red"
dict.pop("colors")
print(dict)


print("\n ----------- \n")


#if-else Conditions
a = 200
b = 330
c = 400
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if a < b and c > a:
  print("Both conditions are True")

if a < b or a > c:
  print("At least one of the conditions is True")

print("\n ----------- \n")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print("\n ----------- \n")


#nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
  else:
    print("Iteration finished!")
else:
    print("Finally finished!")


print("\n ----------- \n")

#functions
def function1(child3, child2 = "child 2", child1 = "child 1"):
  print("The youngest child is " + child3 + " from " + child2 + " and " + child1)

function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("\n ----------- \n")

#Lambda functions
x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print("\n ----------- \n")


#Classes with inheritence
class Person:
  def __init__(self, name, age): #constructor
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"Hello my name is {self.name} and I am {self.age} years old.")

p1 = Person("John", 36)
p1.myfunc()

print("\n ----------- \n")

class Student(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.graduationyear = year

  def welcome(self):
    print(f"Welcome {self.name} ({self.age}), to the class of {self.graduationyear}")

stu = Student("Mike", "30", 2019)

stu.welcome()


print("\n ----------- \n")


#modules importing
import calculatorModule

print(calculatorModule.sum(5,10))
print(calculatorModule.sub(5,10))
print(calculatorModule.mult(5,10))
print(calculatorModule.div(5,10))

print("\n ----------- \n")

from calculatorModule import sum

print(sum(15,10))

print("\n ----------- \n")


#Date module
import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

print("\n ----------- \n")


#Math functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print("min", x)
print("max",y)

x = abs(-7.25)
print("Absolute",x)

x = pow(4, 3)
print("Power of 4",x)

print("\n ----------- \n")

import math

x = math.sqrt(64)
print("Square root of 64",x)

x = 1.6
print("Ceiling function",math.ceil(x))
print("Floor Function",math.floor(x))

print("Pi value is", round(math.pi,2))

print("\n ----------- \n")


#Json parsing
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y)

print("\n ----------- \n")

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\n ----------- \n")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

json.dumps(x, indent=4, sort_keys=True)

print("\n ----------- \n")

#regular expression
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

print("\n ----------- \n")

#need to run following command to install camelcase 
#pip install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


print("\n ----------- \n")

#try catch
try:
  print(aaaa)
except:
  print("Variable aaaa is not defined")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")


print("\n ----------- \n")

username = input("Enter username:")
print("Username is: " + username)