####Object Orianted Programming
"""

To map with real world scenarios, we started using objects in code
This is called OOB
Object -> instence 
"""
# class student:
#     name="Ijaz"
#     age= 32
# s1 =student()
# print(s1)
# print(s1.name)


# class car:
#     color = "blue"
#     brand="mercedes"

# car1=car()
# print(car1.color)
# print(car1.brand)


#####           Constractor 
##### invoke -> execute when object instentiate 
######## init function always invoke 
##### constraction hmesha take parameter 
# the self parameter is a reference to the current instace of the class, and is used to access the variable 
# belongs to the class

# class spouse:
#     ### default constractor
#     def __init__(self):
#         pass
#     ### parametrized constractor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

# s1 =spouse("Ijaz",32)
# s2 =spouse("Samreen", 19)
# print("Hasband name :",s1.name, " age :", s1.age)
# print("Wife name    :",s2.name, " age :",s2.age)


"""

Class and instance Attributes
class.attr
obj.attr
"""
# class student:
#     school = "ABCD school"
#     name = "Unknown"
#     def __init__(self, name, marks):
#         self.name = name # object attributes
#         self.marks=marks

# s1 = student("Ijaz", 88)
# print(s1.name, s1.marks)
# s2 = student("Ijaoo",33)
# print(s2.name, s2.marks)
"""
Methods 
Methods are the functions that belongs to object
"""

# class student:
#     school = "ABCD school"
#     def __init__(self, name, marks):
#         self.name  = name # object attributes
#         self.marks = marks
#     def welcom(self):
#         return self.name

#     def get_marks(self):
#         return self.marks

# s1 = student("Ijaz", 88)
# print(s1.welcom())
# print(s1.get_marks())


###### Question 
# create student class that takes name &marks of 3 objects
## as arguments in constractor , then create a method
## to print the average

# class student:
#     def __init__(self, name, m1,m2,m3):
#         self.name = name 
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def average(self):
#         return self.m3 + self.m2 + self.m1 /3

# s1= student("Ali", 44, 55,66)
# ave = s1.average()
# print(ave)

# class student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
    
#     def get_ave(self):
#         sum = 0 
#         for val in self.marks:
#             sum +=val
#         print("Hi", self.name,"Your ave score is ", sum /3)

# s1= student("Ali", [44,55,66])
# s1.name ="Ijaz"
# s1.get_ave()



"""
static method 
Methods that don't use the self parameter(work at class level)
"""


# class student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
    
#     def get_ave(self):
#         sum = 0 
#         for val in self.marks:
#             sum +=val
#         print("Hi", self.name,"Your ave score is ", sum /3)
    
#     ######### static ,method 
#     @staticmethod  #decorator
#     def hello():
#         print("Hello this is the static method")
# s1= student("Ali", [44,55,66])
# s1.name ="Ijaz"
# s1.get_ave()
# s1.hello()

"""
Important concepts in OOP

Abstraction: Hiding the implementation details of a class
and only showing the essential features to the user
"""
class car:

    def __init__(self):
        self.acc =False
        self.brk = False
        self.cluch=False
    def start(self):
        self.acc=True
        self.cluch=True
        print("car started------")
car1 = car()
car1.start()

"""
Encapsulation: Wrapping data and function into a single unit(object)
"""
###Question 

class SelfAccount:
    
    def __init__(self, balance, acc_no):
        self.balace = balance
        self.acc_no = acc_no

    def debit(self, dedect_mony):
        self.balace= self.balace -dedect_mony
        print("Amount debited = ", dedect_mony)

    def credit(self, add_money):
        self.balace =self.balace+ add_money
        print("Amount crited =", add_money)

    def print_balance(self):
        print("Your account num: ",self.acc_no, "Has Balance =", self.balace)

acc1 = SelfAccount(1000, "Ask020220202")
acc1.debit(500)
acc1.credit(100)
acc1.print_balance()