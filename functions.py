#Write a Python function to find the Max of three numbers

def maxVal(a,b,c):
   if a == b and b == c:
      return "All vals are same"
   elif a > b and a > c:
      return a
   elif b > a and b > c:
      return b
   elif c > a and c > b:
      return c

a = 4
b = 9
c = 8

print(maxVal(a,b,c))

#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

a = (8, 2, 3, 0, 7)

def getSum(a):
   add = 0
   for i in a:
      add = add + i
   return add

print(getSum(a))

#Write a Python function to multiply all the numbers in a list. Go to the editor
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

a = (8, 2, 3, -1, 7)

def getMult(a):
   mul = 1
   for i in a:
      mul = mul * i
      return mul


#Write a Python program to reverse a string. Go to the editor
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

a = "1234abcd"

def rev(a):
   b = ''
   b = a[::-1]
   return b

print(rev(a))

#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument

def fact(a):
   if a == 0:
      return "Factorial is 1"
   elif a < 0:
      return "Factorial does not exists"
   else:
      fact = 1
      for i in range(a, 0, -1):
         fact = fact * i
      return fact

print(fact(5))

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


#Write a Python function to check whether a number falls in a given range.

n = 5
sRange = 1
eRange = 10

def chkRange(n, sRange, eRange):
   if n > sRange and n < eRange:
      return True
   else:
      return False

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

a = 'The quick Brow Fox'

def chkLow(a):
   up, low = 0, 0
   for i in a:
      if i.isupper():
         up += 1
      elif i.islower():
         low += 1
      else:
         pass
   return up, low

print(chkLow(a))

#Write a Python function that takes a list and returns a new list with unique elements of the first list. 
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

a = [1,2,3,3,3,3,4,5]

def setList(a):

   b = []
   for i in a:
      if i not in b:
         b.append(i)
   return b

#Write a Python function that takes a number as a parameter and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1
#and itself.

#Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def getEven(a):
   b = []
   for i in a:
      if a % 2 == 0:
         b.append(i)
   return b

#Write a Python program to find biggest of THREE numbers using function.

def find_greatest(a,b,c):
	if a == b and b == c and c == a:
		return "All the values are same"
	elif a > b and a > c:
		return f"{a} is the greatest value"
	elif b > a and b > c:
		return f"{b} is the greatest"
	else:
		return f"{c} is the greatest"

print(find_greatest(10,5,9))

#Write a Python program using functionthat return absolute value of number.

def absolut(a):
	if a < 0:
		return -a
	else:
		return a

print(absolut(5))

#Write a Python function to sum all the numbers in a list.

a = [1,2,4,5,7,8,9,3]
add = 0
def sum_of(a):
	global add
	for item in a:
		add = add + item
	return add

print(sum_of(a))
print(add)

# Write a Python program to reverse a string.

a = [1,2,4,5,7,8,9,3]

def aa(a):
	return a[::-1]

b = lambda a: a[::-1]
print(b(a))

#Write a Python function to check whether a number is in a given range

start = 0
end = 5
num = 1

def check_in(s,e,n):
	if n > s and n < e:
		return True

print(check_in(start, end, num))

#Write a Python program to print the even numbers from a given list.

a = [1,8,7,-6,2,6,9,-8]

def ch(a):
	b = []
	b = [i for i in a if i > 0]
	return b

print(ch(a))

#Write a Python program that uses lambda function to multiply two numbers

a = lambda x,y : x * y

print(a(5,2))

# Write a Python program that passes lambda function as an argument to another function to compute the cube of a number

a = lambda x : x ** 3
print(a(3))

#Write a Python program using function is_perfect() that returns value 1 if the argument passed to it is a perfect number and 0 otherwise.

def is_perfect(x):
	add = 0
	for i in range(1,x):
		if x % i == 0:
			add = add + i
	if add == x:
		return 1

print(is_perfect(6))

#Write a Python program to calculate the area of a triangle using a function.

def cal_area(b,h):
	area = 1/2 * (b * h)
	return area

print(cal_area(5,4))

#.A function that accepts two values and find their sum

def cal_sum():
	a = 5
	b = 10
	return a + b

print(cal_sum())

#A python program to find the sum of two numbers and return the result from the function

#A function to test whether a number is even or odd

def num(a):
	if a % 2 == 0:
		return True
	else:
		return False

print(num(4))

#A python program to calculate factorial values of numbers

def find_fact(a):
	if a == 1:
		return 1
	else:
		return a * find_fact(a - 1)

print(find_fact(5))

#.A python program to check whethergiven number is prime or not
#Write a Python function to check whether a number is perfect or not. Go to the editor
#According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its 
#proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its 
#aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors 
#(including itself).
#Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
#Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
#The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

#Write a Python function that checks whether a passed string is palindrome or not.
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

#Write a Python function that prints out the first n rows of Pascal's triangle.
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#Sample Pascal's triangle 
#Each number is the two numbers above it added together

# Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a 
#hyphen-separated sequence after sorting them alphabetically. Go to the editor
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow

# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 
#(both included).

#Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python

#Write a Python program to execute a string containing Python code.

# Write a Python program to access a function inside a function

#Write a Python program to detect the number of local variables declared in a function.
#Sample Output:
#3

#Write a Python program that invoke a given function after specific milliseconds. Go to the editor
#Sample Output:
#Square root after specific miliseconds:
#4.0
#10.0
#158.42979517754858
