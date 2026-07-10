#list and touple 
#List is the set of data type that stores set of values
#It can store different type of datatypes(Integer, Folat, strings)
marks =[12.2,323.4,23.3,423.2,33.2]
print(marks)
print(type(marks))
print(len(marks))
print(marks[-3:-1])


student = [True, 112, 213.4, "Ijaz"]
print(student[0])



#........................ Difference between ---
# stings vs list. 
# string -immutable 
# list -mutable 

#str = "Hello"
#str[0] = "J"
student[0]= "Muhammad"
print(student)
print(student[2:len(student)])

#Append in python
student.append("Appendedvalue")
print(student)
#Storting 
list = [1,4,6,3,6,8,2]
#sort assending 
print(list.sort())
print(list)
#sort decending
print(list.sort(reverse=True))
print(list)
#Swapp or mirror 
print(list.reverse())
print(list)
#insert value at particular index
print(len(list))
print(list.insert(5,555))
print(list)

#remove the first occurence of element 
list =[1,2,3,4,5,6]
list.remove(2)
print(list)

#remove element at index
list.pop(3)
print(list)


#****************************************
#************ Tuples in python
#Tuples is built in data type that lest create immutable sequences of values
tup = (1,34,5,76,2,1,1,1,8)
print(tup)
print(type(tup))
print(tup[1])

#//tup1= (1,) , after is nessary for show it touple 
tup2 = (1,)
print(tup2)
print(type(tup2))

print(tup.index(5)) # (5) is the value , it will return the index of that value if value exit
print(tup.count(1)) # (1) is the value in the list


"""
Question #1:
"""
#MoveList = ["3 edi0t", "Fana", "Janwar"]
MoveList =[]
#Mov1 = input("Enter the first movie name : ")
#Mov2 = input("Enter the second movie name:")
#Mov3 = input("Enter the third movie name :")
#MoveList.append(Mov1)
#MoveList.append(Mov2)
#MoveList.append(Mov3)
#print(MoveList)
#Palindrome .... back and forward same 
list1 = [1,2,1]
list2 = list1.copy()
list2.reverse()
if(list2 == list1):
    print("palimdrom")
else:
    print("Not palindrom")

# write code to count the student number having A
tup_studnet = ("C","A","B:","A","A","D")
print(tup_studnet.count("A"))
list = ["C","A","B:","A","A","D"]
list.sort()
print(list)