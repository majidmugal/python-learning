# Q1. convert to uppercase

# text = input("enter your name: ")
# print(text.upper())


#Q.2 convert to lowercase

# text = input("enter your name: ")
# print(text.lower())


#Q3 String length

# text = input("enter a value: ")
# print(len(text))



#Q4 Hello + Name print 

# name = input("enter your name: ")
# print("Hello" , name )



#Q5 First character print karo

# text = input("input any character: ")
# print(text[0])


#Q6 String reverse
 
#str1 = "hello majid"
#print(str1[:-1])


#Q7 Palindrome check

# text = input("enter a string: ")

# if text == text[::-1] :   
#     print("its palindrome")
# else:
#     print("its not plindrome")



#Q8 Vowels count 
# text = input("Enter a string: ")
# count = 0

# for i in text :
#     if i in "aeiouAEIOU":
#         count += 1
# print(count)



#Q9 Spaces count 

# text = "i love india"
# print(text.count(" " ,))



#Q10 "python" word check karo

# text = input("enter a sting: ")

# if "python" in text.lower() : 
#      print("yes")
# else:
#     print("no")




# Q11 Spaces remove

# text = input("enter a string: " )
# result = text.replace(" ","")
# print(result)



# Q12 Vowels replace karo

text = input("enter a string: ")

result = ""

for i in text:
    if i in "aeiouAEIOU":
        result += "*"
    else:
        result += i

print(result)






