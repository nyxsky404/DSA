# Functional Recursion: here return will do the job

# Steps to follow:
    # create a flow
    # Create the base condition


## Sum of 1 to N

# Flow: f(10) = 10 + 9 + 8 + .... + 1 => 10 + f(9)
# Base case: f(1) = 1

N = int(input())

def SumOf1toN(N):
    if N == 1:
        return 1
    return N + SumOf1toN(N-1)

print(SumOf1toN(N))