# ---------------Lists------------------------#
# Ordered , mutable(changable) collection  that can store ,multiple values of different data type#
 # Uses -> Store , Clean , Apply, Replace ,Perform , Represent etc 


# 1- Create Lists 
fruits = ["Apple","Banana","Mango"]
# print(fruits)


# # 2-- Indexing 
# print(fruits[0])
# print(fruits[-1])


# # 3-- Update List
# fruits[1] = "Orange"
# print(fruits)     # ['Apple', 'Orange', 'Mango']


# # 4- Add items 
fruits.append("Papaya")           # add at the end    #['Apple', 'Banana', 'Mango', 'Papaya']
fruits.insert(1,"Leechi")           # insert at index ['Apple', 'Leechi', 'Banana', 'Mango', 'Papaya']
print(fruits)    




# # 5- Remove items 
# fruits.pop(0)
# fruits.remove("Mango")
# print(fruits)





# # 6- Slicing 
# nums = [10, 20, 30, 40, 50, 60]
# print(nums[0:3])
# print(nums[-3:])






# # 7- Looping 
# for f in fruits:
#     print("fruits : ",f)



# 8- Extarct Years 
codes = ["Laptop-2024","Phone-2023"]
years = []
for y in codes:
    years.append(y[-4 : ])
print("Years List : ",years)   #Years List :  ['2024', '2023']
