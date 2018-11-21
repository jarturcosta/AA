import time
import sys

sys.setrecursionlimit(100000)
value = 2
n_iter = 5000

def b(v,n):
    res = 1
    cnt = 0
    for i in range(n):
        cnt += 1
        res = res*v
    return res,cnt

op_cnt = 0
def b_r(v,n):
    global op_cnt
    counter+=1
    if n == 0:
        return 1
    return v*b_r(v,n-1)

start = time.time_ns()/ (10 ** 9)
res = b(value,n_iter)
duration = time.time_ns()/ (10 ** 9) - start
print("Iterative:")
print("Result:",res[0])
print("Duration:",duration)
print("Operations:",res[1],"\n")

start = time.time_ns()/ (10 ** 9)
res = b_r(value,n_iter)
duration = time.time_ns()/ (10 ** 9) - start
print("Recursive:")
print("Result:",res)
print("Duration:",duration)
print("Operations:", op_cnt)
