#Write a Python program to create a tuple
a = ()
print(type(a))

#Write a Python program to create a tuple with different data types
a = ('yash', 458, 14.2, [12,54,89,5], {'a': 45, 'b': 4584})
print(a)

#Write a Python program to create a tuple with numbers and print one item.
a = (1,5,9,3,78,4)
for i in a:
   print(i)

for j in range(len(a)):
   print(a[j])

#Write a Python program to unpack a tuple in several variables
a = (1,5)

z, x = a
print(z, x)

#Write a Python program to add an item in a tuple
a = (1,5)
z = 7

a = a + (z,)
print(a)

#Write a Python program to convert a tuple to a string

a = (1,5,9,3,78,4)

s = ''
for item in a:
   s = s + str(item)
print(s)

# Write a Python program to get the 4th element and 4th element from last of a tuple

a = (1,5,9,3,78,4)

print(f"4th element {a[3]}")
print(f"4th element {a[-4]}")

#Write a Python program to find the repeated items of a tuple.

a = (1,5,9,3,78,4,1)
b = ()
for item in a:
   if item not in b:
      b += (item,)
print(b)

b = set(a)
print(b)

#Write a Python program to check whether an element exists within a tuple.

a = (1,5,9,3,78,4,1)
n = 5

if n in a:
   print(True)
else:
   print(False)

#Write a Python program to convert a list to a tuple.

a = [1,2,3,4,5,6,7]
a = tuple(a)
print(a)

#Write a Python program to remove an item from a tuple
#Write a Python program to slice a tuple.
a = (1,5,9,3,78,4,1)
n = 5

a = a[:a.index(n)] + a[a.index(n) + 1:]
print(a)


#Write a Python program to find the index of an item of a tuple.
a = (1,5,9,3,78,4,1)
n = 5

print(a.index(n))

#Write a Python program to find the length of a tuple.
a = (1,5,9,3,78,4,1)

print(len(a))
#Write a Python program to convert a tuple to a dictionary.
a = ((1,5),(9,3),(78,4))

a = dict(a)
print(a)

#Write a Python program to reverse a tuple.
a = (1,5,9,3,78,4,1)

a = a[::-1]
print(a)

#Write a Python program to convert a list of tuples into a dictionary.
a = [('a',1), ('b', 2)]

a = dict(a)
print(a)

#Write a Python program to print a tuple with string formatting.
#Sample tuple : (100, 200, 300)
#Output : This is a tuple (100, 200, 300)

a = (1,5,9,3,78,4,1)

print("This is a tuple {}".format(a))

#Write a Python program to count the elements in a list until an element is a tuple.

a = ['a', 45, 480.55, {'a':45}, [1,2,4,5], (12,748)]
count = 0
for item in a:
   if type(item) == tuple:
      break
   else:
      count += 1
print(count)

#Write a Python program convert a given string list to a tuple. Go to the editor
#Original string: python 3.0
#<class 'str'>
#Convert the said string to a tuple:
#('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
#<class 'tuple'>

a = 'python 3.0'
b = tuple()
for item in a:
   b = b + (item,)

print(b)

#Write a Python program calculate the product, multiplying all the numbers of a given tuple.
#Original Tuple:
#(4, 3, 2, 2, -1, 18)
#Product - multiplying all the numbers of the said tuple: -864
#Original Tuple:
#(2, 4, 8, 8, 3, 2, 9)
#Product - multiplying all the numbers of the said tuple: 27648

a = (4, 3, 2, 2, -1, 18)
res = 1
for item in a:
   res = res * item
print(res)

# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
#Original Tuple:
#((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
#Average value of the numbers of the said tuple of tuples:
#[30.5, 34.25, 27.0, 23.25]
#Original Tuple:
#((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#Average value of the numbers of the said tuple of tuples:
#[25.5, -18.0, 3.75]

a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

tot = 0
length = 0

for i in a:
   length = len(i)
   add = sum(i)

   av = add/length
   print(av)

#Write a Python program to convert a tuple of string values to a tuple of integer values.
#Original tuple values:
#(('333', '33'), ('1416', '55'))
#New tuple values:
#((333, 33), (1416, 55))

a = (('333', '33'), ('1416', '55'))
b = tuple()
for i in a:
   for j in i:
      b = b + (int(j),)

print(b,a)

#Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
#Original tuple:
#(1, 2, 3)
#Convert the said tuple of positive integers into an integer:
#123
#Original tuple:
#(10, 20, 40, 5, 70)
#Convert the said tuple of positive integers into an integer:
#102040570

a = (1, 2, 3)
s = ''
for i in a:
   s = s + str(i)
print(int(s))

#Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
#Original list:
#(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
#Check if White presenet in said tuple of tuples!
#True
#Check if White presenet in said tuple of tuples!
#True
#Check if Olive presenet in said tuple of tuples!
#False

a = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
check = 'Red'

for i in a:
   if check in i:
      print(True)

#Write a Python program to compute element-wise sum of given tuples. Go to the editor
#Original lists:
#(1, 2, 3, 4)
#(3, 5, 2, 1)
#(2, 2, 3, 1)
#Element-wise sum of the said tuples:
#(6, 9, 8, 6)

a = (1, 2, 3, 4)
b = (3, 5, 2, 1)
c = (2, 2, 3, 1)

d = tuple()

for i, j, k in zip(a,b,c):
   add = i + j + k
   d = d + (add,)

print(d)

#Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. Go to the editor
#Original list of tuples:
#[(1, 2), (2, 3), (3, 4)]
#Sum of all the elements of each tuple stored inside the said list of tuples:
#[3, 5, 7]
#Original list of tuples:
#[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
#Sum of all the elements of each tuple stored inside the said list of tuples:
#[9, -1, 7, 8]


a = [(1, 2), (2, 3), (3, 4)]
b = []
for i in a:
   b.append(sum(i))

print(b)

#Write a Python program to remove an empty tuple(s) from a list of tuples.
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

for i in a:
   if len(i) == 0:
      a.remove(i)

print(a)

#Write a Python program to sort a tuple by its float element.
#Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

a = [('item5', '12.20'), ('item2', '11.5'), ('item3', '15.10')]

print(sorted(a, key = lambda x:x[1]))


#Write a Python program to unzip a list of tuples into individual lists.

a = [(1,2),(3,4),(5,6),(7,8)]

b = [list(i) for i in a]

print(b)

#Write a Python program to replace last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print([i[:-1] + (100,) for i in a])
