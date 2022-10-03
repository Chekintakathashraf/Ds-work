import array.test as test

def monke(self):
    print('bye')

test.A.fun = monke

obj = test.A()

obj.fun()