# Parameterized Function: here "print" is doing job, while "return" is just for stopping the function

## print x for n times

x = int(input())
n = int(input())

def func(x,n):
    if n == 0:
        return
    print(x)
    func(x, n-1)

func(x,n)


## print 1 to N / i to N : Tail Recursion

i = int(input())
N = int(input())

def print1toN(i,N):
    if i > N:
        return
    print(i)
    print1toN(i+1,N)

print1toN(i,N)


## print 1 to N / i to N : Head Recursion

i = int(input())
N = int(input())

def head1toN(i,N):
    if i > N:
        return
    head1toN(i,N-1)
    print(N)

head1toN(i,N)



## print N to 1 / N to i: Tail Recursion

i = int(input())
N = int(input())

def printNto1(i,N):
    if i > N:
        return
    print(N)
    printNto1(i,N-1)

printNto1(i,N)

## print N to 1 / N to i : Head Recursion

i = int(input())
N = int(input())

def head1toN(i,N):
    if i > N:
        return
    head1toN(i+1,N)
    print(i)

head1toN(i,N)
