# import os

# files = os.listdir()


# print(files)

# for x in files:
#      os.path.isfile(x).  #this is help to pront only files in list
#      print(x)


# for x in files:
#     if os.path.isdir(x):  
#                             #this is help to print only folders in list
#         print(x)



# print(os.path.exists("/Users/apple/Documents/python")) // yh btata hai file hai ya nhi




# small proect of make terminal


# while True:
#     command = input("-->")
#     if command == "ls":
#         print(os.listdir())
#     if command == "lsfolder":
#         data = os.listdir()
#         for x in data:
#             if os.path.isdir(x):
#                 print(x)
#     elif command == "lsfiles":
#         data = os.listdir()
#         for x in data:
#             if os.path.isfile(x):
#                 print(x)
#     elif command == "stop":
#         break
#     else:
#         print("invalid command")    


# import sys
# # print(sys.argv)     # file mai data pass karna

# def buy_stocks():
#     print('buy stock'   )

# def sell_stocks():
#     print('sell stock')

# # buy_stock()
# # sell_stock()

# operation = sys.argv[1]

# if operation == "buy":
#     buy_stocks()

# elif operation == "sell":
#     sell_stocks()




from datetime import datetime  

print(datetime.now().date())