# import copy
# # name = input("Enter your name: ")
# # print("Hello,", name)

# # print("Hello", "World", sep=", ", end="!")
# # print(name)

# # for i in range(10):
# #     if i == 5:
# #         break
# #     print(i)

# # for i in range(10):
# #     if i == 5:
# #         continue
# #     print(i)

# # fruits = ["apple", "banana", "cherry"]

# # # len()
# # print(len(fruits))  # Output: 3

# # # id()
# # print(id(fruits))  # Output: Unique ID of the list object

# # # type()
# # print(type(fruits))  # Output: <class 'list'>

# # # range()
# # for i in range(5):
# #     print(i)  


# fruits = ["apple", ["banana"], "cherry"]

# # # Append
# # fruits.append("orange")
# # print(f"Append: {fruits}")

# # # Insert
# # fruits.insert(1, "grape")
# # print(f"Insert: {fruits}")

# # # Remove
# # fruits.remove("banana")
# # print(f"Remove: {fruits}")

# # Copy
# # Shallow Copy
# # fruits_shallow_copy = copy.copy(fruits)
# # fruits_shallow_copy[1] = ["lemon"]  
# # print(f"Shallow Copy: {fruits_shallow_copy}, Original: {fruits}")

# # # Deep Copy
# # import copy
# # fruits_deep_copy = copy.deepcopy(fruits)
# # fruits_deep_copy[1] = "kiwi"  
# # print(f"Deep Copy: {fruits_deep_copy}, Original: {fruits}")

# # number_square_pairs = [(x, x ** 2) for x in range(10)]
# # print("Number-Square pairs:", number_square_pairs)

# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# # Slice from index 1 to 4 
# subset1 = fruits[1:4]  
# print("Positive Slicing:", subset1)

# # Slice with a step
# subset2 = fruits[1:6:2]  
# print("Positive Slicing with Step:", subset2)

# # Slice the last three elements
# subset3 = fruits[-3:] 
# print("Negative Slicing:", subset3)

# # Slice from the second to last to the fourth to last 
# subset4 = fruits[-2:-5:-1]  
# print("Negative Slicing with Reverse:", subset4)

# fruits[1:1] = ["kiwi", "mango"]  
# print("Insert into a Slice:", fruits)

fruits = ["apple" , "banana" , "cherry" , "date" , "elderberry"]

fruits.append("fig")
fruits.insert(1 , "grape")
fruits.remove("banana")
fruits[-2:]

even = [x for x in range(0,20) if(x%2==0)]
print(even)

nested = [[1,2],[3,4],[5,6]]
flatten = [ j for i in nested for j in i]
print(flatten)

from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)

cube = list(map(lambda x: x**3 , numbers))
print(cube)

even = list(filter(lambda x: x%2==0 , numbers))
print(even)

