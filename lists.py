
#1. Write a Python program to sum all the items in a list.

a = [1,2,3,4,5]

add = 0
for item in a:
	add += item

print(f"The sum of all the items in the list {a} is ::::: {add}")

#2. Write a Python program to multiply all the items in a list.

a = [1,2,3,4,5]

mult = 1
for item in a:
	mult *= item
print(f"The multiplication of all the items in the list {a} is ::: {mult}")

#3. Write a Python program to get the largest number from a list.

a = [1,2,3,4,5]

largest = 0
for item in a:
	if item > largest:
		largest = item

print(f"The largest item in the list is {largest}")

#4. Write a Python program to get the smallest number from a list.

a = [-1,2,3,4,5]

smallest = 0
for item in a:
	if item < smallest:
		smallest = item
print(f"The smallest number in the list is :: {smallest}")

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

b = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in b:
	if len(item) >= 2 and item[0] == item[-1]:
		count += 1

print(f"The elements in the list whose length is greater than 1 and have the corner item value same are :: {count}")

#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


#7. Write a Python program to remove duplicates from a list.

a = [1,2,3,4,5, 4]
b = []

for item in a:
	if item not in b:
		b.append(item)

print(f"List after removing duplicates is {b}")

b = list(set(a))
print(f"List after removing duplicates using type casting {b}")

#8. Write a Python program to check a list is empty or not

a = [1,2]

if len(a) == 0:
	print(f"The list is empty")

#9. Write a Python program to clone or copy a list.

a = [1,2,3,4,5]
b = a.copy()
print(b)

#10. Write a Python program to find the list of words that are longer than n from a given list of words.

a = ['assdX', 'fewtrgf', 'da', 's']
n = 2
b = []
for item in a:
	if len(item) > 2:
		b.append(item)

print(f"List {b}")

#11. Write a Python function that takes two lists and returns True if they have at least one common member.

def takeList(li1, li2):

	for item in li1:
		if item in li2:
			return True

a = [1,2,3,4,5]
b = [5,96,3,4,12]

print(takeList(a,b))

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

a.pop(0)
a.pop()
a.pop()
print(a)

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

a = [1,2,3,4,5,6,7,8,9]

for item in a:
	if item % 2 == 0:
		a.remove(item)

print(f"The list after removing all the ven numbers are :: {a}")





