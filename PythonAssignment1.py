#  1.WAP that takes 2 nos as input and prints their sum.
a= int(input("Enter first number"))
b= int(input("Enter second number"))
c = a+ b
print("the sum of two numbers is : ", c)

# 2.WAP that checks whether a given number is odd or even.
t = int(input("Enter a number"))
if(t %2==0):
    print("the number is even")
else:
    print("the number is odd")

# 3.WAP that calculates factorial of given number.
d = int(input("Enter a number"))
def fac(d):
    if(d<=1):
        return 1
    else:
        fac=1
        for i in range(1, a+1):
            fac *=i
        return fac
print(fac(d))

#4.WAP that asks the user for their name and then prints a greeting message.
name = input("enter your name:")
def Greet(name):
    return "Good morning", name
print(Greet(name))

#5.WAP that takes string input and prints it to a text file.
e = input("enter a string")
filename = "First.txt"
with open(filename, 'w') as file:
    file.write(e)
print(f"your input has been written to: {filename}")

# 6.Write a program that reads the content of a text file and prints it to the console
with open("First.txt", 'r') as file:
    content=file.read()
    print(content)
#7.Write a python program that takes a string as input and returns its length. 

String = input("Enter a string: ")
str = len(String)
print(f"the length of string is {str}")
#8.Write a python program that concatenates two strings and returns the result.
 
f= input("Enter first string: ")
g =input("Enter second string: ")
str1= f + g
print(f"Concatenated string is : {str1}")

#9. Write a python program that checks if a substring is present in a given string.
Str= input("Enter a string") 
key=input("Enter a substring")
def subString(str, key):
    for i in Str:
        if key in str:
            return True
        else:
            return False
print("Substring present:", subString(Str,key))

#10.Write a python program that converts a given string to uppercase.
m= input("Enter a string") 
newString= m.upper()
print(f"This is string in uppercase: {newString}")

#11.Write a python program that generates the first n numbers in the Fibonacci sequence.
Fib= int(input("Enter the number to find fibonacci sequence"))
def fib(Num):
    a, b= 0,1
    for i in range(Num):
        print(a, end=" ")
        a, b = b, a+b


print(fib(Fib))

#12.Write a python program that calculates the sum of the digits of a given number. 
number= input("Enter a number: ")
def SumOfDigits(number):
    list=[int(digit) for digit in number]
    count=0;
    for i in list:
        count+=i
    print(count)
SumOfDigits(number)

#13.Write a program that asks the user for their birth year and calculates their age
year=int(input("Enter a your birth year:"))
def Calci(year):
    Age= 2024-year
    return Age
print("The age of person is: ", Calci(year))

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.  
lines=[]
while True:
    line = input("Enter a line(Or just hit enter to finish)")
    if line=="":
        break
    lines.append(line)
for line in lines:
    print(line)

#15. Write a program that reads data from a CSV file and prints it to the console. 
import csv
file_name= input("Enter name of file:")
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#16.Write a program in python that counts the frequency of each character in a string. 
string1=input("Enter a string: ") 
frequency= {}
for char in string1:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(frequency)

#17.Write a program in python that converts a given string to title case (first letter of each word capitalized).
string=input("Enter a string: ")
def TitleCase(string):
    return string.title()
print(TitleCase(string))

#18.Write a python program that checks if two strings are anagrams of each other. 
String1=input("Enter a string: ").lower()
String2=input("Enter another string: ").lower()

if sorted(String1)==sorted(String2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#19.Write a python program that removes all punctuation from a given string.
S="Hey, this is @python! prog/ram!!!!!."
print("String before removing punctuation:",S)
punc="[@!./]"
for i in S:
    if i in punc:
        S=S.replace(i," " )

print("The final string is :", S)

#20. Write a python program that takes a list of numbers and returns their sum.
List=input("Enter list of numbers separated by space: ")
List=[int(num) for num in List]
count=0;
for i in List:
    count+=i
print(count)


# 21. Write a python program that counts the occurrences of a specific element in a list.
LIST=['a','v','b','c','d','a']
freq={}
for i in LIST:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
# 22. Write a python program that returns the minimum and maximum values in a list of numbers.
list=[1,2,43,2,1,0,43,23,354,231,234,4,3,2]
print("Max =" ,max(list),"Min=",min(list))


# 23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
choice=input("enter c if you want to convert temp from celcius to fahrenheit or enter f if you want vice versaa: ")
if choice=='c':
    c=int(input("enter temp in celcius: "))
    f=(9/5)*c+32
    print(f)
elif choice=='f':
    f=int(input("enter temp in fahrenheit: "))
    c=(5/9)*(f-32)
    print(c)
else:
    print("Wrong input")


# 24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
Op=input("Enter an operator: +,-,*,/")
if Op=='+':
    res=first+second
    print(res)
elif Op=='-':
    res=first-second
    print(res)
elif Op=='*':
    res= first*second
    print(res)
elif Op=='/':
    res= first/second
    print(res)
else:
    print("Wrong input")
# 25. Write a program that copies the contents of one text file to another.
# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
st="HEy khushi"
print("The string starts with given prefix: ", st.startswith("H"))
print("The string end with given suffix: ", st.endswith("i"))
# 27. Write a program in python that converts a string into a list of its characters
STRING="KHUSHI"
def Converts(string):
    string=list(string)
    return string
print(Converts(STRING))