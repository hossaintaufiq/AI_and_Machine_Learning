# name= "Hossain Ahmmed "
# age= 25

# is_adult = True 
# print("My name is "+ name + "and I am " + str(age) + " years old")


name = input("Enter your name: ")
age = input ("Enter your age: ")
is_adult = False; 

if int(age)>18:
    is_adult = True

print("Name: "+name + "Age: "+ age + " Is Adult: " + str(is_adult))    
