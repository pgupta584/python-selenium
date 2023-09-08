my_list = ["John", 34, True, 12345678, "male"]
# Printing List
print("my_list --> ", my_list)

# Getting List Length
created_list = list(my_list)
print("created_list --> ", created_list)

# Getting length
my_list_length = len(my_list)
print("my_list_length --> ", my_list_length)

# Getting 4th Element from List
print("Getting 4th Element --> ", my_list[3])

# Getting last element
print("Getting last element--> ", my_list[-1])

# Getting 2nd last element
print("Getting 2nd last element -->", my_list[-2])

# Getting item from ranges between 1 & 3 (Last index will be excluded)
print("Getting item from ranges between 1 & 3 --> ", my_list[1:3])

# Getting the items from the beginning to, but NOT including after index (Last index will be excluded)
print("Getting the items from the beginning to, but NOT including --> ", my_list[:3])

# Getting item starting from index till last index
print("Getting item starting from index till last index --> ", my_list[1:])

# list use the in keyword:
if "John" in my_list:
    print("Yes, 'John' is in the list")

# Add Examples ----------------

# Add an item to the end of the list, using append()
my_list.append("Jimmy")
print("my_list with Append --> ", my_list)

# Insert an item at a specified index, use the insert() method
my_list.insert(0, "START")
print("my_list after Insert an item at a specified --> ", my_list)

# Append elements from another list to the current list, use extend() method
last_name = ["LastName", "Corbet"]
my_list.extend(last_name)
print("Extending Current List by adding another list --> ", my_list)

# Using extend() method we can add any iterable object (tuples, sets, dictionaries etc.)
tuple_item = ("tuple1", "tuple2")
my_list.extend(tuple_item)
print("Extending Current List by adding another any item --> ", my_list)

# Remove example -----------

# Removing an Item
my_list.remove("Corbet")
print("After Removing an item, Current List  --> ", my_list)

# Removing an Item - using specified index - pop() method
my_list.pop(0)
print("Removing an Item - using specified index, Current List  --> ", my_list)

# If you do not specify the index, the pop() method removes the last item
my_list.pop()
print("Removing last Item , Current List  --> ", my_list)

# Removing 1st element using index
del my_list[0]
print("Removing last Item , Current List  --> ", my_list)

# Clear the list content - list still remains, but it has no content
my_list.clear()
print("Clearing the list , Current List  --> ", my_list)

# Delete the entire list - this will cause an error because you have successfully deleted the list
# del my_list
# print("Deleting the list , Current List  --> ", my_list)

# Iterating List item using Loop
my_new_list = ["John", 34, True, 12345678, "male"]
print("Iterating List item")
for i in my_new_list:
    print(i)

# Iterating List index using Loop
print("Iterating List index")
for i in range(len(my_new_list)):
    print(i)

# list items by using a while loop
print("Iterating List item using while loop")
i = 0
while i < len(my_new_list):
    print(my_new_list[i])
    i = i + 1

# Shorting List -- TypeError: '<' not supported between instances of 'int' and 'str'
# my_new_list.sort()
# print("Sorting list --> ", my_new_list)

# We can do Sorting in same data type - by default alphabetical order
list_item = ["John", "Tom", "Harry"]
print("Before Sorting list --> ", list_item)
list_item.sort()
print("After Sorting list --> ", list_item)

# Sorting number - by default Ascending order
list_number = [2, 5, 6, 8, 3]
print("Before Sorting list --> ", list_number)
list_number.sort()
print("After Sorting list --> ", list_number)

# Sorting in Descending order
list_item.sort(reverse=True)
print("After Sorting Descending order list --> ", list_item)
list_number.sort(reverse=True)
print("After Sorting Descending order list --> ", list_number)

# Copy List ----------
# Copy list from another list - using copy() method
list_item = ["John", "Tom", "Harry"]
copy_item = list_item.copy()
print("List After Copy --> ", copy_item)

# Copy list from another list - using list method
list_item = ["John", "Tom", "Harry"]
copy_item = list(list_item)
print("List After Copy --> ", copy_item)

# Join/ Combine the List ----------

# Join/Combine two list - Using + Operator
list_item = ["John", "Tom", "Harry"]
list_number = [2, 5, 6, 8, 3]
combined_list = list_item + list_number
print("List After Combined --> ", combined_list)

# Join/Combined two lists is by appending all the items from list2 into list1, one by one
list1 = ["John", "Tom", "Harry"]
list2 = [2, 5, 6, 8, 3]
for x in list2:
    list1.append(x)
print("List After Combined --> ", list1)

# We can use extend() method to combined
list1 = ["John", "Tom", "Harry"]
list2 = [2, 5, 6, 8, 3]
list1.extend(list2)
print("List After Combined --> ", list1)

