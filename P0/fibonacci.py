print("This program calculates the nth term of the fibonacci series")

def fibonacci(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        print(n1, end = ", ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return 

num = int(input("Type a positive number: "))
fibonacci_series = fibonacci(num)

print("The resulting fibonacci series is: ", fibonacci_series)