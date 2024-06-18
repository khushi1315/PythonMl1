# # 1.WAP that takes 2 nos as input and prints their sum.
# a= int(input("Enter first number"))
# b= int(input("Enter second number"))
# c = a+ b
# print("the sum of two numbers is : ", c)

# #2.WAP that checks whether a given number is odd or even.
# c = int(input("Enter a number"))
# if(c %2==0):
#     print("the number is even")
# else:
#     print("the number is odd")

# 3.WAP that calculates factorial of given number.
# d = int(input("Enter a number"))
# def fac(d):
#     if(d<=1):
#         return 1
#     else:
#         fac=1
#         for i in range(1, a+1):
#             fac *=i
#         return fac
# print(fac(d))

#4.WAP that asks the user for their name and then prints a greeting message.
# name = input("enter your name:")
# def Greet(name):
#     return "Good morning", name
# print(Greet(name))

#5.WAP that takes string input and prints it to a text file.
# e = input("enter a string")
# filename = "First.txt"
# with open(filename, 'w') as file:
#     file.write(e)
# print(f"your input has been written to: {filename}")

# 6.Write a program that reads the content of a text file and prints it to the console
# with open("First.txt", 'r') as file:
#     content=file.read()
#     print(content)
#7.Write a python program that takes a string as input and returns its length. 

# String = input("Enter a string: ")
# str = len(String)
# print(f"the length of string is {str}")
#8.Write a python program that concatenates two strings and returns the result.
#  
# a= input("Enter first string: ")
# b= input("Enter second string: ")
# str1= a + b
# print(f"Concatenated string is : {str1}")

#9. Write a python program that checks if a substring is present in a given string.
# Str= input("Enter a string") 
# key=input("Enter a substring")
# def subString(str, key):
#     for i in Str:
#         if key in str:
#             return True
#         else:
#             return False
# print("Substring present:", subString(Str,key))

#10.Write a python program that converts a given string to uppercase.
# f= input("Enter a string") 
# newString= f.upper()
# print(f"This is string in uppercase: {newString}")

#11.Write a python program that generates the first n numbers in the Fibonacci sequence.
# Fib= int(input("Enter the number to find fibonacci sequence"))
# def fib(Num):
#     a, b= 0,1
#     for i in range(Num):
#         print(a, end=" ")
#         a, b = b, a+b


# print(fib(Fib))

#12.Write a python program that calculates the sum of the digits of a given number. 
# number= int(input("Enter a number: "))
# def SumOfDigits(number):
#     return sum(int(digit) for digit in str(number))
# print(SumOfDigits(number))

#13.Write a program that asks the user for their birth year and calculates their age
# year=int(input("Enter a number:"))
# def Calci(year):
#     Age= 2024-year
#     return Age
# print("The age of person is: ", Calci(year))

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.  
# lines=[]
# while True:
#     line = input("Enter a line(Or just hit enter to finish)")
#     if line=="":
#         break
#     lines.append(line)
# for line in lines:
#     print(line)

#15. Write a program that reads data from a CSV file and prints it to the console. 
# import csv
# file_name= input("Enter name of file:")
# with open(file_name, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#16.Write a program in python that counts the frequency of each character in a string. 
# string1=input("Enter a string: ") 
# frequency= {}
# for char in string1:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1
# print(frequency)

#17.Write a program in python that converts a given string to title case (first letter of each word capitalized).
# string=input("Enter a string: ")
# def TitleCase(string):
#     return string.title()
# print(TitleCase(string))

#18.Write a python program that checks if two strings are anagrams of each other. 
String1=input("Enter a string: ").lower()
String2=input("Enter another string: ").lower()

if sorted(String1)==sorted(String2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")