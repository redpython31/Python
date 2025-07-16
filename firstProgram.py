
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

#word = "hello world"

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

#numSet = {9, "9.0"} #Possible solution

#numSet1 = {("float", 9.0),("int", 9)}

#print(numSet)
#print(numSet1)

#Loops in Python

#syntax

# i = 1
# while i <= 5:
#     print("Faisal coder")
#     i += 1

#Question #11

#print numbers from 1 to 100.

# while i <= 100:
#     print(i)
#     i += 1

#print number from 100 to 1

# j = 100

# while j >= 1:
#     print(j)
#     j -= 1

#print the multiplication table of a number n

# userInput = int(input("Enter number: "))

# while i <= 10:
#     print(userInput * i)
#     i += 1

#print the elements of the following  list using a loop

loopList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# loop_length = len(loopList)

# loop_i = 0

# while loop_i < loop_length:
#     print(loopList[loop_i])
#     loop_i += 1

#Search for a number X in this tuple using loop

loop_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# tuple_input = int(input("Enter number: "))

# idx = 0

# while idx < len(loop_tuple):
#     if(loop_tuple[idx] == tuple_input):
#         print(tuple_input,"is available at the index of",idx)
#         break
#     elif(idx+1 == len(loop_tuple)):
#         print("Not found!")
#     idx += 1

#Loops in Python

#Question #12

#Print the elements if the loopList list using a loop

# for num in loopList:
#     print(num)

# loop_Char = "Faisal coder"

# for charc in loop_Char:
#     print(charc)
# else:
#     print("End of line.")

#search for a number x in the loop_tuple using loop

# forInput = int(input("Enter a number: "))

# for_idx = 0

# for el in loop_tuple:
#     if (el == forInput):
#         print(forInput,"is found at the index of",for_idx)
#         break   #if don't want to check forward
#     for_idx += 1
    
#Range(start,stop,step)=> range(1,5,1)
#stop field is compulsory

# for rng in range(5):
#     print(rng)
# print("\n")

# for rng in range(1,5):
#     print(rng)
# print("\n")

# for rng in range(1,10,2): #here is in range(start,stop,step)
#     print(rng)

#Question #13

#print numbers from 1 to 100.
# for rng_test in range(1,101,1):
#     print(rng_test)
# print("\n")

# #print numbers from 100 to 1

# for rng_test in range(100,0,-1):
#     print(rng_test)
# print("\n")

#print the multiplication table of a number n.

# rng_input = int(input("Enter a number: "))

# for rng_test in range(1,11):
#     print(rng_test * rng_input)

#Pass statement

# for el in range(10):
#      pass
    #empty loop we can not leave.but there is a way we can leave a loop empty with (pass)
# if(el > 4):
#     pass

#Question #14

#Write a program to find the sum of first n numbers. (using while loop)

# ques1 = int(input("Enter a number: "))

# result = 0

# i = 0
# while (i <= ques1):
#     result += i
#     i += 1
# print(result)

#Write a program to find the factorial of first n numbers. (using for loop)

# result1 = 1

# for fact in range(1,ques1+1):
#     result1 *= fact
# print(result1)

 #Functions in Pyhton

# def cal(a, b):
#     calculate = a + b
#     return calculate

# reslt= cal(5,10)
# print(reslt)

# def prt():
#     print("hello")

# prt()

#average of 3 numbers.


# def avg_sum(a,b,c):
#     sum = a + b + c
#     avg_resutl = sum / 3
#     return avg_resutl

# call_avg = avg_sum(5,7,9)
# print(call_avg)

#Question #15

#Write a program to print length of alist. (list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "Mumbai"]

# def len_cities(city):
#     cityRslt = len(city)
#     return cityRslt



# city_len = len_cities(cities)
# print(city_len)

#write a program to print the elements of a list in a single line.(list is the parameter)

# def single_line(input):
#     for item in input:
#         print(item, end= " ")

# single_line(cities)

#Write a function to find the factorial of n.(n is the parameter)

# fun_fact = int(input("Enter a number: "))

# def factorial(num):
#     result = 1
#     for factor in range(1,fun_fact + 1):
#         result *= factor
#     print(result)

# factorial(fun_fact)


#write a function to convert USD to INR

# cal_curr = int(input("Enter a number: "))

# def converter (curr):
#     inrVal = curr * 83
#     print(inrVal)

# converter(cal_curr)

#Write a function to take a input number if number is odd then output is "ODD" or if even than output is "EVEN"

# checkNum = int(input("Enter a number: "))

# def funCheck(x):
#     if(x == 0):
#         print("Zero")
#     elif (x % 2 == 0):
#         print("EVEN")

#     else:
#         print("ODD")

# funCheck(checkNum)

# RECURSION

# def prt(y):

#     if(y == 0):
#         return
#     print(y,"hello faisal.")
#     prt(y-1)
#     print("end")

