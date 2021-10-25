
def Fact(n):

    if n==0:
        return 1
    return n*Fact(n-1)

ans=Fact(4)
print("Factorial is :",ans)