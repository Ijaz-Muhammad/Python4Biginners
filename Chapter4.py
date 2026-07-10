#Dictionary in python 

info={
    "name": "Ijaz",
    "languages":["verilog","python","C"],
    "contact": 3465090851,
    "Male":True,
    "Weight":83.2,
    443:234,
    "name":"afasdf"
}
print(info) # print dictionary
print(type(info)) # type of dic
print(info["languages"])#access the word in dic

info["name"]="Muhammad Ijaz"#update key value
info["Hobby"]="Learning" #add more key words 
print(info["name"]) #"Print tht meaning of key"
print(info["Hobby"])#"print the meaning of the key"

"""
Nested Dictionay 
"""

student = {
 "name":"Ashraf",
 "marks":{
     "math":88,
     "Eng":99,
     "urdu":55,
     "chem":89
 },
 "class":"9"

}

print(student)
print(student["class"])
print(student["marks"]["math"])
student["marks"]["phy"]=99
print(student)

print(student.keys()) #only dic keys not nested keys, only outer layer keys
print(list(student.keys()))#Convert keys into list
print(len(list(student.keys())))#length of dictionay
print(student.values()) # all values in the dictionay
print(list(student.values())) # dictionay values into list conversion 
print(student.items())# retun all pairs inform of tuples 
print(list(student.items()))#items inside the list
pairs = list(student.items())
print(pairs[0])
print(student["name"]) # return error 
print("my name is Ijaz")# due to above error this will not run 
print(student.get("name1")) # return non
print("my name is Ijaz")# allong side eeor this line will run 
new_dict = {"city":"Skardu"}
student.update(new_dict)
print(student)





"""
Sets in python 
Def: collection of unordered items
Each element is the set must be unique and immutable 
Set elements are immutable
"""
num ={1,2,3,4,5,5,55}
set2 = {"Skardu",1,3,2,2,2,4,"Ijaz","Ijaz"}
print(num) #only take unique value , ignore repeated values 
print(set2)
print(len(num)) # duplicate value igore 

collection ={} # empy dictionay 
print(type(collection))
settt= set() #empty set
print(type(settt))

############## Set Methods

set1=set()
set1.add(1)
set1.add(4)
set1.add(4)
set1.add(6)
set1.remove(1)
set1.remove(4)
set1.add("Ijaz")
set1.add((1,2,3,4))
#set1.add([2,3,4,5,6,7]) #list cannot add in sets
print(set1)
print(len(set1))
set1.pop()
set1.pop()
print(set1)
set1.clear()
print(set1)

# union and intersection methodd
aset = {1,2,5,6,3,4,5,6}
bset = {2,3,6,7,8,8}
bset.union(aset)
print(bset)
print(aset)
print(aset.union(bset))
print(aset.intersection(bset))


"""
Questions;

"""
ques={
    "table":["a piece of furniture", "list of facts & figure"],
    "cat": "a small animal "
}
print(ques)

classrooms = {"python", "java", "c++", "python", "javascript", "python","c"}
print(classrooms)
print(len(classrooms))

"""
marks ={}
sub1=set()
x = input("enter the marks: ")
marks.update({"Pyh": x})
x = input("enter the mark: ")
marks.update({"chem": x})
x = input("enter the mark: ")
marks.update({"eng": x})
print(marks)

"""
values = {9,"9.0"}
print(values)

values ={
    ("float", 9.0),
    ("int",9)
}
print(values)

