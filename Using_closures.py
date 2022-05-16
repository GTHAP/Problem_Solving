# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) 
# returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

def f(a, b):
    return a, b

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    first, _ = pair(f)
    return first

def cdr(pair):
    _ , second = pair(f)
    return second

car(cons(3,4))
cdr(cons(3,4))
