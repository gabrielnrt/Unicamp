from numpy import sqrt

a = 1
b = 2

def f(x,y):
    return y*(a + (x**2))
    
def g(x):
    return b/(a + (x)**2)
    
def F(y):
    return sqrt((b-a*y)/y)
    
def G(x):
    return x/(a + (x**2))

x = 2.1
y = 0.3

print("Item b")
for k in range(20):
    tempx = f(x,y)
    tempy = g(x)
    
    x = tempx
    y = tempy
    
    print("x = ",x)
    print("y = ",y)
    print()
    
print("**********************")
x = 2.1
y = 0.3
print("Item c")
for k in range(20):
    tempx = F(y)
    tempy = G(x)
    
    x = tempx
    y = tempy
    
    print("x = ",x)
    print("y = ",y)
    print()