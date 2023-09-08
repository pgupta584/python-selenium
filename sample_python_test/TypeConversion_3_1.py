birth_year = input("Enter your year of birth ")
# age = 2023-birth_year // Here birth_year is String So We can't subtract from int
# Converting String into integer
age = 2023 - int(birth_year)
print("Your Age is ", age)
print("----- Add example -----")
first_Number = input("Enter first Number ")
second_Number = input("Enter second Number ")
add = first_Number + second_Number
print("Addition of no is ", add)
# Addition of no is  1020 , Since input is String Not integer - So we need to convert it into int
print("-- After Converting into integer and adding -- ")
add = int(first_Number) + int(second_Number)
print("Addition of no is ", add)
# Adding two float no
a = 10.50
b = 10
sum = a + b
print(sum)
# 20.5
# print("Sum is -- >> "+sum)
# TypeError: can only concatenate str (not "float") to str
# We can't concat int with integer hence converting type
print("Sum is -- >> " + str(sum))
