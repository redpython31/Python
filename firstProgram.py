
#comment
"""Multiline comment"""

"""
#Variable

name = None
age = 29
price = 35.99
a = None
isCool = False 
a = 5
b = 3
sum = a + b
power = a**b # b power of a a^b

#Print statement

print("My name is: ",name)
print("My age is: ",age)
print("Book price is: ",price)
print("None value: ",a)
print("you are cool: ",isCool)
print (sum)
print(power)


#type casting explicitly

name = input("Enter your name: ")
print("Welcome" ,name)

age = int(input("Enter your age: "))
print("Your age is: " ,age)

price = float(input("Enter price: "))
print("Price" ,price)
"""

#Question #1

#Write a program to input 2 numbers & print their sum.

# input1 = int(input("Enter first number: "))
# input2 = float(input("Enter Second number: "))

# result = print("Sum is: ",input1 + input2)

#Question #2

#Write a program to input side of a square & print its area.

# sqare = float(input("Enter a side of square: "))
# print("Square value is: ", sqare**2)

#Question #3

#Write a program to input 2 floating point numbers & print their average.

# ava = float(input("Enter first value: "))
# ave = float(input("Enter second value: "))

# print("Average is: ", (ava+ave)/2)

#Question #4

#write a program to input 2 int numbers, and print True if a is greater than or equal to b. if not print false.

# userone = int(input("Enter first value: "))
# usertwo = int(input("Enter second value: "))
# print(userone >= usertwo)

# Conditional Statement

# String Indexing and length

# str = "Coder Faisal"

# lenght = len(str)

# print(lenght)

# print(str[4]) #print character index 

# Slicing pos + or neg -

word = "hello world"

# print(word[2:7])
# print(word[:8]) #auto takes first index 0 
# print(word[2:len(word)]) #if we dont know last index
# print(word[1:]) #auto takes last index

# #Negative index

# print(word[-4:-1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# print(word[-7:-3])

#String function

# print(word.endswith("l"))

# print(word.replace("hello","bye"))

# print(word.capitalize())

# print(word.find("l")) #it will give you first occurence index

# print(word.count("l"))

#Question #5

#Writn a program to input user's first name & print its length.

# userInput = input("Enter your name. ")

# print("Your name has",len(userInput), "letters.")

#Question #6

#Write a program to find occurrence of '$' in a string


# testString = "Hi$ i$ am$ faisal$ from$ ludhiyana$" 

# print("First dollor sign at index of ",testString.find("$"))
# print("There is",testString.count("$"),"$")

#Conditional statement

# marks = int(input("Enter your total marks: "))

# if(marks >= 90):
#     print("Grade = A")
# elif(marks >= 80):
#     print("Grade = B")
# elif(marks >= 70):
#     print("Grade = C")
# else:
#     print("Grade = D")

#Question #6

#Write a program to check if a number entered by the user is odd or even

# input_num = int(input("Enter any number."))

# if(input_num == 0):
#     print("Number is zero.")
# elif (input_num % 2 == 0):
#     print("Number is even.")
# else:
#     print("Number is odd.")

#Question #7

#Write a program to check greatest number of three.

# firstNum = int(input("Enter first num: "))
# secNum = int(input("Enter second num: "))
# thirdNum = int(input("Enter third num: "))

# if(firstNum > secNum and firstNum > thirdNum):
#     print(firstNum,"is largest number.")
# elif(secNum > firstNum and secNum > thirdNum):
#     print(secNum,"is largest number.")
# else:
#     print(thirdNum,"is largest number.")

#Write a program to check a number is multiple of 7 or not.

# check_Num = int(input("Enter number: "))

# if (check_Num % 7 == 0):
#     print(check_Num,"is multiple of 7.")
# else:
#     print(check_Num,"is not multiple of 7.")

#list in pyhton

# multiValue = ["Faisal", 29, "coder"]

# print(multiValue)
# print(multiValue[0])
# print(multiValue[1])
# print(multiValue[2])

# #string -> immortable , list -> mortable

# multiValue[0] = "kasif"

# print(multiValue)

# List Slicing

# listSlicing = [87,64,33,95,76]

# print(listSlicing[1:4])
# print(listSlicing[:4])
# print(listSlicing[1:])
# print(listSlicing[-3:-1])

#List Method
 
# lists = [2,1,3]

# lists.append(4)
# print(lists)

# lists.sort()
# print(lists)

# lists.sort(reverse = True)
# print(lists)

# lists.reverse()
# print(lists)

# lists.insert(0,5)
# print(lists)

# lists.remove(4)
# print(lists)

# lists.pop(0)
# print(lists)

#Tuples in Python

# tup = (87, 64, 33, 95, 76)
# print(type(tup))

