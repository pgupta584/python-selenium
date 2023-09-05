# If we want to iterate through all the element we can use for loop
# Take one list
sample_list = [1, 4, 7, 10, 12]
# for loop to iterate all
print("Iterate all")
for i in sample_list:
    print(i)

print("Use of Range")
for i in range(0, 10):  # assume range is (a,b) start index a=0 and last element is b=10-1
    print(i)

print("Add Natural no till 10")
addition = 0  # Assume initial summ is = 0
for i in range(1, 11):  # assume range is (a,b) start index a=1 and last element is b=11-1
    addition = addition + i
    # print(i)
print("Sum is --> ", addition)
# Coding indentation is very important in python - please remember
print("*********************")
# Other Range examples
for i in range(11):  # assume range is (a,b) start index a=0 if not given and last element is b=11-1=10
    print(i)

print("*********************")
# Other Range & Increased by no examples
for i in range(1, 11, 2):  # assume range is (a,b) start index a=1 if not given and last element is b=11-1=10
    print(i)  # It will print no by adding 2 to previous no till range ,like in java we do i++,i=i+3 etc
