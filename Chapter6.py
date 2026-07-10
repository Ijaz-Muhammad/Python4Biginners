########Functions in PYTHON
### group of statement that peform group of task
### function definition 
def sum(a,b):# a,b are function parameters 
    s = a+b
    return s
s1= sum(4,5) #4,5 are function arguments 
print(s1)


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output)


#average of three numbers
def av_3num(a,b,c):
    av = (a+b+c)/3
    return av

ave = av_3num(4,4,4)
print(ave)

######## Built in functions
print("Ijaz")
##### User define function 
###defult paramenters 
def cal_pr(a=4,b=2):
    print(a*b)
    return a*b

cal_pr(2,3 )

cities =["Islamabad", "karachi", "lahore"]
Heros =["Imrankhan", "QuaidAzam"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(Heros)

def print_singleline(list):
    for el in list:
        print(el, end=" ")
    
print_singleline(cities)
print()
print_singleline(Heros)
print()

##### factorial function 
def fact_n(n):
    sum =1
    for i in range(1,n+1):
        sum *=i
    return sum 
print(fact_n(4))

### function to convert USD to PKR
def USD2PKR(usd):
    return(282*usd)

print(USD2PKR(2)) 

######### assingment 
def odd_or_even(n):
    if n%2 ==0:
        print("EVEN")
    else:
        print("ODD")
odd_or_even(5)



###### Recusion 
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
print("print ----")
def show2(n):
    if(n>5):
        return
    print(n)
    show2(n+1)
show2(1)
print("Factorial ----")
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))

######## pactice question 
def sum_NN(n):
    if(n==0):
        return 0
    return sum_NN(n-1) + n
        

print(sum_NN(6))

###### 
list_apha = ["A", "B","C", "D"]
def print_list(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)

print_list(list_apha)
