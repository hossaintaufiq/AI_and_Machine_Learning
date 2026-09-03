# # for i in range (1,6): 
# #     print(i)

# age = input("Enter your age: ")
# if int(age)>=80 : 
#     print("You are eligible for a senior citizen discount.")
# elif int(age)>=60 and age<80 : 
#     print("You are eligible for a senior citizen discount.")
# elif int(age)>24 and age<60 : 
#     print("You are eligible for a regular discount.")
# elif int(age)>=18 and age<=24 :
#     print("You are eligible for a youth discount.")
# else: 
#     print("You are not eligible for any discount.")


nums=[5,6,7,7,1,9 ,111,1,1,5,1,1]

freq_map= {}         #we can use dictionary to store the frequency of each number in the list = dict()

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else: 
        freq_map[nums[i]]=1


print(max(freq_map, key=freq_map.get))  #this will return the key with the maximum value in the dictionary