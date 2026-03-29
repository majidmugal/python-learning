# a = open("test.py")

# file_data = a.readable().  # readable() give true false
# print(file_data)


# a = open("test.py")

# file_data = a.read().  #this is read all data 

# print(file_data)




# a = open("test.py")

# file_data = a.readline(). #this is read only single line
# print(file_data)




# a = open("test.py")

# file_data = a.readlines()  #this is read all lines in list format 
# print(file_data)


# a = open("test.py")

# for x in a.readlines():
#     if "hello" in x:
#         print(x)




# with open("test.py") as e:
#     print(e.readable())
    
#  e.read()



# a = open("test.py" , "w")

# new_file = a.write("hello majid")

# print(new_file)


# data = [ "line1\n", "line3\n", "line4\n",]

# a = open("test.py", "w")

# a.writelines(data)


# a.close()




# data = [ "hello\n", "majid\n","mugal\n"]

# a = open("test.py", "a")

# a.writelines(data)



# a = open("/Users/apple/Desktop/videoa_files/WhatsApp Video 2024-08-03 at 7.08.20 PM.mp4", "rb")

# print(a.readline())

# a.close()

# with open("test.py" "r") as a:
#      data = a.read()

# count_lines = 0
# count_spaces = 0

# for x in data :
#     if x == "\n":
#         count_lines += 1
    
#     if x == " ":
#         count_spaces += 1

# print(count_spaces , count_lines)



# with open("test.py" "r") as a:

#     file = a.read()
#     print(file)





# with open("test.py", "r") as f:
#     print(f.readline())
#     print(f.readline())


# with open("test.py", "w") as f:

#    f.write("i love python")

    


# with open("test.py", "a") as f:

#     f.write("\nhello majid")





# with open("test.py", "r") as f:

#     lines = f.readlines()              #count lines in file

#     print(len(lines))





# with open("test.py", "r") as f:

#     data = f.read()

#     if "Python" in data:
#         print("word found")




# with open("test.py", "r") as f:

#     total = 0
#     for line in f:
#         total += int(line)
#     print(total)


# with open("test.py" , "r") as f:

#    data = f.readlines()
#    print(len(data))                   # count  names lines and convert to uppercase

#    for name in data:
#       print(name.upper())
    

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as f:
        f.write(username + "," + password + "\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as f:
        users = f.readlines()

    for user in users:
        u, p = user.strip().split(",")

        if u == username and p == password:
            print("Login successful ✅")
            return

    print("Invalid username or password ❌")


# main menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")


    

















# new lines  ke bare m smjhana hai



