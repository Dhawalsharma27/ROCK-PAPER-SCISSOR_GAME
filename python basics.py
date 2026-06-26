# Varible
# A variable is labelled storage container.It holds data or a value that you can use and. change ,and refernce thoughout your code
# allowed characters = A-z, 0-9,and _
# variable cannot start with number and python is case sensitive
# keywords cannot be used as variable 
name = "Dhawal"
age = 18
print(f"Name is {name} and age is {age}" )
# keyword
# A keyword is the reserved words that have a fixedd, specific meaning. They are the building blocks of the language's syntax
import keyword
from random import random

import lib.module as module
print(keyword.kwlist)
#statements
name1 = "Raj" ; print(name1) 
# Comments 
# Comments are the statments that are completely ignored by the interpreter in python code the line after # is comments

# Indentation matters in python if the code have more indented it will through error

# Data types
# Data types are used to classify and categorize data, telling the interpreter how you intend to use that specific piece of information
print(type(name)) ; print(type(age))
# to check
print(type(name1) == str)
print(isinstance(age,int))
# Typecasting :we can convert from one datatype to another as
number = "80"
age =  int(number)
print(isinstance(age,int))
# other data types : bool for boolean, list for lists, tuple for tuplles, range for ranges, dict for dictionaries, set for sets
# Operators
# opteratos arr the special symbols or keywords used to perform operations on values and variables.
# Arithmetic operators
1 + 1 # Addition operators
2 - 1 # Substraction operators
2 * 2 # Multiplication Operators
4 / 2 # division operators
4 % 3 # modulus operators
4 ** 2 # exponentiation operators
5 // 2 # floor division operators

# + can also used to combine two strings
# += increments the value by given value
age = 20
age += 5
print(age)
# Comparision operators
a = 24
b = 23
print(a == b ,  a != b , a > b , a < b, a <= b , a >= b);
# Boolean operators
condition1 = True
condition2 = False
# not means not true , and means both are true , or means either one is true
print(not condition1, condition1 and condition2, condition1 or condition2) 

# Or operator return the first true value
print( 0 or 1, False or "hey", "hi" or ' hey', [] or False , False or [])

# is and in operators
# is operator checks if two variables point to the same object in memory
# in operator checks if a value is present in a sequence (like a list, tuple, or string)
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return True if age >  18 else False
result1 = is_adult(20)
print(result1)
result2 = is_adult2(17)
print(result2)  

# strings
# A string is a sequence of characters enclosed in single or double quotes. Strings are used to represent text in Python. They can contain letters, numbers, symbols, and whitespace. Strings are immutable, meaning they cannot be changed after they are created.
# Strings can be concatenated using the + operator and repeated using the * operator. They support various methods for manipulation, such as .upper(), .lower(), .strip(), .replace(), and many more. Strings can also be indexed and sliced to access specific characters or substrings.
name = "rocky"
name += " balboa"
age = str(18)
print(f"My name is {name} and I am {age} years old.")
# string operations
print("Beau".upper())#convert all characters to upper case
print("BEAU".lower())#convert all characters to lower case
print("BEAu person".title())#convert the first character of each word to upper case and the rest to lower case
print("BEAu person".islower())#check if all characters are in lower case
print("BEAU".isupper())#check if all characters are in upper case
print("  Beau  ".strip())#remove leading and trailing whitespace
print("Beau".isalpha())#check if all characters are alphabetic
print("Beau123".isalnum())#check if all characters are alphanumeric
print("Beau".replace("B","P"))#replace all occurrences of a substring with another substring
print("Beau".find("a"))#find the index of the first occurrence of a substring
print("Beau".count("e"))#count the number of occurrences of a substring
print("Beau".startswith("B"))#check if the string starts with a specific substring
print("Beau".endswith("u"))#check if the string ends with a specific substring
print("Beau".split("e"))#split the string into a list of substrings based on a delimiter
print(" ".join(["Beau","person"]))#join a list of strings into a single string with a specified delimiter
print("Beau".index("a"))#find the index of the first occurrence of a substring (raises an error if not found)
print("0.123".isdecimal())#check if all characters are decimal characters
print(len("Beau"))#find the length of the string
# Escaping characters: backslash \ is used to escape special characters in a string. For example, if you want to include a double quote inside a string that is enclosed in double quotes, you can use the backslash to escape it:
name = "Dhawal \"The Rock\"" 
print(name)
name = 'Dhawal \nThe Rock'
print(name)
name = "Dhawal \tThe Rock"
print(name)
name = "Dhawal \\The Rock"
print(name)
name = "Rekha"
print(name[1])#accessing a specific character in the string using indexing
print(name[-1])#accessing the last character in the string using negative indexing
print(name[1:4])#slicing the string to get a substring from index 1 to 3
print(name[:4])#slicing the string to get a substring from the beginning to index 3
print(name[2:])#slicing the string to get a substring from index 2 to the end

