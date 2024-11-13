"""
The fibonacci sequence is as follows

f(n) = { 1            , n<=1
         f(n-1)+f(n-2), n>1

Given an integer k, we write a function to take in k and 
check if k is in the fibonacci sequence. If so, we return 
n such that f(n)=k, else return -1.
"""

def in_fib(k:int) -> int:
    if k < -1:
        return -1
    if k == 1:
        return 1

    f1 = 1 # f(n-1)
    f2 = 1 # f(n-2)
    f = f1 + f2
    n = 2 # since cases where n<1 taken care of

    # Increment f according to fib, sequence until we reach/pass k
    while f < k:
        f2 = f1
        f1 = f
        f = f1 + f2
        n += 1

    if k == f:
        return n
    else:
        return -1

def main():
    x = 7
    print(x, in_fib(x))

    x = 8
    print(x, in_fib(x))

    x = 20
    print(x, in_fib(x))

    x = 21
    print(x, in_fib(x))

if __name__ == "__main__":
    main()
