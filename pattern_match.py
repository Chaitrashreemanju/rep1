#3X3 MATRIX
for row in range(3):
    for col in range(3):
        print(f"({row},{col} )", end=" ")
    print() 

#
##
###
####
#####
num=5
for row in range(1,num+1):
    print("*"*row)


#####
#### 
###
##
#
num=5
for row in range(num):
    print("*"*(num-row) )   


#####
 ####
  ###
   ##
    #    
num=5
for row in range(num):
     print(" " * row   ,"*"*(num-row))   

    #
   ##
  ###   
 ####
##### 
num=5
for row in range(1,num+1):
     print(" " * (num-row)   ,"*"*(row))   


#
 # 
  #
   #
    #     
num=5
for row in range(num):
    for col in range(num):
        if row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")        
    print()        


    #
   # 
  # 
 # 
#    
num=5
for row in range(1,num+1):
    print("  "*(num-row),"*")


    #
   # #
  # # #
 # # # # 
num=5
for row in range (1,num+1):
    print(" "*(num-row),"* "*row)

# # # # #
 # # # #
  # # # 
   # #
    #
num=5
for row in range(num,0,-1):
    print(" "*(num-row),"* "*row)    

    #
   # #
  # # #
 # # # #
# # # # #
 # # # #
  # # # 
   # #
    # 
num=5
for row in range (1,num+1):
    print(" "*(num-row),"* "*row)  
for row in range(num-1,0,-1):
    print(" "*(num-row),"* "*row)      