def fibonacci(n):
    prev2, prev1 = 1, 0
    current = 0

    for i in range(0, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        print(prev1)
         


n = int(input())
fibonacci(n)