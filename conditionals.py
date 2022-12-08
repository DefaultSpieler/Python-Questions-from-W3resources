#Write a Python program to find those numbers which are divisible by 7 and 
#multiple of 5, between 1500 and 2700 (both included)

for i in range(1500, 2701):
	if i % 5 == 0 and i % 7 == 0:
		print(i)
		
#Write a Python program to guess a number between 1 to 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess 
#is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

g_num = 7

while True:
    u_num = int(input("Enter your guess"))
    if u_num == g_num:
        print("Well guessed!")
        break
    else:
        print("You were wrong")
        continue


#Write a Python program that accepts a word from the user and reverse it.

u_in = input("Enter your String")

print(f"Your String {u_in} \n The reversed String {u_in[::-1]}")

#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0

for el in a:
    if el == 0:
        pass
    elif el % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(f"The total count of odd numbers {odd} \n The total count of even numbers {even}")


#Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f"Item {item} \t Type {type(item)}")


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected Output : 0 1 2 4 5   

for el in range(0, 6):
    if el == 3 and el == 6:
        continue
    else:
        print(el, end=" ")

#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Sample Output :
#fizzbuzz
#2
#fizz
#4
#buzz

for i in range(0, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        continue

#Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
#Note :
#i = 0,1.., m-1
#j = 0,1, n-1.

#Test Data : Rows = 3, Columns = 4
#Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]].

#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

a = 'Hello World'
if a == ' ':
    print("Program ended!")
for i in a:
    print(i.lower())

#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
#Sample Data : 0100,0011,1010,1001,1100,1001
#Expected Output : 1010

#Write a Python program that accepts a string and calculate the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2


letters = 0
digits = 0
s = 'Python 3.2'

for i in s:
    if i.isalpha():
        letters = letters + 1
    elif i.isnumeric():
        digits = digits + 1

print(digits)
print(letters)


#Write a Python program to check the validity of password input by users.
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.

import string 

lower_alpha = list(string.ascii_lowercase)
upper_alpha = list(string.ascii_uppercase)
num = '0123456789'
sym = '@#$'

password = 'HelloMy@lien1'

#Write a Python program to get the Fibonacci series between 0 to 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

#Write a Python program to calculate a dog's age in dog's years. Go to the editor
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
#Expected Output:

#Input a dog's age in human years: 15                                    
#The dog's age in dog's years is 73

dog_age = 2

a = 0
for i in range(1,dog_age + 1):
    if i == 1 or i == 2:
        a = a + 10.5
    else:
        a = a + 4

print(f"Dog age in dog years is {dog_age} and that in human years is {a}")

#Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
#Expected Output:

#Input a letter of the alphabet: k                                       
#k is a consonant.

a = 'k'

vowel = 'aeiou'

if a in vowel:
    print("Yes")

#Write a Python program to convert month name to a number of days. Go to the editor
#Expected Output:

#List of months: January, February, March, April, May, June, July, August
#, September, October, November, December                                
#Input the name of Month: February                                       
#No. of days: 28/29 days
