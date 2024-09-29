# FIRST 10 EVEN NUMBERS
num=2
while(num<=20):
    print(num)
    num+=2


# FIRST 10 ODD NUMBERS
num=1
while(num<=30):
    print(num) 
    num+=2


# FIRST 10 NATURALS NUMBERS
num=1
while(num<=10):
    print(num)
    num+=1 


# FIRST 10 WHOLE NUMBERS
num=0
while(num<10):
    print(num)
    num+=1 
    

# FIRST 10 INTEGERS AND THIER SQUARE
num=1
print("NUM    SQ")
while num<=10:
    print(num,"\t",num**2)
    num+=1


# SERIES 105,98,91,.....7    
num=105
while num>=7:
    print(num)
    num-=7


# SERIES 10,20,30....100
num=10
while num<=100:
    print(num, end=",")
    num+=10


# 10 reversee naturals numbers
num=10
while num>=1:
    print(num)
    num-=1


# # SUM OF FIRST 10 NATURALS NUMBERS
num=1
sum=0
while num<=10:
    sum=sum+num
    num=num+1
print(sum)   


# SUM OF FIRST 10 NATURALS NUMBERS
num=0
sum=0
while num<=20:
    sum=sum+num
    num=num+2
print(sum)  


# USER ENTERED TABLEE
i=0
num=int(input("Enter a number :"))
while i<=10:
    print(num,"*",i,"=" ,num*i)
    i+=1


# EVEN NUMBERS BETWEEN THE USER ENTERED
num1=int(input("ENTER NUM1 : "))
num2=int(input("ENTER NUM2 : "))
while num1<num2:
    if num1%2==0:
       print(num1)
    num1+=1


# SUM OF DIGITS 
integer=int(input("ENTER DIGITS : "))
sum=0
while integer!=0:
    if integer%2==0:
     ld=integer%10
     sum+=ld
    integer=integer//10
print(sum)


#REVERSE THE DIGIT
dig=int(input("Enter the digits:"))
rev=0
temp=dig
while dig!=0:
    ld=dig%10
    dig//=10
    rev=rev*10+ld
if temp==rev:
    print("REVERSE")
else:
    print("NOT A REVERSE")
 
 
# FIBONACCI SERIES
n=int(input("enter:"))
if n==1:
    print("1")
elif    n==2:
    print("1,1")
else:    
    fd=1
    sd=1
    print(fd,end=" ")
    print(sd,end=" ")
    i=2
    while (i<n):
        nd=fd+sd
        print(nd,end=" ")
        fd=sd
        sd=nd
        i+=1    


# EXTRACT MUTABLE AND IMMUTABLE DATA FROM THE LIST 
items=eval(input("ENTER THE ITEMS:"))
mutable=[]
immutable=[]
index=0
while index<len(items):
    char=items[index]
    index+=1
    if type(char) in (list,set,dict):
        mutable.append(char)
    else:
        immutable.append(char)
print("MUTABLE",mutable)
print("IMMUTABLE",immutable)      


# REVERSE A WORD 
word=input("ENTER :")
rev=''
index=0
while index<len(word):
    rev=word[index]+rev
    index+=1
print(rev)    


# EXTRACT UPPER AND LOWWERR CASE FROM STRING
string=input("Enter the string:")
upper=''
lower=''
index=0
while index<len(string):
    char=string[index]
    if char.isupper():
        upper+=char
    else:
        lower+=char
    index+=1        
print("UPPER:",upper)
print("LOWER:",lower)    


# CHECK IN A GIVEN LIST IF A WORD ID PALINDROME OR NOT AND IF ITS A PALINDROME THEN APPEND IT TO A NEXT LIST
words=['asa','gog','dog']
output=[]
index=0
while index<len(words):
    word=words[index]
    if type(word)==str:
        rev=''
        index2=0
        while index2<len(word):
            char=word[index2]
            rev=char+rev
            index2+=1
        if rev==word:
            output.append(word) 
    index+=1       
print(output)            


#CHAR IS KEYS AND ITS ASSCI IS THE VALUE 
word=(input('enter:'))
output={}
index=0
while index<len(word):
    char=word[index]
    if char not in output:
        output[char]=ord(char)
    index+=1
print(output)    


#KEYS ARE CHAR FROM A SENTENCE AND VALUES ARE THE NUMBER OF TIMES THE CHAR OCCUR
word=(input('enter:'))
output={}
index=0
while index<len(word):
    char=word[index]
    if char not in output:
        output[char]=1
    else:
        output[char]+=1
    index+=1
print(output)            


KEYS ARE WORD FROM A SENTENCE AND VALUES ARE THE LENGHT OF WORD 
words=(input('enter:'))
word=words.split()
output={}
index=0
while index<len(word):
    char=word[index]
    if char not in output:
        output[char]=len(char)
    else:
        output[char]+=1
    index+=1
print(output)


# KEY= WORD and VALUE= NUMBER OF TIMES THE WORD REPEATED
line=(input('enter:'))
words=line.split()
output={}
index=0
while index<len(words):
    word=words[index]
    if word not in output:
        output[word]=1
    else:
        output[word]+=1
    index+=1
print(output)   

#CATEGORIES ALL THE FILENAMES WITH RESPECT TO ITS EXTENSION
files=['start.py','demo.py','hello.py','new.py','hello.txt','same.csv','hi.txt']
output={}
index=0
while index<len(files):
    file=files[index]
    item=file.split('.')
    name=item[0]
    ext=item[1]
    if ext in output:
        output[ext]+=1
    else:
        output[ext]=1
    index+=1
print(output)                        

# MAX WORD FROM THE STRING (stores words=key and no of words repeated=values )
line=input("Enter the line:")
output={}
index=0
words=line.split()
while index<len (words):
    word=words[index]
    if word not in output:
         output[word]=1
    else:
         output[word]+=1
    index+=1   
max_val=max(output.values())
print(max_val)
max_word=[]
index2=0
keys=list(output.keys())
while index2<len(keys):
    word=keys[index2]
    value=output[word]
    if value==max_val:
          max_word.append(word)
    index2+=1
print(max_word)           
