# String --> Sequence of characters
# Kept inside Single or Double quote

str_1 = "Pankaj"
str_2 = "Pankaj Gupta"
str_3 = "My Name is Pankaj Gupta"
str_4 = "Pankaj"
str_5 = "Ranjan"
str_6 = " Space "

print(len(str_1))  # to find String length
print(str_1[0])  # to get Char at certain index = 0
print(str_1[1])  # to get Char at certain index = 1
# print(str_1[6])  # to get Char at certain index = 6 --> IndexError: string index out of range
print(str_1[3:6])  # to get substring --> from index 3 to 6

# Verify String
print(str_1 == str_2)  # Check if str_1 present inside str_2 --> return true if Yes
print(str_1 != str_2)  # Check if str_1 present inside str_2 --> return true if Yes

# Verify Substring
print(str_1 in str_2)  # Check if str_1 present inside str_2 --> return true if Yes
print(str_5 not in str_2)  # Check if str_1 present inside str_2 --> return true if Yes

# Splitting the String
obj = str_2.split(" ")  # Splitting str_3 with Space
print(obj[0])
print(obj[1])

# Trimming String
# Trim space from both side
print("Before Strip --> ", str_6)
strip_obj = str_6.strip()
print("After Strip --> ", strip_obj)
# Trim space only from left
print("Left Strip --> ", str_6.lstrip())
# Trim space only from Right
print("Right Strip --> ", str_6.rstrip())
