

class Myclass:  # class name should be MyClass
  def __init__(self, par1, par2)  # bad indentation
  self.par1 = par1 
  self.par2 = par2 
  def myMethod()  # missing parameters
  print("Method called") # bad indentation

try:
  x = 10 / 0  # division by zero
excep ZeroDivisionError:  # typo in except
  print("Caught division by zero!")

myList = [1, 2, 3
print myList[3]  # syntax error, index out of range

dictExample = {'key1': 'value1', 'key2' 'value2'}  # missing colon
print(dictExample['key3'])  # key error

import math

def calcSqrt(number):
  return mat.sqrt(number)  # typo in math

print(calcSqrt(25))

if 10 in [1, 2, 3, 4, 5]: print("Found it!") else: print("Not found!")  # incorrect syntax

user_input = input "Enter a number: "  # missing parentheses

def no_return(x, y):
  sum = x + y
  # Missing return statement

result = no_return(5, 10)
print("The result is " + result)  # Type error

f = open("non_existent_file.txt")  # File not found error
file_content = f.read()
print(file_content)

for i in ran(10):  # typo in range
print i  # indentation error, missing parentheses

def func1():
  return "Func1"

def func2():
  return "Func2"

result = func3()  # calling an undefined function

if True:
print("True statement")  # bad indentation
else:
print("False statement")  # bad indentation

a == 5  # assignment error
b = 10
if a = b  # incorrect operator
print("Equal values")  # bad indentation

# Ending the file without any error handling
