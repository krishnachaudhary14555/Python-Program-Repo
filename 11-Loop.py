 #-------Loop -> means doing the same work again and again automatically.--------------------#

''' for Loop -> used to iterate (repeat) over a seuence'''

# 1 Basic Loop
for i in range(1,11):
    print(i)




word = "Python"
for char in word:
    print(char)



# 2 word1 = "SQL"
# for j in range(1,6):
#     print(word1)  # print SQL 5 times


# #  3- Loop through list 
# items = ["Pen","Book","Laptop"]
# for item in items:
#     print(item)



# # 4- Even numbers 
# for j in range(0, 21, 2):
#     print(j)



# # 5- Total Calculation

# marks = [ 78,89,65]
# total = 0
# for m in marks:
#     total+=m
# print("Total : ",total)




# # 6- Clean City Names
# cities = ["MUMbai","PUNE", "chennai"]
# cleaned = []
# for city in cities:
#    cleaned.append(city.strip().title())
# print("Cleaned : ",cleaned)


# # 7- Loop with if condition
# nums = [5,12,3,18,7]
# newList = []
# for n in nums :
#     if( n > 10):
#         newList.append(n)
# print("Greater elements list : ",newList)



# # 8- Extract last digits from IDs
# Ids = ["EMP-001122", " EMP-887765"]
# for emp in Ids:
#     print(emp[-4:])





# # 9- Fixing Spelling Mistakes 

# wrong_list = ["Bengluru","Monbai","Kolkatta"]
# corr_list = []
# for city in wrong_list:
#     corr_list.append(city.replace("Bengluru","Bengaluru").replace("Monbai","Mumbai").replace("Kolkatta","Kolkata"))
# print("Correct List : ",corr_list)




# # 10 - Loopig through Dictionary
# student = {"name":"Satish","age":25,"city":"Pune"}
# for item in student.items():   # item=key,value 
#     # print(key ,":",value)
#     print(item)

   

# # 11- Count vowels in a word 
# name = "Hello Krishna"
# count =0
# vowel= "aeiou"
# for c in name:
#     if c in vowel :
#         count+=1
# print(count)


# # 12 - Calculate average of marks 
# marks = [34,67,90,87]
# sum = 0
# count =0
# for m in marks:
#     sum+=m
#     count+=1
#     avg= (sum/count)
# print(avg)

