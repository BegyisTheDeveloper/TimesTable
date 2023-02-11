#A timestable program accepting the user's input

print("Times table generator")

num = int(input("Enter a number: "))

for i in range(1, 13):
    print(num, "x", i, "=", num*i)