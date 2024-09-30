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