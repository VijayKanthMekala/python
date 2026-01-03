def fun(n, m):
    fib = [0, 1]  
    count = 0  # Track multiples of m
    
    while True:
        fib.append(fib[-1] + fib[-2])  # Generate next Fibonacci
        if fib[-1] % m == 0: 
            count += 1  
            if count == n: 
                return fib[-1]  

n, m = 4, 3  # 4th Fibonacci multiple of 3
print(fun(n,m))
