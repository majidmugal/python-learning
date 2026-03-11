# tuple

# number = (1,2,3,4,5)

# print(f"number of tupele : {number}")


# fruits = ("apple", "mango", "cherry")
# print(fruits)



# nested_tuple = (1 , [5,6], "majid")

# nested_tuple[1][0] = 9
# nested_tuple[1][1] = 8

# print(nested_tuple)




# single_element_tuple = (2 ,)

# print(single_element_tuple)


# packed_tuple = 1 , True, "majid"

# print(packed_tuple)


# my_tuple = (0,1,3,4,5,6,7,8,9 )

# print(my_tuple[4])

# print(my_tuple[-2])

# print(my_tuple[:5])

# print(my_tuple[::2])


#repetation

# print(my_tuple * 2)

#membership

# print( 3 in my_tuple) 



# change an element // (show error)

# tuple1 = ("html" , "css" , "javascript")

# tuple1[1] = "python1"

# print(tuple1)



# my_tuple_with_list = (1, [2, 3], 4)
# my_tuple_with_list[1].append(5)
# print(my_tuple_with_list)




# tuple_packing = "python" , 2 , True
# print(tuple_packing)



#tuple unpacking

# x ,y, z = 10 ,20, 30 
# print(f" unpacked x = {x}, y = {y}, z = {z}")


#Unpacking with * (star operator) for arbitrary remaining elements (Python 3+)


# my_list = (1,2,3,4,5,6)

# x ,y, *rest , z = my_list

# print(x , y , rest , z)



#list convet to tuple
# my_list = [1,2,3,4]

# my_tuple = tuple(my_list)

# print(my_tuple)



#tuple convert to list

# my_tuple = (1,2,3,4,5)

# my_list = list(my_tuple)

# print(my_list)


my_tuple = (1 , 2 , 3 , 2 , 4 , 2)

print(my_tuple.count(2))