# boolean
Done = False
if Done:
    print("Task is completed")
else:
    print("Task is not completed")

print(type(Done) == bool)

ingredients_purchased = True
meal_cooked = False
# all function returns True if all elements of the iterable are true (or if the iterable is empty). It is often used to check if multiple conditions are met before proceeding with a certain action.
ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)
# Number data types
num1 = complex(10, 3)
print(num1.real) # prints the real part of the complex number
print(num1.imag) # prints the imaginary part of the complex number

# built-in functions in python
print(abs(-5.6)) # returns the absolute value of a number
print(round(3.14159)) # returns the number rounded to the specified number of decimal places
print(round(3.14159, 2)) # returns the number rounded to the specified number of decimal places
print(max(1, 2, 3, 4, 5)) # returns the largest item in an iterable
print(min(1, 2, 3, 4, 5)) # returns the smallest item in an iterable


# Enum
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.value) # prints the value associated with the RED member of the Color enum
print(Color.GREEN.value) # prints the value associated with the GREEN member of the Color enum
print(Color['BLUE'].value) # prints the value associated with the BLUE member of the Color enum
print(list(Color)) # prints a list of all members of the Color enum
print(len(Color)) # prints the number of members in the Color enum

# User input
age = input("Enter your age: ") # prompts the user to enter their age and stores it as a string
print(f"You entered: {age}") # prints the age entered by the user

#Conditional statements: if-else, elif, nested if-else
condition = True
if condition == True:
    print("The condition")
    print("was True")

else:
    print("The condition")
    print("was False")

#List
Dogs = ["Roger", 1, "syd", True]
# to Print a element of particular index in list we can do
print(Dogs[1])
print(Dogs[1:3])
# we can also print the whole list
print(Dogs)
# in operator
print("syd" in Dogs)
# we can also find the length of the list
print(len(Dogs))
# we can also add elements to the list
Dogs.append("hey")
print(Dogs)
# we can also extend the list with another list
Dogs.extend(["Rahul", 7, False])
print(Dogs)
# another way
Dogs += (["tie",78])
print(Dogs)
# we can replace a element from list
Dogs[1] = (90)
print(Dogs)

# we can remove the ellements from the list
Dogs.remove("Rahul")
print(Dogs)

# pop is  used to remove the last element from the list
print(Dogs.pop())
print(Dogs)

# we can insert elements in the list at a particular index
Dogs.insert(3,"Maxton")
print(Dogs)

# we can sort the list using sort 
items = ["Roger", "Freak" , "lover", "ansh"]
items.sort()
print(items)

# we can copy the list into another list It is provided in sorted order
itemscopy = items[:]
print(itemscopy)

# sorting list
# instead of writting  sorted(items,key = str.lower)
# print(items)

print(sorted(items,key= str.lower))

