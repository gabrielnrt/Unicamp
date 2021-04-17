def f(x):
    y = x*(x-1)
    return y

def derivada(x,h):
    g = f(x+h) - f(x)
    g = g/h
    return g

delta = 1e-2
#ITEM A
print("Item 'a':")
R = derivada(1,delta)
print("A derivada de x(x-1) em x = 1 é ",R)

#ITEM B
print()
print("Item 'b':")
for i in [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]:
    D = derivada(1,i)
    print("Para delta =",i,", temos que a derivada é", D)
