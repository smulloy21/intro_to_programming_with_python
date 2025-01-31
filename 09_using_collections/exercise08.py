# Explain why the code below prints different values on lines 3 and 4.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# line 4 provides the index of the first occurance of 'f' from the right 
# FROM WITHIN THE SUBSTRING text[21:35], whereas line 4 does the same, but
# provides the index using the whole string as context
