print("Program for adding the numbers from 1 to the one you choose")

def sumN(n):
    sum = 0
    for x in range(n):
        sum = sum + x + 1

    return sum

num = int(input("Introduce a number: "))
total_sum = sumN(num)

print("The total sum is: ", total_sum)