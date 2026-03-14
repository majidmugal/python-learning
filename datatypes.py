# data types interview questton




1. Find the type of a variable
#x = "Hello"
#print(type(x))

2. Convert string to integer
#a = "50"
#b = int(a)
# print(b + 10)


3. Find length of list
numbers = [1,2,3,4,5]
print(len(numbers))


4. Add element to list
a = [10,20]
a.append(30)
print(a)



5. Remove duplicates from list
a = [1,2,2,3,4,4]
a = list(set(a))
print(a)


6. Access dictionary value
student = {"name":"Rahul","age":21}
print(student["name"])


7. Check element in list
numbers = [1,2,3,4]
print(3 in numbers)


8. Convert list to tuple
a = [1,2,3]
b = tuple(a)
print(b)


9. Convert tuple to list
a = (10,20,30)
b = list(a)
print(b)


10. Reverse a list
a = [1,2,3,4]
a.reverse()
print(a)
Medium Level (11–20)


11. Find maximum value in list
numbers = [10,20,5,40]
print(max(numbers))


12. Find minimum value
print(min(numbers))


13. Sum of list elements
numbers = [1,2,3,4]
print(sum(numbers))


14. Count occurrences in list
a = [1,2,2,3,2]
print(a.count(2))



15. Merge two lists
a = [1,2]
b = [3,4]

c = a + b
print(c)



16. Sort list
numbers = [4,1,3,2]
numbers.sort()
print(numbers)



17. Find unique elements
a = [1,2,2,3,3,4]
print(set(a))



18. Add key to dictionary
data = {"name":"Aman"}
data["age"] = 22
print(data)


19. Get dictionary keys
data = {"a":1,"b":2}

print(data.keys())



20. Get dictionary values
print(data.values())
Harder Level (21–30)



21. Find common elements in two lists
a = [1,2,3]
b = [2,3,4]

print(set(a) & set(b))



22. Remove element by index
a = [10,20,30]

del a[1]

print(a)



23. Copy a list
a = [1,2,3]
b = a.copy()

print(b)



24. Nested list access
a = [[1,2],[3,4]]

print(a[1][0])

Output
3




25. Dictionary loop
data = {"a":1,"b":2}

for key,value in data.items():
    print(key,value)




26. List comprehension
numbers = [1,2,3,4]

squares = [x*x for x in numbers]

print(squares)




27. Check if list is empty
a = []

if not a:
    print("Empty list")




28. Convert string to list
text = "Python"

print(list(text))

Output

['P','y','t','h','o','n']





29. Join list into string
words = ["I","love","Python"]

sentence = " ".join(words)

print(sentence)




30. Create dictionary from two lists
keys = ["name","age"]
values = ["Rahul",21]

data = dict(zip(keys,values))

print(data)