#OPERACOES ARITMETICAS BASICAS
import math
import sympy
import numpy

a = 1 + 2 + 3
b = 3**10 - 1 + 8
c = 6 / 5 + 0.5**4

print(a);
print(b);
print(c);

d = (6-4j)**2

e = 2 + 4 + 5.6
f = 2 / 3 - 4
g = (3-4j)*(3+4j)
h = math.pi
i = math.sqrt(2)



x = sympy.symbols('y')
z = (1+x**2)**2
sympy.simplify(z)
y = 2.3 + 6.7**2
r = y**2 + 1 / 2**3

numpy.set_printoptions(legacy='1.25')
sympy.sin(sympy.pi/5)
numpy.sin(numpy.pi/5)
type(1.5 + 2.1j)

print(a);
print(b);
print(c);
print(d);
print(e);
print(f);
print(g);
print(h);
print(i);
print('r =', r, 'y = ', y, 'e', 'z =', z);
