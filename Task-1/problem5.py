def fib(n):
    if n <= 0 :
        return 0
    elif n == 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter a +ve num: "))
for num in range(n):
    if num == n-1 :
        print(fib(num))
        break
    print(fib(num),end=",")