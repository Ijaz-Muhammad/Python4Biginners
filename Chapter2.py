"""
String representation
"""

str1 = "This is string"
str2 = 'Ijaz'
str3 = """ This is another type"s of string representation """

str4 = "This is a another chapter \n We are learning this chapter"
print(str4)

#String concatination / Entry space is count in length 
final_str = str1 + " " + str2 
print("Final string :" ,final_str)
print("Length of Final String : ", len(final_str))
# Length calculating function 
len1 = len(str2)
print(len(str1))
print(len1)

"""
Indexing in pythonnnnnnnnnnnn
only can access, could not manipulate like str[4] ="2"
"""
str = "Muhammad Ijaz"
# str[starting _idx: ending_idx]
print(str[:8]) # start to 8th index 
print(str[-4:-1]) # From backword count -4th index will not be included
"""
M  u h a m m a d I j a z
-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
""" 
"""
str.endswith("er.") , it means that if string ends with this subsrting 
"""

str1 = "muhammad Ijaz"
print(str1.endswith("z")) # return True / False 
print(str1.capitalize()) # capitalize the First Char
print(str1.replace("Ijaz","Ijooo")) # Replace old string with New
print(str1.find("z"))#return index of char
print(str1.count("m"))#count the char in the string

print("*"*100 )

name = input("Enter Your Name: ")
print(len(name))
print(name.count("$"))
print(name.find("I"))

print("*"*100 )
age = int(input ("Enter the age : "))
if(age >= 18):
    print("You can vote")
    print("can drive")
else:
    print("Cannot vote")


"""
Question 1: even or odd
Question 2: Greates of 3
Question 3: multiple of 7
"""
num1 = int(input("Enter a number: "))
if((num1 %2) ==0):
    print("Even")
else:
    print("Odd")

#-------------
a= 4 
b= 6
c= 5
if(a>b and a >c):
    print("a is greates")

elif(b>a and b>c):
        print("b is greates")
else:
    print("c is greates")

#-----------
x= 47
if(x%7 == 0):
     print("multiple of 7: ")
else:
     print("Not multiple of 7 ")
