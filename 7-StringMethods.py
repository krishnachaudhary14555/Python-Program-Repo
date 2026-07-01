'''
--------------------STRING METHODS --------------
CLeaning , Formatting , Validation , Transformation 
'''
text1 = "       hello python learners     "

'''Remove spaces'''
# print(" Original Text : ",text1) # Original Text :         hello python learners 
# print("Remove Spaces : " , text1.strip())




 # 📙Convert To Capital Letters 
# print( " ALL Capital Letters : " ,text1.upper().strip())  #  HELLO PYTHON LEARNERS





# ✒️------------Convert to Proper Case  -> title()--------

# print("Proper Case : " , text1.title())  #   Hello Python Learners  


# -------------Convert To Capital Letters  -> lower()--------------
# print( " ALL Lower Letters : " ,text1.lower().strip())  #   hello python learners



''' ----------- Replace  ->  .replace( "old" , "new" )---------'''

# print("Replace word Python with SQL  : ",text1.replace("python" ,"SQL"))  #hello SQL learners 


'''------Count occurrences of a letter of word  --> count("char)-----------'''
# print( "Count of l : ", text1.count("l"))  #Count of l :  3





# --------- Check if text starts with something   ---> .startswith("text")
# print(" Starts with hello ? : ", text1.strip().startswith("hello"))        # True





# ------------Check if only numbers are present in data  ---> .isnumeric()
# mobile = "4558662216"
# print(" Is Numeric : ", mobile.isnumeric())   #True


#  ---------------split string into list of words   ---> .split()
# msg = "Welcome to Python Course"
# words = msg.split()
# print("List of words : ", words)       # ['Welcome', 'to', 'Python', 'Course']



# --------------------join back with hyphen
# joined_text = "-".join(words)
# print("Joined text : ",joined_text) # Welcome-to-Python-Course




# ----------------------# Find position of a letter -> .find("char")
# print("Index of p in msg string : ", msg.find("P")) #11 index


#----------------------- Extract Domain from Email
email = "student@example.com"
# domain = email[email.find("@")+1 : ]
# print("Domain : ",domain)


''' Ends with -> .endswith()  method'''
str = "Hello Python"
# print("String ends with n ? : ", str.endswith("n"))  # True

''' Check string is  contains only alpha : -> .isalpha()'''
# print("String contains alphabets : ",str.isalpha())  # generally it returns true but it contains space " " that's why it returns false






# ----------------------Check if string contains alphabets and numbers both
# str1 = "Hello123"
# print("String contains alpha and num : ",str1.isalnum()) # True



# --------------Advance Example : Clean Price (Remove Special Characters  )---------------
# Example : "Price: $3500/-" --> "3500"
price_text = "Price: $3500/-"
clean_price = price_text.replace("Price", "").replace("$","").replace("/-","").strip()

print("Clean price : ",clean_price)


# clean = price_text[price_text.find("$")+1 : -2]