# Tuples
# tuple is another fundamental python data structure that is used to create group of immutable objects they cannot be modified 
# tuples are defined using parentheses () and can contain elements of different data types. Tuples support indexing and slicing, allowing you to access specific elements or subsets of the tuple. They are often used to represent fixed collections of related data, such as coordinates or RGB color values. Since tuples are immutable, they are generally faster than lists for certain operations and can be used as keys in dictionaries.
Names2 = ("Roger", "Hayad")
Names2[-1]
Names2.index("Roger")
print(len(Names2))

print("Roger" in Names2)
Names2[0:2]
print(sorted(Names2))
newtuple = Names2 + ("tina", "Ruby")
print(newtuple)


# Dictionaries: Dictionaries are unordered collections of key-value pairs. Each key in a dictionary is unique and is used to access its corresponding value. Dictionaries are mutable, meaning you can add, remove, or change their contents after creation. They are defined using curly braces {} with key-value pairs separated by colons.
Dog = {"name" : "Dhawal", "age" : 2 , "colour" : "Green"}
print(Dog["age"])
print(len(Dog))#It will print the len of the dictionary
Dog["age"] = 43
print(Dog)
print(Dog.get("age"))
# items() convert the dictionary into list
print(Dog.items())
# using value() we can get all the values of dictionary
print (Dog.values())
# popitem pop the last element of dictionaries
print(Dog.popitem())

print(Dog.pop("age"))

# Using in to check if name is in dog or not
print( "name" in Dog)

# we can add new item to dictionary using 
Dog["Fav_food"] = "Panner"
print(Dog)

# sets
set1 = {"Dhawal" , "Jay"}
set2 = {"Jay","Luna"}

intersect = set1 & set2
print(intersect)

# union of sets
mod = set1 | set2 
print(mod)

# diffrence bettween two set
diff = set1 - set2
print(diff)

# functions
def Hello(name, age):
    print(f"Hello my name is {name} and I am {age} year old")

Hello("Dhawal", 22)
print(type(age))

# the change inside the function does not affect he values of outside the function
def change(value):
    value = 4

val = 3
change(val)
print(val)

# but in dictionary since it is mutable the changes inside the function reflect outside the function
def change1(value):
    value ["name"] = "Raj"
val1 = {"name" : "Dhawal"}
change1(val1)
print(val1)

#variable scope in functions
def hello(name):
    print(f'"Hello {name} !"')
    return name , "Gomti" , 9
hello("harsh")
print(hello("sid"))
# when we declare a variable outside the function we can use it inside as well as outside the function where if we declare a variable inside we cannot use it outside
age = 90 
def test():
    age = 30
    print(age)

print(age)
test()

# Nested functions: functions defined inside another function are called nested functions.
#  They can access variables from the enclosing function's scope, allowing for encapsulation and organization of code.
#  Nested functions are often used to create closures, where the inner function retains access to the outer function's variables even after the outer function has finished executing.
def talk(phrase):
    # say function is defined inside the talk function, making it a nested function.
    # The say function takes a word as an argument and prints it.
    def say(word):
        print(word)

    #  The talk function splits the input phrase into individual words and calls the say function for each word, effectively printing each word on a new line.
    words = phrase.split(' ')
    #  The talk function splits the input phrase into individual words and calls the say function for each word, effectively printing each word on a new line.
    for word in words:
        say(word)

talk("Hello there! How are you?")

# nonlocal is the keyword used to access the variable of outer function variable inside the nested function without using  nonlocal it is not possible to access the outer variable inside the nested function. 
# It is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# it as global variable. It is used to work with variables inside nested functions, where the variable should not belong to the inner function.
def counter():
    count = 0 

    def increment():
        nonlocal count  # This allows us to modify the 'count' variable from the outer function
        count += 1
        return count

    return increment
increment_counter = counter()
print(increment_counter())  # Output: 1
print(increment_counter())  # Output: 2
print(increment_counter())  # Output: 3

# Objects: Objects are instances of classes that encapsulate data and behavior.
#  They are created from class definitions
age = 8

