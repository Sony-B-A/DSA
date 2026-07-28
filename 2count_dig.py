# Noukri code 360
# Level:Easy
# Problem statement
'''
Ninja want to add coding to his skill set so he started learning it. On the first day,
he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.

Ninja called you for help as you are his only friend. Help him to solve the problem.
'''
from math import *
# method 1

def countDigit(n: int) -> int:
   # Write your code here.
   if n == 0:
      return 1
      
   num = abs(n)
   count = 0

   while num > 0:
      count += 1
      num = num // 10

   return count

# method 2

def countDigit(n: int) -> int:
   return int(log10(n) + 1)