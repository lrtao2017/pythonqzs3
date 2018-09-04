#!/usr/bin/env python
__author__ = "lrtao2010"

'''
#输出1 2 3 4 5 6 8 9 10
n = 0
while n <= 10:
    if n == 7:
        n += 1
        #print("\n")
        pass
        #continue
        #break
    else:
        print(n)
    n += 1

#求1-100的所有数的和
N = 1
Num = 0
while N <= 100:
    Num = Num + N
    N += 1
print(Num)
'''
#求1-2+3-4+5-6......100的所有数的和
N = 1
Num = 0
while N <= 100:
    if N % 2 == 1:
        Num = Num + N
    else:
        Num = Num - N
    N += 1
print(Num)
