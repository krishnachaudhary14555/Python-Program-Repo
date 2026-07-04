# -------------- Tuple -------------------#
# tuple is like a permanet list whose value cannot be changed------------------------------#
# -- Ordered and immutable collection----#


# # 1- Create Tuple 
# fruits = ("Apple","Banana","Mango")
# print(fruits)


# # 2-- Indexing 
# print(fruits[0])
# print(fruits[-1])
# print(type(fruits))


# #- 3- Slicing 
# nums = [10, 20, 30, 40, 50]
# print(nums[ 1: 4])


# # - 4- Looping 
# colors = ("Red", "Blue", "Green", "Yellow")
# for  c in colors :
#     print(c)


# # - 5- Tuple  Length 
# colors = ("Red", "Blue", "Green", "Yellow")
# print(len(colors))




# # - 6- Concatenation
# a = ( 1,2 )
# b= (3,4)
# c= a+b
# print(c)


# # *** 7-  Packing and Unpacking
# data = ("Laptop", 45000 , "Black")
# product , price , color = data  # values stores respectively with names
# print(f" Product : {product} \n Price : {price} \n Color : {color}")



# --8 - Nested Tuples Inside List
employees = [("E101", "Rohit","Pune"), ("E102","Sneha","Mumbai")]
for eid,ename,ecity in employees:
    print(eid , ename , ecity)
print(employees[0][1])   # indexing 

