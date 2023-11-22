#1
'''
str = "hellow world!"
print(str)
#2
a = input("Enter num1: ")
b = input("Enter num2: ")
a = int(a)
b = int(b)
sum = a + b
print(sum)

#3
a = int(input("Enter a num: "))
if a > 0:
    print("a num is posetive")
elif a < 0:
    print("a num is negative") 
else:
    print("a num is 0") 

#4
name = input("Enter your name: ")
print(len(name))

#5
list = [2, 4, 5, 8]
n = len(list)
sum = 0
for i in list:
    sum += i
print(sum)
'''
#6 factorial
f = int(input("Enter a num: "))
res = 1
for i in range(f):
    res *= i+1
print (res)    




    