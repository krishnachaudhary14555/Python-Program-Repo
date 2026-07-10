# -------------- File Handling ----------------------------#
# - File Handling in Pyhton uses the built_in functions: to open(filename,mode) ------#


# # - 1. Reading Full File
# with open("sample.txt","r") as f:
#     print(f.read())

# # 2. Reading data Line by Line
# with open("sample.txt","r") as f :
#     for line in f:
#         print(line.strip().title())



# # 3. Writing (Overwrite) -> create new one if not exist
# with open("notes.txt" , "w") as f:
#        f.write("Day 20 - File Handling")
#        f.write("Read and Learn.")
      


# # 4. Appending
# with open("notes.txt","a") as f:
#     f.write("\n Appending data in notes File")


# # 5 . Cleaning data in file 
# cleaned = []
# with open("sample.txt","r") as f:
#     for line in f:
#         cleaned.append(line.strip().title())
# with open("Cleaned_Output.txt","w") as f:
#     for city in cleaned:
#         f.write(city + "\n")





# 6 . Counting Lines
count = 0
with open("sample.txt","r") as f:
    for _ in f:
        count += 1
print("Total lines : ",count)