print(age.bit_length()) # returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros
print(age.real) # returns the real part of a complex number (for integers, it returns the integer itself)
print(age.imag) # returns the imaginary part of a complex number (for integers, it returns
print(id(age)) # returns the memory address of the object

# loops: Loops are used to execute a block of code repeatedly until a certain condition is met.
# Python provides two main types of loops: for loops and while loops. 
# For loops are used to iterate over a sequence (like a list, tuple, or string), while loops continue executing as long as a specified condition is true. Loops can be controlled using break and continue statements, and they can also be nested within each other for more complex iterations.
Count = 0
while Count < 5:
    print("This is a while loop")
    Count += 1
print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)

# it provide index with item
for index, item in enumerate(items):
    print(index, item)

# break and continue
# continue skip the part and continue further
for item in items:
    if item == 2:
        continue
    print(item)

# break stop the loop
for item in items:
    if item == 2:
        break
    print(item)

# classes in python
class Dog:
    def bark(self):
        print("woof!")

roger = Dog()
roger.bark()
print (type(roger))

# constructor in python
class frog:
    #constructor __init__(self):
    # with the help constructor we assign the variables input outside the class by self.varible = pointing varible
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("woof!") #since we dont have any return type it will show none at last if we put the methodd inside the print 


Roger = frog("Roger" ,45 )
print(Roger.age)
print(Roger.name)
Roger.bark()

# Inheritance : In this the lower class inherit the methods of parent class 
class Animal():

    def walk(self):
        print("Walking...")

class cat(Animal):
    def wake(self):
        print("Cat waked up !")

Activity = cat()
Activity.wake()
Activity.walk()

#Modules
#import module #is used to import the module in the current file and we can use the functions of that module by using module name followed by dot and function name
#from module import snake # we can also import the function directly from the module and use it without using module name

# module.snake() # using module name
#snake() # using function name directly since we imported it directly from the module
#from lib import module # we can also import the module from the lib folder and use it by using module name followed by dot and function name
from lib.module import snake # we can also import the function directly from the module and use it without using module name
snake()

# math for math utilities
# os for operating system related tasks
# sys for system-specific parameters and functions
# random for generating random numbers 
# datetime for working with dates and times
# json for working with JSON data
# requests for making HTTP requests, and many more.
# urllib for working with URLs and making HTTP requests
# re for regular expressions and pattern matching
# http for working with HTTP servers 
# You can also create your own modules by defining functions and classes in a separate Python file and importing them into other files as needed.

# import math

# print(math.sqrt(16)) or
from math import sqrt
print(sqrt(16))

import sys
#print(sys.argv) #This will print the list of command line arguments passed to the script, including the script name itself as the first element. If you run this script from the command line with additional arguments, they will be included in the output list. For example, if you run python script.py arg1 arg2, the output will be ['script.py', 'arg1', 'arg2'].
#name = sys.argv[1]
#print("hello " + name) #this will print hello followed by the name passed as command line argument when running the script. For example, if you run python script.py Alice, the output will be "hello Alice". Note that sys.argv[0] is the name of the script itself, so we use sys.argv[1] to access the first argument passed to the script.
import argparse # argparse is a built-in Python library used for parsing command-line arguments. It allows you to define the expected arguments, their types, and help messages, making it easier to create user-friendly command-line interfaces for your scripts. 
# You can specify required and optional arguments, set default values, and handle errors gracefully. 
# The library automatically generates help messages and usage instructions based on the defined arguments, enhancing the usability of your command-line applications.
#we can use argparse for credit card validation, user authentication, file handling, and many other scenarios where you need to accept input from the command line and process it in a structured way. It is a powerful tool for creating flexible and user-friendly command-line interfaces in Python.
parser = argparse.ArgumentParser(
    description="This program demonstrates a simple example of using argparse."
)

parser.add_argument('-c', '--color', type=str, metavar='COLOR', required=True, help='Specify a color', choices=['red', 'green', 'blue']) #-c and --color are the short and long options for the argument, type=str specifies that the argument should be a string, metavar='COLOR' is used to display the name of the argument in the help message, required=True makes this argument mandatory, help='Specify a color' provides a description of the argument for the help message, and choices=['red', 'green', 'blue'] restricts the allowed values for this argument to 'red', 'green', or 'blue'.

