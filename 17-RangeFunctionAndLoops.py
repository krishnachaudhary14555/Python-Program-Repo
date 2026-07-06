# ------------ Range()  & Loops ----------#
# - Range is like telling function starts from here, go till there. Synatx : range(start, stop, step)


# for i in range(1 ,5):
#     print(i)



# # -2-  Print even numbers (0-18)
# for i in range(0,20,2):
#     print(i)


# # 3- Count Downs 
# print("\n")
# for i in range(10, 0, -1):
#     print(i)




# # 4- Loop though list using /index
# print("\n 4) Loop through list ")
# items = ["Pen","Book","Laptop"]
# for i in range(len(items)):
#     print(i, items[i])

# for i in items:
#     print(i)


# # -5- Generate Employee IDs
# for i in range(1,6):
#     print("EMP-",i)



# # -6 - Create Years list 
# print("\n 6) Create Years List.")
# years = []
# for i in range(2015, 2026):
#     years.append(i)
# print("Years : ",years)


# # 7- Clean city Names using range
# cities = ["MUMbai", "ALigarh", "aGra","delhi","PATNA"]
# cleaned = []
# for i in range(len(cities)):
#     cleaned.append(cities[i].strip().title())
# print("Cleaned : ",cleaned)


# # 8- Extract last 4 digits from IDs
# ids = ["EMP-001122","EMP-550044","EMP-990011"]
# for i in range(len(ids)):
#     print(ids[i][-4: ])



# - Nested for Loop in range
# for i in range(1,3):
#     for j in range(1 ,3):
#         print(f"i value : {i}, j value : {j}")



