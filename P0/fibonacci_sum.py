print("This program ads the fibonacci terms from 1 to n")

def fibonacci(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        print(n1, end = ', ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

num = int(input("Type a positive number: "))
fibonacci_series = fibonacci(num)

print("The resulting fibonacci series is: ", fibonacci_series)

sum = 0
for x in fibonacci_series:
    sum = sum + x

print("The total sum of all the terms of that fibonacci series is: ", sum) 