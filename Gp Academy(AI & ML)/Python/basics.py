# print("Hello world!")
# if 5>2: 
#     print("Five is greater than two!")
# elif 5==2:
#     print("Five is equal to two!")
# else:
#     print("Five is less than two!")


# x=0; 

# if 5>2: 
#     x=5; 

# elif 5<2: 
#     x=10; 

# else: 
#     x=0; 


# print("The value of x is : ", x*5, " and the value of x is : ", x*10);

# x,y,z= " Orange", "Banana", "Cherry"; 

# print(x,y,z)


# functions

# x=10; 

# def sumOfNumbers(): 
#     i=0; 
#     sum=0;
#     while i<10:
#         sum+=i;
#         i+=1;
#     return sum;


   

# print(sumOfNumbers()); 

# def myFunction():
#     print("Hello from a function")


# # print(myFunction()); 
# myFunction();    

# import datetime
# x=datetime.datetime.now(); 
# print(x)

# input 

# print("Enter your name: ")
# name=input(); 
# print("Hello ", name)


import re 

txt = "The rain in the Spain stays mainly in the plain" 

x = re.search("^The.*Spain$", txt)
print(x)