import time

import random

op_cnt = 0

def generateArray(l):
    return [random.randint(0,1000) for i in range(l)]

def search(array,number):
    global op_cnt
    counter = 0
    for n in array:
        op_cnt += 1
        if number == n:
            #return "Number "+str(n)+" found at position "+str(array.index(n))
            counter+=1
    return counter

array = generateArray(1000000)

start = time.time_ns()/ (10 ** 9)
res = search(array,random.randint(0,1000))
duration = time.time_ns()/ (10 ** 9) - start
print("Iterative:")
print("Result:",res)
print("Duration:",duration)
print("Operations:", op_cnt, "\n")