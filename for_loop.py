# EXTRACT ALL THE NUMERIC FROM THE LIST
# items=eval(input("Enter the list:"))
# numeric=[]
# for item in items:
#     if type(item)  in [int,float,complex]:
#         numeric.append(item)
# print(numeric)      


#  EXTRACT ALL THE LOWECASE CHAR FROM STRING 
# string=input("Enter the string:")
# lower=''
# upper=''
# for char in string:
#     if char.islower():
#         lower+=char
# print(lower)    


#  THERE IS A SENTENCE, DISPLAY DICT WHERE IT'S KEYS IS WORDS AND VALUES IS LENGTH OF THAT WORD
# line=input("enter a sentence:")
# words=line.split()
# dict1={}
# for word in words:
#     if word not in dict1:
#         dict1[word]=len(word)
# print(dict1)     

#  MIMIC LENGTH 
# string='srtyuojj'
# count=0
# for i in string:
#     count+=1
# print(count)   

# Collection
# items=eval(input("Enter the collection:"))
# count=0
# for item in items:
#     count+=1
# print(count)    

#GREATEST NUMBER IN COLLECTION
# list1=eval(input("Enter the list of num"))
# max=0
# for num in list1:
#     if num>max:
#         max=num
# print(max)    


##CHAR IS KEYS AND ITS ASSCI IS THE VALUE
# word=(input('enter:'))
# output={}
# for char in word:
#     output[char]=ord(char)
# print(output)


#KEYS ARE WORD FROM A SENTENCE AND VALUES ARE THE LENGHT OF WORD 
# line=(input('enter:'))
# output={}
# words=line.split()
# for word in words:
#     output[word]=len(word)
# print(output)  


# EXTENSTION=KEY and number of file with same extentsion is the value
# files=['start.py','demo.py','hello.py','new.py','hello.txt','same.csv','hi.txt']
# output={}
# for file in files:
#     item=file.split('.')
#     name=item[0]
#     ext=item[1]
#     if ext not in output:
#         output[ext]=1
#     else:
#         output[ext]+=1
# print(output)            


# DISPLAY THE MOST REPEATED WORD FROM STRING
line=input("Enter the line ")
output={}
words=line.split()
for word in words:
    if word in output:
        output[word]+=1
    else:
        output[word]=1
print(output)        
max_val=max(output.values())
print(max_val)
max_word=[]
for key in output:
    value=output[key]
    print(value)
    if value==max_val:
        max_word.append(key) 
print(max_word)           