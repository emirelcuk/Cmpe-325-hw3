

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
