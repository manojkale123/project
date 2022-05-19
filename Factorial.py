#Factorial of number
def fact(n):
    fact=1

    for i in range(1,n+1):
        fact=fact*i
    return fact
factorial=fact(5)
print(factorial)