# print(tup[3])

# tup_1 =() #empty tuple
# print(tup_1)

# tup_2 = (1,) #this is right way to single digit tuple
# print(tup_2)

# tup_3 = (2, 3,) # no worry to put last comma.
# print(tup_3)

# print(tup[1:3])

# print(tup.index(95))

# print(tup.count(33))

#Question #8

#write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

# movies = []

# mov = input("Enter first movie: ")
# movies.append(mov)

# mov = input("Enter second movie: ")
# movies.append(mov)

# mov = input("Enter third movie: ")
# movies.append(mov)

# print(movies)

#Wrint a program to check if a list contains  a palindrome of elements. (hint: use copy() method)

# pal = [1,2 , 3, 9, 1]

# cpal = pal.copy()
# cpal.reverse()

# if (pal == cpal):
#     print(pal,"is palindrome.")
# else:
#     print(pal,"is not palindrome.")

#next 

# pali = [1, "abc", "abc", 1]

# cpali = pali.copy()
# cpali.reverse()

# if (pali == cpali):
#     print(pali,"is palindrome.")
# else:
#     print(pali,"is not palindrome.")

#Write a program to count the number of students with the "A" grade in the following tuple.

# testTup = ("C","D","A","A","B","B","A")

# print(testTup.count("A"))

#store the above values in a list & sort them from "A" to "D".

# testList = ["C","D","B","A"]

# testList.sort()

# print(testList)

#Dictionary in Python

# info = {
#     "name" : "Faisal",
#     "subjects" : ["Linux", "Python","Cyber-Security"],
#     "topics" : ("dict","set"),
#     "age" : 29,
#     "is_adult" : True,
#     12.99 : 99.99 # This is a ex of floating (key) and floating (value) [key:value] 
# }

# print(info["name"])
# print(info["subjects"])
# print(info["topics"])
# print(info[12.99])

# info["name"] = "Kasif" #change value in same key
# info["surname"] = "Mohammad" #add a new key:value 

# print(info)

# null_dict = {} #empty dictionary

# print(null_dict)

#Nested Dictionary

# student = {
#     "name" : "Faisal",
#     "class" : 12,
#     "score" : {
#         "chem" : 97,
#         "phy" : 98,
#         "maths" : 96 
#     }
# }

# print(student["score"]["chem"])
# print(student.keys())   #which type of key are there but not print nested keys
# print(list(student.keys())) #list of student dictionary
# print(len(student)) #length of student dictionary

# print(list(student.values()))
# print(student.items())
# print(list(student.items()))

# pairs = list(student.items())
# print(pairs[0])

#print(student["name2"])  #key mistype output error value
#print(student.get("name2"))#key mistype output None

# student.update({"city" : "Delhi"})
# print(student)

# new_dict = {"mob" : 9839587496}
# student.update(new_dict)
# print(student)

#Sets in Python

# sets = {1,2,3,4, "Hello", "World","World", 2,2,3}
# set ignore duplicate integers or string

# emptySet = set() #empty set syntax

# print(sets)
# print(type(sets))
# print(len(sets))


# sets.add(9)
# sets.add("Faisal") #This is string
# sets.add((1,3,6)) #This is tuple
# #set.add([1,3,5]) #we cannot add any list 

# print(sets)

# sets.remove(9)
# sets.remove("World")
# print(sets)

# sets.clear()
# print(len(sets))

# popFun = {"hello", "faisal", "How", "are", "You"}

# print(popFun.pop())
# print(popFun.pop()) 
# print(popFun.pop())

# otherSet = {1, 2, 4 , 5 , 8 , "Hello", "Faisal", "World"}

# print(sets.union(otherSet))
# print(sets.intersection(otherSet))

#Question #9

#Store following word meanings in a python dictionary: 

#table: "a piece of funrnityre", "list of facts & figures"
#cat: "a small animal"

# object = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
#     }

# print(object)

#you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students. 

#python, java, C++, python, javascript, java, python, java, C++, C

# language = {"python", "java", "C++", "python", "javascript", "java", "python","java", "C++", "C"}

# print(len(language))

#Question #10

#Write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one. Use subject name as key & nakes as value.

# stdMarks = {}

# sub = (input("Enter subject: "))
# marks = int(input("Enter marks: "))
# stdMarks.update({sub : marks})

# sub = (input("Enter subject: "))
# marks = int(input("Enter marks: "))
# stdMarks.update({sub : marks})

# sub = (input("Enter subject: "))
# marks = int(input("Enter marks: "))
# stdMarks.update({sub : marks})

# print(stdMarks)

#Figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data types)

numSet = {9, "9.0"} #Possible solution

numSet1 = {("float", 9.0),("int", 9)}

print(numSet)
print(numSet1)
