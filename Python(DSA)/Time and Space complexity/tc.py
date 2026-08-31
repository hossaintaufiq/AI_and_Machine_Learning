# for i in range (1,6): 
#     print(i)

age = input("Enter your age: ")
if int(age)>=80 : 
    print("You are eligible for a senior citizen discount.")
elif int(age)>=60 and age<80 : 
    print("You are eligible for a senior citizen discount.")
elif int(age)>24 and age<60 : 
    print("You are eligible for a regular discount.")
elif int(age)>=18 and age<=24 :
    print("You are eligible for a youth discount.")
else: 
    print("You are not eligible for any discount.")
