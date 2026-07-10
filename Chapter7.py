########## file I/O in python 
# f = open("file_name", "mode") //// file_name.txt, r: read, w:write
# data = f.read()
#f.close()


"""
Character   Meaning

'r' : Open for reading (default)
'w' : Open for writing, truncating the file first
'x' : create a new file and open it for writing 
'a' : open for writing, appending to the end of the file if it exit
'b' : binary mode
't' : text mode (default)
'+' : open a disk file for updating(read/write)
"""
########## file reading : 'r' // there must be file before openning
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt","r")
# data = f.read(5) # only 5 number of characters 
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)
# f.close()

############ Writing file  : 'w' /// file create if not exist
# f= open("sample.txt",'w') # this creates new file it is not exist already
# f.write("This is new write file ")
# f.close()

##### append in file : 'a' /// file will create if not exist
# file = open("sample1.txt",'a') # this creates file if not exist if exist then just append at the end
# file.write("This is line #1 \nThis is line # 2")
# file.close()

# file=open("sample1.txt",'a') # this append the file if already exit 
# file.write("\nThis line #3")
# file.close()
######## 'r+', pointer at start-- for read /write /// file must exist for r+ ... this will overwrite the file 

# f = open("demo_r+.txt", 'r+')
# f.write("abcd") # this overwride from start of the index
# data = f.read()
# print(data)

# #### 'w+' for write/read // file can create if not exit before 
# f=open("demo_w+.txt",'w+')
# f.write("w+: Demo example ") 
# data = f.read() # now the pointer will be at the end of txt line so nothing will read
# print(data)

####### 'a+' : read/append -> no truncate 

#### with syntex  // close file is not nessary here, with syntex will do it bydefault 

# with open("demo.txt", 'r') as f:
#     data=f.read()
#     print(data)

# with open("demo.txt", 'w') as f:
#     f.write("Hello this example of with ")

####### Deleting a file 

# import os 
# os.remove("demo.txt") 

###Question 1
# f = open("practice.txt",'w')
# f.write("Hi everyone \nwe are learning File I/O\nusing Java.\nI like programming in Java.")
# f.close
## Question 2: overlape the Java with python

# with open("practice.txt",'r') as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt",'w') as f:
#     f.write(new_data)

###### Question 3: file the word leaning in the txt file 

# def check_for_word():
#     word = input("Enter the word want to find: ")
#     with open("practice.txt",'r') as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found") 
# check_for_word()

#############Question: find the work in line 
# def check_for_line():
#     word = "learning"
#     data = True
#     lineNo =1
#     with open("practice.txt",'r')as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(lineNo)
#             lineNo +=1
#     return -1
            
# check_for_line()
# print(check_for_line())

############## Question : count number seprated by comma

# with open("practice_no.txt",'r') as f:
#     data =f.read()
#     print(data)
#     num =""
#     for i in range(len(data)):
#         if(data[i] ==','):
#             print(int(num))
#             num=""
#         else:
#             num +=data[i]

#######using split method 
count =0
with open("practice_no.txt",'r') as f:
    data =f.read()
    num =data.split(",")
    for value in num:
        if(int(value)%2==0):
            count +=1
print(count)