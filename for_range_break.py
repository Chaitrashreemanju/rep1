# n NATURAL NUMBERS
# end=int(input("Enter the number:"))
# for num in range(1,end+1):
#     print(num)


# n EVEN NUMBERS 
# end= int(input("Enter the number:"))
# for num in range(1,end+1,2):
#     print(num)   


# MULTIPLICATION TABLE
# num=int(input("Enter the number:"))
# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")    


# PRINT ODD NUMBERS IN REVEERSE ORDER
# for i in range(99,0,-2):
#     print(i)


# FACTORIAL OF A NUMBER
num=int(input("Enter the number:"))
factorial=1
for fact in range(1,num+1):
    factorial=factorial*fact
print(factorial)    


# FIBONACCI SERIES
series=[0,1]
num=int(input("Enter the number:"))
if num==1:
    print(series[0])
elif num==2:
    print(series[1])
else:
    for i in range(num-2):
        fib=series[-1]+series[-2]
        series.append(fib)        
print(fib)


#  program that accepts a string and calculates the number of digits and letters.
string=input("Enter the string: ")
letters=0
digits=0
for char in string:
    if char.isalpha():
        letters+=1
    elif char.isdigit():
        digits+=1
print("Letters are:", letters , "Digits are:", digits)    


# PRIME OR NON-PRIME
num=int(input("Enter the number:"))
if num==1:
    print("NON PRIME")
elif num==2:
    print("PRIME")
else:
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime==True:
        print("PRIME")
    else:
        print("NON PRIME") 



# CHECK IF A COLLECTION IS HOMOGENEOUS COLLECTION OR NOT
collection=eval(input("Enter a collection: "))
homogeneous=True
ref_type=type(collection[0])
for item in collection:
    if type(item)==ref_type:
        homogeneous=False
        break
if homogeneous==True:
    print("Its a homogeneous collection")
else:
    print("Its a hetrogeneous collection")    


# VALIDATE USERNAME AND PASSWORD 
actual_username=input("enter:")
actual_password=input("enter:")
while True:
    username=input("enter the username:")
    if username==actual_username:
        break
for _ in range(3):
    password=input("enter the password:")
    if password==actual_password:
        break
else:
    print("User Blocked")                