# prt(5) 

#Write a recursuve function to calculate the sum of first n natural numbers.

# n_natural = int(input("Enter number: "))

# def n_func(z):
#     if(z == 0):
#         return 0
#     return n_func(z -1 ) + z
    


# n_output = (n_func(n_natural))
# print(n_output)

#Write a recursive function to print all elements in a list . Hint: use list & index as paramenter

# rec_list = [55, 14, 25, 89, 75, 35, 69, 12, 4, 9]

# def rec_idx( w, u = 0):
#     if(u == len(w)):
#         return 
#     print(w[u])
#     rec_idx(w,u+1)


# rec_idx(rec_list)

#File Input/Output

# f = open("sample.txt", "w")

# f.write("I have opened a file sample.txt and writing in it something. This is sample line in this text file")

# f.close()

# f = open("sample.txt" , "r")

# data = f.read() #this is reading mode
# print(data)
# f.close()

# f = open("sample.txt", "a")
# f.write("\n now i am add some text in the existing file this is called appending")

# f.close()

#Here i can print one line or only some character of the file.

# f = open("sample.txt", "r")
# line1 = f.readline()

# print(line1)

# f.close()

# f = open("sample.txt", "r")
# characterWise = f.read(20)
# print(characterWise)

# f.close()

#Combine Mode

# f = open("combineMode.txt", "w+")


# combWrite = f.write("This is a example of combine mode for w+ means we can override any existing file and also read in one shot.")

# f.close

# f = open("combineMode.txt", "r+")

# readComb = f.write("This changed by using r+ mode.")

# print(f.read(readComb))

# f.close

# f = open("combineMode.txt", "a+")

# print(f.read())

# f.write("this will be change or write from the last in file.")

# f.close

#With syntax 

# with open("sample.txt" , "w") as f:
#     f.write("This is sample line in this text file now i am add some text in the existing file this is called appending.\n This is example of [with syntax] here we don't need to f.close function and i am appending some lines in this file.This is example of [with syntax] here we don't need to f.close function and i am overriding some lines in this file.")

# with open("sample.txt", "r") as f:
#     print(f.read())

#Deleting a file with os module

# f = open("test.txt", "w")

# f.write("this file makes purpose to check import os function that is using for deleting files.")

# f.close

# import os

# os.remove("test.txt")

#Question #16

#create anew file "Practice.txt" using python. add the following datain it:

# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# f = open("practice.txt", "w")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# f.close

#Write a function that replace all occurrences of "java" with "python" in above file.

# f = open("practice.txt", "r")

# data= f.read()

# newData = data.replace("Java","Pyhton")
# print(newData)

# f = open("practice.txt", "w")

# f.write(newData)

# f.close()

#Search if the word "learning" exists in the file or not.

# word =  input("Enter any word: ")

# with open("practice.txt", "r") as f:

#     data = f.read()

#     if(data.find(word) != -1 ):
#         print("Found")
#     else: 
#         print("Not Found")

#Write a function to find in which line of the file does the word "learning" occur first.
#Print -1 if word not found.

# def find_line(text):

#     line_no = 1
#     with open("practice.txt", "r") as f:
#         line = f.readline()
#         while line:
#             if(text in line):
#                 print(f"Found at line {line_no}")
#                 return 
#             line_no += 1
#             line = f.readline()
#         print("Word not found!")

# findInput = input("Enter word: ")

# find_line(findInput)

#From a file containing numbers separated by comma, print the count of even numbers.

# with open("commaSep.txt", "w") as f:
#     data = f.write("1,2,3,5,22,45,36,88,25,64,91,99")

# count = 0
# with open("commaSep.txt","r")as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)

#Object Oriented Programming (OOPs)

# class Student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")

#     def welcome(self):
#         print("welcome students.",self.name)

# s1 = Student("Faisal",99)
# s1.welcome()
# print(s1.name,s1.marks)

# s2 = Student("Kasif", 98)
# s2.welcome()
# print(s2.name,s2.marks)

#Question #17

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.

# class Datas:

#     def __init__(self,name ,marks):
#         self.name = name
#         self.marks = marks
       

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Hi{self.name}you avg score is: {sum/3:.2f}")

# s1 = Datas("Faisal",[98, 96, 93])

# s1.get_avg()

#Static Methods

# class CheckMethod :

#     @staticmethod  #Decorator
#     def greet():
#         print("Hello Faisal coder.")

# c1 = CheckMethod()

# c1.greet()

#Question #18

#Create Account class with 2 attributes- balance & account no.
#Create methods for debit, credit & printing the balance.

# class Account:

#     def __init__(self, accountNo, balance):
#         self.accountNo = accountNo
#         self.balance = balance
        
        
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Your account is debited by: {amount}")
#         print(f"Your balance is: {self.balance}")

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Your account is credited by: {amount}")
#         print(f"Your balance is: {self.balance}")

