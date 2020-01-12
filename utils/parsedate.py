from datetime import date, timedelta

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# parse Date
def parse_date(d):    # write Fibonacci series up to n
    splitted=d.split('-')
    d_=date(int(splitted[0]), int(splitted[1]), int(splitted[2]))   # date
    return d_