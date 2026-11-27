# Q:1______________________________wap if a number is enter by user is odd or even_____________________

# num=int(input("number is:"))
# if(num % 2==0):
#     print("odd")
# else:
#     print("even")

# Q:2____________________________wap find the gratest of three number enter by user_____________________

# a=int(input("value of a:"))
# b=int(input("value of b:"))
# c=int(input("value of c:"))
# if(a>b and a>c):
#     print("a is gratest value")
# elif(b>c):
#     print("b is greatest value")
# else:
#     print("c is gratest value")


# Q:3_____________________________wap to chek a numer enter by user it is multiple of 7 or not____________

# a=int(input("enter number:"))
# if(a % 7 == 0):
#     print("a is multiple of 7")
# elif(a % 7 != 0):
#     print("a is not multiple of 7")

#_________________________________concept of list_________________________________________________________

# marks=[12,13,14,15,16,17,181,19]
# print(marks[3])

#__________________________________clicing in list________________________________________________________

# marks=[12,13,14,15,16,17,18,19]
# print(marks)
# print(marks[4])
# print(marks[1:4])
# print(marks[-6:-1])

# ___________________________________list methods_________________________________________________________

# 1:_________________________________add one element ayt the end_________________________________________

# list=[1,2,3,4,5]
# list.append(11)
# print(list)

#2:__________________________________sorts in accending order_________________________________________
# list=[1,4,7,2,9,3]
# list.sort()
# print(list)

#3:__________________________________sorts in deciding order__________________________________________

# list=[1,4,7,2,9,3]
# list.sort(reverse=True)
# print(list)

#4:___________________________________reverse list_____________________________________________________
# list=[1,4,7,2,9,3]
# list.reverse()
# print(list)

#5:___________________________________reverse element at index________________________________________
#  
# list=[1,4,7,2,9,3]
# list.insert(2,"crescent")
# print(list)

#6:___________________________________remove first occurance of element________________________________

# list=[1,4,7,2,9,3]
# list.remove(9)
# print(list)

#7:___________________________________remove element at index__________________________________________

# list=[1,4,7,2,9,3]
# list.pop(4)
# print(list)

#____________________________________simple program in list concept____________________________________

# fruits=["apple","banana","orange",]

# print("\nlist of fruits")
# print(fruits)

# #____________ adding items in list

# fruits.append("graps")
# print("\nupdate list")
# print(fruits)

# # ____________show only first index

# print("\nfirst index or first fruit")
# print(fruits[0])

# # _____________counting length of the all list
# print("\nnumber of fruits")
# print(len(fruits))

#______________________________________tuple concept__________________________________________________

# a=(1,2,3) 
# print(a)
# print(a[0:2])
# print(type(a))

# tuple methods

#1:__________________________________return index of first occurance___________________________________

# tup=(1,2,3,4)
# print(tup.index(4))

#2:___________________________________counts total occurrance___________________________________________

# tup=(1,4,2,3,4)
# print(tup.count(4))

#                               Q:1>>> wap to ask the user to enter names of their fav movies and store them in list

# m1=(input("movie one name:"))
# m2=(input("movie two name:"))
# m3=(input("movie three name:"))

# list=[m1,m2,m3]
# print(list)

#                                   :2>>>wap if a list contain a palindrome of element.......use of copy mathod

# list=[1,2,3,4,3,2,1]

# copy_list=list.copy()
# copy_list.reverse()

# if(copy_list==list):
#     print("palindrome")
# else:
#     print("not palindrome")

#                                        Q:3>>>wap to count the number of students with the "A" grade in the following tuple

# tup=("C","D","A","A","B","B","A")
# print(tup.count("A"))

#                                               Q:4>>>WAP to store the values in a list and sort them

# list=["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

#                                                   Dicitonary concepts

# dict={
#     "name":"muhammad Talha",
#      "cgpa": 12.3,
#      "marks":[12,14,81],
# }

# print(dict)
# print(dict["marks"])

#                                                   Dictionary Methods

# 1:>>>                                               return all keys

# student={
#     "name":"muhammad talha",
#     "subject":{
#         "physics":75,
#         "chem":95,
#         "bio":83,
#     }
# }

# print(student.keys())
# # other concept
# print(list(student.keys()))
# print(len(list(student.keys())))

# 2:>>>                                         return alla values

# student={
#     "name":"muhammad talha",
#     "subject":{
#         "physics":75,
#         "chem":95,
#         "bio":83,
#     }
# }

# print(student.values())

# 3:>>>>                        out put in pairs form or in tuple form


# student={
#     "name":"muhammad talha",
#     "subject":{
#         "physics":75,
#         "chem":95,
#         "bio":83,
#     }
# }

# pairs=(list(student.items()))
# print(pairs[0])


# 4:>>>>                            return key according to the value


# student={
#     "name":"muhammad talha",
#     "subject":{
#         "physics":75,
#         "chem":95,
#         "bio":83,
#     }
# }
# # error
#  print(student["name2"])
# # no error->thy give out (none)
# print(student.get("name2"))
