# If we want to iterate until a condition is false , we can use while loop
# Take one example
age = 20

while age > 18:
    print("Eligible to vote")
    print("Age is --> ", age)
    if age == 20:
        break
print("*****************")
kid_age = 10
while kid_age < 18:
    print("Note Eligible to vote")
    print("Age is --> ", kid_age)
    kid_age = kid_age + 1

print("********$$$$$$$$$$$*********")

voter_age = 20
while voter_age > 18:
    print("Eligible to vote")
    if voter_age > 18:
        voter_age = voter_age - 1
        continue
    if voter_age < 18:
        print("Not Eligible to vote")
        break
