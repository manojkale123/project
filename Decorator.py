
def div(a,b):
    print(a/b)


def sum(fun):
    def inner(a,b):

        if a<b:
            a,b=b,a
            return fun(a,b)
    return inner

no=sum(div)
div(2,4)