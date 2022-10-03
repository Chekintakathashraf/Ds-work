def upper_dec(func):
    def inner():
        ans = func()
        return ans.upper()
    return inner
@upper_dec
def print_str():
    return 'good morning'

print(print_str())

def div_dec(func):
    def inner(x,y):
        if y==0:
            return 'invalid input'
        else:
            return x/y
    return inner
@div_dec
def print_div(a,b):
    return a/b

# print(print_div(10,0))












