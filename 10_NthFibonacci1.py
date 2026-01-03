# Function for nth Fibonacci number
def Fibonacci(n):
    if n<= 0:                                 #       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))
print(Fibonacci(15))
print(Fibonacci(20))
                                              #       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.