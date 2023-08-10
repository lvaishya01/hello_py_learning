# import random
# import converters
# from utils import find_max
# import math
# print("Hello world")
# print("Lakshya")
# print('o----')
# print('  |||')
# print('*' * 10)
# # birth_year = input('Birth year: ')
# # print(birth_year)
# # # birth_year = '100'
# # print('you were born in ' + birth_year)
# # age = 2023 - int(birth_year)
# # print(age)
# # print('your age is ' + age)
# # 0.453592
# # weight = input('Weight : ')
# # in_kg = 0.453592*float(weight)
# # print(in_kg)
# course = 'Python for beginners'
# print(course[0])
# print(course[-1])
# print(course[4:8])
# another = course[:]
# print('another : ' + another)
# print('course : ' + course)
# print(len(course))
# print(course)
# # print(course.upper())
# course1 = course.upper()
# print(course1)
# course2 = course1.lower()
# print(course2)
# print(course.find('o'))
# course = course.replace('beginners', 'noobs')
# print(course) 
# print('beginners' in course)
# print('noobs' in course)
# a = 100/6
# b = 100//6
# print(a)
# print(b)
# print(a - float(b))
# print(a - b)

# print(10 ** 3)

# x = 10
# x+=3
# print(x)
# x-=3
# print(x)

# x = 2.9
# # x = x//1
# print(x)
# print(round(x))
# x = 2.3
# print(round(x))

# print(abs(-2.9))

# print(math.ceil(2.9))

# print(math.floor(2.9))

# is_hot = True
# is_cold = True
# if is_hot:
#     print("It's a hot day")
# elif is_cold:
#     print("It's a cold day")
# else:
#     print("It's a good day")
# print("yoyo")

# x = 15
# y = 20
# is_good = True
# if x<=15:
#     print(f"value is : {x}")
# else :
#     print(f"Value is: {y}")


# name = input("Your name ? : ")

# if(len(name) < 3):
#     print('Name must be atleast 3 char long')
# elif (len(name) > 50):
#     print('Name can be atmost 50 char long only')
# else:
#     print('Name looks good')

# i = 1
# while i<=5:
#     print('*' * i)
#     i+=1
# print("done!!")

# i = 0
# x = 0
# while(i < 3 and x != 9):
#     x = int(input(""))
#     i+=1

# guess_count = 0
# guess_limit = 3
# secret_number = 9
# while(guess_count < guess_limit):
#     guess = int(input(""))
#     if(guess == secret_number):
#         print("WIN :)")
#         break
#     guess_count+=1
# else :
#     print("LOSE :(")
# print("yo")

# s = input("")
# if(s == "help"):
#     print("start - to start the car")
#     print("stop - to stop the car")
#     print("quit - to exit")
#     t = input("")
#     if(t == "start"):
#         print(1)
#     elif(t == "stop"):
#         print(2)
#     elif(t == "exit"):
#         print(3)
#     else:
#         print("fuck off")
# else :
#     print("I don't understand that")

# s = ""
# t = ""
# while(True):
#     s = input("> ")
#     if(s.lower() == "quit"):
#         break
#     elif(s.lower() == "start"):
#         if(t.lower() != s.lower()):
#             print("car started")
#         else:
#             print("car already started")
#             t = s
#     elif(s.lower() == "stop"):
#         if(t.lower() != s.lower() and t!=""):
#             print("car stopped")
#         else:
#             print("car already stopped")
#             t = s
#     else:
#         print("typo:(")
# print("<<finish>>")

# for elem in "Python":
#     print(elem)

# for elem in ["Mosh","John","lkv"]:
#     print(elem)

# for elem in range(3,11,2):
#     print(elem)

# prices = [10,20,30,57]
# sum = 0
# for elem in prices:
#     sum+=elem
# print(f"total sum is {sum}")

# for x in range(4):
#     for y in range(3):
#         print(f"x,y = {x},{y}")


# for x in range(5):
#     if x==0 or x==2:
#         print('X'*5)
#     else:
#         print('X'*2)

# names = ["Mosh","John","lkv","hkv","jkv"]
# print(names)
# i = 0
# while i<len(names):
#     print(names[i])
#     i+=1

# print(names[:])
# print(names)
# print(names[-1:-4])

# num1 = [2,2,4,6,3,4,6,1]
# # num2 = num1
# num2 = []
# for num in num1:
#     if(not num in num2):
#         num2.append(num)
# print(num2)

# num = (1,2,3,4)

# hsh = {
#     '1' : "one",
#     '2' : "two",
#     '3' : "three",
#     '4' : "four",
#     '5' : "five",
#     '6' : "six",
#     '7' : "seven",
#     '8' : "eight",
#     '9' : "nine",
#     '0' : "ten",
# }

# s = input("Phone: ")
# t = ""
# for ch in s:
#     t+=hsh.get(ch, "!")
#     t+=' '
# print(t)

# def func(name):
#     print(f"yoyo {name}")


# print("start")
# func("hanulal")
# print("end")

# print(converters.kg_to_lbs(70))

# numbers = [1,2,3,4,6,7,9,5,8]
# print(find_max(numbers))

# for i in range(3):
#     print(random.random())
print("hello")