# accountNum = int(input("Enter account Number: "))        
# deposite = int(input("Enter amount: "))

# acc1 = Account(accountNum, deposite)

# acc1.debit(2000)
# acc1.credit(3000)

#OBJECT ORIENTED PROGRAMMING (OOPs) part 2

#used to delete object properties or object itself.

# class faisal:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# f1 = faisal("faisal",29)

# print(f1)
# print(f1.name,f1.age)

#delete properties or attributes

# del f1.name
# print(f1.name)

# print(f1)
# del f1
# print(f1)

#we can also private class attributes and methods (function)

# class Person:
#     __name = "faisal"   #this is class attribute

#     def __hello(self):
#         print("hello faisal")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome()) #This is calling internally class
# print(p1.__name())
# print(p1.__hello())

#INHERITENCE

# class Car:

#     color = "Black"

#     @staticmethod
#     def start():
#         print("Car Started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped..")

# class ToyotaCar(Car):

#     def __init__(self,name, brand):
#         self.name = name
#         self.brand = brand

# car1 = Car()
# print(car1) #Normally calling to Car class.

# car2 = ToyotaCar("fotuner","Toyota")
# print(car2)
# print(car2.name)

# print(car2.start(),car2.name,car2.stop())

# print(car1.color)


# class Fortuner(ToyotaCar):
#     def __init__(self, name , brand, type):
#         super().__init__(name, brand)
#         self.type = type

#we can access all the properties from class Car to Fortuner.

# car3 = Fortuner("SUV","fotuner","Toyota")

# print(car3)
# print(car3.color)
# car3.start()

# print(car3.brand, car3.name, car3.type)

# car3.stop()

#Multiple inheritance

# class A:
#     varA = "Faisal"
# class B:
#     varB = "Coder"
# class C(A, B):
#     varC = "Pro"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#Class Method

# class People:

#     name = "anonymous"   #we have to change this name


    # def chgName(self, name):    #we can one of them
        #self.name = name    #except this
        # People.name = name  #this trick
        # self.__class__.name = "faisal"  #this trick

    # @classmethod    #this is second trick
    # def chngName(cls, name):
    #     cls.name = name

# p1 = People()

# p1.chgName("kazi") # \
# print(p1.name)     #  \     we did from this trick but fail
#                    #  /
# print(People.name) # /

#=================================

#Now we can see the change in name with classmethod
# p2 = People()

# p2.chngName("arhan")
# print(p2.name)
# print(People.name)

#@Property

# class Subject:

#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
       # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
    #Then we create new method
#     @property
#     def percentage(self):
#         return f"{(self.phy + self.chem + self.math) / 3:.2f}%"

# std1 = Subject(88, 98, 99)

# print(std1.percentage)

#suppose a student have wrong marks in phy so.

# std1.phy = 95
# print(std1.phy)
# print(std1.percentage) #But actual percentage not changed

# print(std1.percentage) #now the percetage is changed

# POLYMOPHISM : OPERATOR OVERLODING

# print(1 + 2)
# print("Mohd" + "Faisal")
# print([1,2,3] + [4 ,5 ,6])

# class Complex:
#     def __init__(self,real, img):
#         self.real =real
#         self.img = img

#     def showNum(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal , newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal , newImg)

# com1 = Complex(1, 3)
# com1.showNum()

# num2 = Complex(4, 7)
# num2.showNum()

# num3 = com1 + num2
# num3.showNum()

# num3 = com1 - num2
# num3.showNum()

#Question #19

#Define a circle class to create a circle with radius r using the constuctor.



# class Circle:

#     def __init__(self, radius):
#         self.radius = radius
    
#Define an Area() method of the class which calculates the aea of the circle.

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#Define a perimete() method of the class which allows you to calculate the perimeter of the circle.

#     def perimeter(self):
#         return 2 * (22/7) *self.radius

# cir1 = Circle(21)

# print(cir1.area())
# print(cir1.perimeter())

#Define a Employee class with attributes role, department & salary. This class also has a showDetail() method.

# class Employee:

#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetail(self):
#         print(self.role, self.department, self.salary)
    
# #Create an engineer class that inherits properties from Employee & has additional attributes : name & age.

# class Engineer(Employee):

#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age
#         super().__init__("Engineer","IT","85,000")


# emp1 = Employee("Executive","Data-Analytic",95000)        
# emp1.showDetail()

# emp2 = Engineer("Faisal",29)
# emp2.showDetail()

#Create a class called order which stores item & its price.

# class Order:
#     def __init__(self, item , price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price
    

# odr1 = Order("chips", 50)
# odr2 = Order("Glue", 10)

# print(odr1.item, odr1.price)
# print(odr2.item, odr2.price)

# print(odr1 > odr2)

#Use Dunde function__gt__() to convey that:
#   order1 > order2 if price of order1 > price of order2

