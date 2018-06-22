import functools

def decorator(func):
    @functools.wraps(func)
    def inner(arg, n='Decor'):
        arg1=n
        n=arg**3
        return func(arg1, n)
    return inner

def Func(arg, n='Undecor'):
    print(n)
    return(arg)

print(Func(2))

print(decorator(Func)(2))