args = parser.parse_args()# This line parses the command-line arguments based on the defined arguments in the parser. It processes the input provided by the user when running the script and stores the values in the args variable for further use in the program.
print(f"The specified color is: {args.color}")

# lambda functions: Lambda functions, also known as anonymous functions, are small, unnamed functions defined using the lambda keyword.
#  They can take any number of arguments but can only have one expression. 
# Lambda functions are often used for short, simple operations that can be defined in a single line of code, such as sorting or filtering data. 
# They are commonly used in conjunction with higher-order functions like map(), filter(), and reduce() to perform operations on collections of data without the need for a full function definition.
lambda num : num * 2 # This is a lambda function that takes a single argument num and returns its value multiplied by 2. You can assign this lambda function to a variable for later use, like this: double = lambda num: num * 2. Then you can call the function using double(5), which would return 10.

multiply = lambda a, b : a * b # This is a lambda function that takes two arguments a and b and returns their product. 
# You can assign this lambda function to a variable for later use, like this: multiply = lambda a, b: a * b. Then you can call the function using multiply(3, 4), which would return 12.

print(multiply(3, 4))

# map, filter, and reduce are higher-order functions in Python that allow you to apply a function to a collection of data in a concise and efficient way.
# map() : Map function applies a given function to each item in an iterable (like a list) and returns a new iterable with the results. It is often used for transforming data.
numbers = [2, 3, 4, 5]
def double(num):
    return num * 2
result = map(double, numbers) # This line applies the double function to each element in the numbers list using the map function.
# The result is an iterable (map object) that contains the doubled values of the original list.
print(list(result))

# we can use lambda function with map to make it more concise:

# instead of def double(num): return num * 2, we can use lambda function as:
result = map(lambda num : num ** 2, numbers) # This line applies a lambda function that squares each element in the numbers list using the map function. The result is an iterable (map object) containing the squared values of the original list.
print(list(result)) # This line converts the result (which is a map object) into a

# Filter: The filter function is used to filter elements from an iterable based on a specified condition. It takes a function and an iterable as arguments and returns a new iterable containing only the elements for which the function returns True.
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda num : num % 2 == 0, numbers) # This line uses the filter function to select only the even numbers from the numbers list. The lambda function checks if each number is divisible by 2 (i.e., even). The result is an iterable (filter object) containing only the even numbers.
print(list(result)) # This line converts the result (which is a filter object) into a list and prints it, showing the even numbers from the original list.

# Reduce: The reduce function is used to apply a binary function cumulatively to the items of an iterable, reducing the iterable to a single value. It is part of the functools module in Python. The reduce function takes two arguments: a function and an iterable. The function should take two arguments and return a single value. The reduce function applies this function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda a , b : a + b , numbers) # This line uses the reduce function to calculate the sum of all elements in the numbers list. The lambda function takes two arguments (a and b) and returns their sum. The reduce function applies this lambda function cumulatively to the elements of the numbers list, resulting in a single value that represents the total sum.
print(sum) # This line prints the final result of the reduction, which is the sum of all elements in the numbers list. In this case, it will output 15, as 1 + 2 + 3 + 4 + 5 equals 15.

# Recursion: Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to break down complex problems into simpler subproblems. A recursive function typically has two main components: a base case that stops the recursion and prevents infinite loops, and a recursive case that continues the process by calling the function with modified arguments. Recursion can be an elegant solution for problems that have a natural hierarchical structure, such as tree traversals, factorial calculations, and Fibonacci sequence generation.
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(6))
# In above method the method call itself multiple time to return the value

