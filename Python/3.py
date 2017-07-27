# -*- coding: UTF-8 -*-
# 乘法运算

a = input("Input one number: ")
b = int(input ("how many times do you want to count: "))
count = 0

n = b
if n == 1:
    count = a
else :
    for n in range (1, b+1):
        count += a
print "The result is : ", str(a), " * ",str(b)," = ",str(count)
