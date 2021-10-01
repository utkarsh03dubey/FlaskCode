def factorial(x):
    fact=1
    for i in range(x):
        fact = fact * (x-i)

    return fact


print(factorial(5))