#Decorators: Decorators are a powerful feature in Python that allow you to modify the behavior of a function or class.
#  They are often used to add functionality to existing code without permanently modifying it.
def logtime(func): #arguments in decorators are the function that is being decorated. In this case, func is the function that will be passed to the logtime decorator when it is applied to another function.
    def wrapper():
        print("before") 
        val = func() # This line calls the original function (func) that is being decorated and stores its return value in the variable val. The wrapper function is responsible for executing the original function and can perform additional actions before or after the function call.
        print("after")
        return val
    return wrapper
@logtime # This line applies the logtime decorator to the hello function. It means that when you call hello(), it will first execute the wrapper function defined inside logtime, which prints "before" and then calls the original hello function.
def hello():
    print("Hello")
hello() # This line calls the hello function, which has been decorated with logtime. When executed, it will print "before", then "Hello" (from the original hello function), and finally "after" (from the wrapper function in the decorator).

# Docstrings: Docstrings, short for documentation strings, are multi-line string literals used to document Python modules, classes, functions, and methods. They are enclosed in triple quotes (""" or ''') and are placed immediately after the definition of a module, class, function, or method. Docstrings provide a convenient way to describe the purpose, behavior, and usage of the code they document. They can be accessed using the __doc__ attribute or with the help() function, making it easier for developers to understand and use the code without needing to read through the implementation details.

def increment(n):
    """Increment a number"""
    return n + 1
print(increment.__doc__) # This line prints the docstring of the increment function, which is "Increment a number"
print(help(increment))

# Annotations : Anotations in Python are a way to attach metadata to function parameters and return values. They provide a means of specifying the expected types of arguments and return values, which can help with code readability, documentation, and static type checking. Annotations are defined using a colon (:) after the parameter name, followed by the type or description. The return type can be specified using the arrow notation (->) after the closing parenthesis of the parameter list. Annotations do not enforce type checking at runtime but can be used by tools like linters and IDEs to provide warnings or suggestions.
def increment(n: int) -> int: # this function sepcifies that it will recieve an int and return a int
    return n + 1

# we can also this with variables
count: int = 0 # this specifies that the variable is of type int

# Exceptions : Exceptions in Python are events that occur during the execution of a program that disrupt the normal flow of the program. 
# They are used to handle errors and other exceptional conditions that may arise during runtime. Exceptions can be caught and handled using try, except, else, and finally blocks.

try: 
    #some lines of code
    result = 2 / 0
except ZeroDivisionError: 
    # If the excepted error occured handle it 
    print('Cannot divide by zero!')
# except <ERROR2>:
    #if another error occured handle it 
# # if any other type that we dont except can be handled
# expect:
# # any type error can be handle using expect 
# else:
    # no exceptions were raised, the code ran successfully
finally:
    # this will run in any case whether error occur 
    result = 1

print(result)

# you can raise Exception by your own using raise function 
try:
    raise Exception('An error!')
except Exception as error:
    print(error)

class DogNotFoundException(Exception): # 
    print("inside")
    pass # means nothing it is used when we define a class with no methods inside it
try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')

# there is way to open read and write the content of the file using try 
# filename ='"C:\Users\DHAWAL\Documents\Code Clusters.pdf"'
# try:
#     file = open(filename,'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close


# but there is another way using with 
# with : 
# with open(filename, 'r') as file:
#     content = file.read()
#     print(content) #close will automatically called

# third party packages in python 
# pip
# pip has 272 packages 
# we can install a package using : pip install packagename
# we can upadte a package to latest version: pip install -U packagename
# we can uninstall a package : pip unistall packagename
# we can check the package: pip show packagename

# List compression: Are way of creating new list from existing list by some syntax. Often prefered over loop to make code more readable
numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

# Polymorphism: Generalize a funcitonality so we can work on diffrent types its a imp concept in oops
class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 =  Cat()

animal1.eat()
animal2.eat()


# Operator overloading: 
class Dogi:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other): #greater than
        return True if self.age > other.age else False
    
roger = Dogi('Roger',9)
syd = Dogi('syd', 8)

print(roger > syd)

# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator 
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator


