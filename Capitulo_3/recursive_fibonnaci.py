from time import time_ns
import matplotlib.pyplot as plt

def rec_fib(n):
    if n < 2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

intervals = []
indices = range(2,30)

for i in  indices:
    start = time_ns()
    rec_fib(i)
    end = time_ns()
    intervals.append(end-start)

print(intervals)

plt.plot(indices,intervals)
plt.show()