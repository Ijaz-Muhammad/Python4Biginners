
print ("*"*10, "How to do printing in python ", "*"*10)

print("Helloworld ","My name is ijaz")
print ("*" * 10)
print (22222+1)
t =5
print("t = ", t)

print("*"*10, "How to define the variables in python ","*"*10)
name = "Ijaz"
age = 23
price = 24.5555

print ("name = ", name , "age= ", age, "price = ", price)

print("*"*10, "How to check the data type ","*"*10)
print(type(name))
print(type(age))
print(type(price))
name1 ='Ijazzzzzz'
name2 = "Ijazzzz"
name3 = '''Ijazzzz'''


print('name1=', name1, 'name2=', name2, 'name3=', name3)


age = 20
old = False
kat = None

print(type(age))
print(type(old))
print(type(kat))

print("*"*10, "How to do arthimatic operation ","*"*10)
print("Addition = a +b", "Subtraction  = a - b", "Multiplication = a*b", "Division  = a/b", "modulus = a %b")
a = 8
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print("*"*10, "Multiple Line comment " , "*"*10)
# Hi i am Ijaz 
"""
HI
I am 
Muhammad Ijaz 
"""
# aaa
# fff

# vsdfasd
# adsfas

print("*"*10, "Relational operator ", "*"*10)
a=4
b=5
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

print("*"*10, "Assignment operator", "*"*10)
num1 = 11
num1+=10
print(num1)
num1 -=5
print("num1: ",num1)
print("&"*10, "Logical Operator ", "&"*10)
print(not False)
print(not True)

a=10
b=2
print(not (a>b))
a = True
b = False
print(a and b)
print(a or b)

print("*"*10,"Type conversion", "*"*10)
print("type conversion is automatically ")
print("Type casting is manually ")

a = 2
b = 4.325
sum = a+b
print(sum)
print(type(sum))
print("Type casting is manually ")
a = "2"
b = 4.3
c = int("3")
sum = int(a)+b+c
print(sum)

a= 4.5
b = str(a)
print(b)
print(type (b))


print("*"*30, "Take input from user ", "*"*10)

Name = input("Enter Your name: ")
age = int(input("Enter your age : "))
print("Welcom : ", Name)
print("Your age is : ", age)
print(type(age))
print("Type : ", type(int(age)), age)

print("*"*10, "Practice Question ", "*"*10)
print("Question number 1")
a = int(input("Enter first num: "))
b = int(input("Enter Second num:"))
print("a + b : ", a+b)
print("Question # 2")
a = int(input("Enter the side length of squar box:"))
print("Area of squar box : ", a*a)
print("Question # 3")
 
a = input("Enter value of a : ")
b = input("Enter value of b :")
if a > b: 
    print("Yes a greater then b : ", True)
else:
    print("No a is not greater then b : ", False)
    