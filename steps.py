"""
There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""

def staircase(n):
    if n==1 or n == 2:
        return n
    return staircase(n-2) + staircase(n-1)

result = staircase(5)
print(result)
