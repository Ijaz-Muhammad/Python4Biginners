########################
######### Loops in python 
count=1
while True:
     
    if count <=5:
        print("Hello",count)
        count = count+1
    else:
        break

while count >=0:
        print("Count = ",count)
        count -= 1

"""
Question 1: print  1to 100 and 100 t0 1
"""
i =1
print ("Print 1 to 100")
while i<=100:
     print("i  : ", i)
     i +=1
print("Print 100 to 1")
while i>1:
    i -=1
    print('i :',i)
    
print("Print multiplication table for n")
n=4#input("Enter the number of which you want to create table:")
i =0
while i<=10:
     print(n,"*",i, "=" ,n*i)
     i+=1

i =0
print("squar of input ")
while i<=10 :
     print("i = ", i, "i^2","=",i**2)
     i +=1
print("seach for x in tuple using loop")

tuple_1 =(1,4,9,16,36,49,64,36,81,100)
i =1
x =36
while i < len(tuple_1):
    if tuple_1[i]==x:
        print("x = ", tuple_1[i], "index:",i)
    else:
        print("not found yet = ",i)
    i+=1

print("End of")


i =1
while i<10:
     if (i%2==1):
        i+=1
        continue #skip
     print(i)
     i+=1
###########################################################
############## For loop in python
list = [1,2,3,4,5,6,7]
list = ["potato", "ginger", "ladyfinder", "cucumber"]
for val in list:
     print("Value : ", val)

tuplee = (1,2,3,4,5,3,4,6,3,5,667,5)
for num in tuplee:
     if num == 6:
          break
     print("index: ",num)
else:
     print("Loop end")

str ="MuhammadIjaz"

for char in str:
    if(char =="I"):
        print("Found I")
    print(char)
     
print("End")

#############
### Question: print the element of the following list using loop:
######
list = [1,4,9,16,32,64,81,100]
for num in list:
     print(num)
else:
     print("loop ended")

tuple = (1,4,9,16,32,64,81,100, 49)
x= 49
indx =0
for num in tuple:
     if(num == x):
          print("found at index :  ", indx)
          break
     print("Searching")
     indx +=1

#################
### range function , 
#### range(start?,stop, step? )
print(range(5)) # range 

seq = range(10)

for i in range(10) :
     print(i)
print("simple range")
for i in range(2,10) :
     print(i)
print("start specified range")
for i in range(1,101,2) :
     print(i)
print("start , stop specified range")

# Linear search we did before this
####Question 1: print from 1 to 100 and 100 to 1
for i in range(101):
     print(i)
for i in range(100, 0, -1):
     print(i)
for i in range(11):
     print("2 *", i, "=", i*2)

#########pass statement: null statement for future code ,  
for el in range(10):
     pass ### idel loop , empty loop ,  

print("some useful work")

sum =0
n =5
i=1
while i<= 5:
     sum +=i
     i +=1

print("total sum =",sum )

for i in range(6):
     sum  +=i
     
print("Total sum =",sum)



####### Factorial of first n number using for loop
# factorial of n = 3, = 1*2*3= 6
n= 3
fact=1
for i in range(1, n+1):
     fact *= i


print("factorial =", fact)