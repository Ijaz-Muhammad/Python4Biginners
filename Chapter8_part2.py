##########OOPs part 2
"""
del keyword
used to delete object properties or objec itself 
del s1.name
del s1
# """
# class student:
#     def __init__(self,name):
#         self.name = name

# s1= student("ijaz")
# print(s1.name)
# del s1.name
# print(s1.name)


"""
Private (like) attributes & methods

conceptual implementation in python
Private attributes & methods are meant to be used only within 
the class are not accessible from outside the class
"""
"""
OOP
Private, Public 
"""

###Public class
class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = account("12321", "acdfads")
print(acc1.acc_no, acc1.acc_pass)

###Private class
class account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = account("12321", "abcd")
print(acc1.reset_pass())

###Private class
# class person:
#     __name ="anonymous"

#     def __hello(self):
#         print("Hello person ")

#     def welcome(self):
#        self.__hello()

# p1 = person()
# print(p1.welcome())

## inheritance
"""
When one class (child/derived) derives the properties & method 
of another class(parent/base)
"""
# single inheritence 
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started--")
#     @staticmethod
#     def stop():
#         print("car stop---")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name
    
# car1 = ToyotaCar(Car)
# car2 = ToyotaCar("prius")
# print(car1.start())
# print(car2.color)

# # Multi level inheritence 
# class Car:
#     @staticmethod
#     def start():
#         print("car started--")
#     @staticmethod
#     def stop():
#         print("car stop---")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type



# car1 = Fortuner("disel")
# print(car1.start())

# # multi inheritance
# class A:
#     varA ="Welcom to class A"
# class B:
#     varB = "Welcom to class B"

# class C(A,B):
#     varC = "Welcom to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

## Super method 
# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started--")
#     @staticmethod
#     def stop():
#         print("car stop---")

# class ToyotaCar(Car):
#     def __init__(self,brand,type):
#         super().__init__(type)
#         self.brand = brand
#         super().start()

# c1 = ToyotaCar("ggg","kk")
# print(c1.type)


class student:
    def __init__(self, math, phy,chem):
        self.math = math
        self.phy  = phy
        self.chem = chem

    @property
    def percentage(self):
        return str((self.math + self.phy + self.chem)/3)+"%"

std1 = student(78,66,55)
print(std1.percentage)
std1.math=88
print(std1.percentage)




#### polymorphysim : Operator overloading
## when the same operator is allowed to have different 
## meaning accordin to the context

print(1 + 5)
print(type(1))
print("Muhammad" + "Ijaz")
print(type("Muhammad"))
print([1,2,3,4] + [5,6,7,8])
print(type([1,2,3,4]))

a1 = 1+5j
a2 = 4+6j
print(type(a1))
print(a1+a2)

### complex number create

class complex_no:
    def __init__(self, real, img):
        self.real = real
        self.img  = img
    def showNo(self):
        print(self.real,"i + ", self.img,"j")

    # def add(self, N2):
    def __add__(self, N2):
        newReal = self.real + N2.real
        newImg  = self.img + N2.img
        return complex_no(newReal, newImg)
    def __sub__(self, N2):
         newReal = self.real - N2.real
         newImg  = self.img - N2.img
         return complex_no(newReal, newImg)
    

num1 = complex_no(3,5)
num1.showNo()

num2 = complex_no(4,8)
num2.showNo()
### Operators & Dunder functions 
# num3 = num1.add(num2)
num3 = num1 + num2
num3.showNo()
num4 = num1 - num2
num4.showNo()

###### practice question
class circule: 
    def __init__(self, radius):
        self.radius = radius
    def cir_area(self):
        return (22/7)* self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius

c1 = circule(21)
area =c1.cir_area()
print(area)
peri = c1.perimeter()
print(peri)


#####practice question 

class employ:
    def __init__(self, rol, depart, salary):
        self.rol = rol
        self.depart = depart
        self.salary = salary

    def showDetails(self):
        print("Rol    : ", self.rol)
        print("Depart : ", self.depart)
        print("Salary : ", self.salary)

emp1 = employ("Manager","HR",4444)
emp1.showDetails()        

class Engr(employ):
    def __init__(self,name, age):
        self.name = name
        self.age  = age
        super().__init__("Engieer", "IT", "7777")

eng1 = Engr("Ijaz", 32)
eng1.showDetails()

        
###practice 3

class Order:

    def __init__(self, item, price):
        self.item = item 
        self.price = price
  
    def __gt__(self, order2):
        if(self.price > order2.price):
            print("Order 1 is Greater ")
        elif(self.price == order2.price):
            print("Both are equal price ")
        else:
            print("Order 2 is Greater ")
ord1 = Order("Coffee", 110)
ord2 = Order("Tea", 110)
print(ord1.item, ord1.price)
print(ord2.item, ord2.price)
comp = ord1 > ord2
