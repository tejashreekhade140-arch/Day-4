#FUNCTIONS 

#Simple Text
text =" wlcome to IMCC  "

# 1.removing the spaces from both ends 
print("Remove spaces:",text.strip())

# 2.converts to Upper 
print("Upper Case:", text.upper())

# 3.Converts to Lower case
print("Lower Case:", text.Lower())

# 4.capitalize first letter
text=text.strip()
print("capitilize First Letter:",text.capitalize())

# 5.capitalize each word
print(text.title())

# 6.count occurences of a substring 
print("letter C occurs ",text.count("C"),"times in text")

# 7.find the position of a substring 
print("position of IMCC in text is",text.find("IMCC"))

# 8.replace a substring 
print(text.replace("IMCC","python Magic"))

# 9.check if string starts or ends with certain substring
print(text.startswith("  We"))
print(text.endswith("! "))

# 10.split string into list by a delimeter 
print("simple split", text.split())

# 11.joins  list of strings with a separate 
word=["python","is","fun"]
print(" ".join(word))
