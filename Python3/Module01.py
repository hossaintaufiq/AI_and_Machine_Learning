# name= "Hossain Ahmmed "
# age= 25

# is_adult = True 
# print("My name is "+ name + "and I am " + str(age) + " years old")


# name = input("Enter your name: ")
# age = input ("Enter your age: ")
# is_adult = False; 

# if int(age)>18:
#     is_adult = True

# print("Name: "+name + "Age: "+ age + " Is Adult: " + str(is_adult))    


# loop 

# i=1; 

# while i<=10: 
#     print(i)
#     i+=1 
# print("loop ended")


# for LOOP 

# for i in range(1,11):
#     print(i)
# print("loop ended")


# function set 

def calculator (num1, num2, operator): 
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2 
    elif operator == "*":
        return num1 * num2 
    elif operator == "/":
        if num2 != 0:
            return num1 / num2 
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("Result: " + str(result))