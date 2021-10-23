# no recibe, no devuelve
# void, void
def suma():
    # codigo
    print(5+6)

# no recibe, devuelve
# void, return
def resta():
    op = 11 - 6
    return op
    # return 11 - 6

# recibe, no devuelve
# params, void
def mult(a, b):
    op = a * b
    print(op)
    # print(a*b)

# recibe, devuelve
# params, return
def div(a, b):
    return (a / b)

# params, return
def fib(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print("\tFUNCIONES")
    suma()
    result = resta()
    print(result)
    # print(resta())
    mult(2,10)
    result = div(10,3)
    print(result)
    print(fib(20))
