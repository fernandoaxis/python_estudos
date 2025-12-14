# =========================================
# OPERAÇÕES ARITMÉTICAS BÁSICAS EM PYTHON
# =========================================

# Importação de bibliotecas matemáticas
import math      # Funções matemáticas básicas (pi, raiz quadrada, etc.)
import sympy     # Matemática simbólica (expressões algébricas)
import numpy     # Computação numérica e matemática científica


# =========================================
# OPERAÇÕES ARITMÉTICAS SIMPLES
# =========================================

# Soma de números inteiros
a = 1 + 2 + 3

# Potenciação (**), subtração e soma
b = 3**10 - 1 + 8

# Divisão (/) sempre gera número real (float)
# Potenciação com números reais
c = 6 / 5 + 0.5**4

print('a =', a)
print('b =', b)
print('c =', c)


# =========================================
# NÚMEROS COMPLEXOS
# =========================================

# Em Python, j representa a parte imaginária
# (6 - 4j)²
d = (6 - 4j)**2
print('d =', d)

# Produto de números complexos conjugados
g = (3 - 4j) * (3 + 4j)
print('g =', g)


# =========================================
# OPERAÇÕES COM NÚMEROS REAIS
# =========================================

e = 2 + 4 + 5.6          # Soma com número real
f = 2 / 3 - 4            # Divisão gera float

print('e =', e)
print('f =', f)


# =========================================
# FUNÇÕES MATEMÁTICAS (biblioteca math)
# =========================================

h = math.pi              # Valor de π
i = math.sqrt(2)         # Raiz quadrada de 2

print('pi =', h)
print('sqrt(2) =', i)


# =========================================
# MATEMÁTICA SIMBÓLICA (biblioteca sympy)
# =========================================

# Criação de uma variável simbólica
x = sympy.symbols('y')

# Expressão algébrica simbólica
z = (1 + x**2)**2

# Simplificação simbólica (não altera z automaticamente)
z_simplificado = sympy.simplify(z)

print('Expressão simbólica z =', z)
print('z simplificado =', z_simplificado)


# =========================================
# CÁLCULOS NUMÉRICOS
# =========================================

# Operações com números reais
y = 2.3 + 6.7**2

# Atenção à precedência de operadores:
# 2**3 é calculado antes da divisão
r = y**2 + 1 / 2**3

print('y =', y)
print('r =', r)


# =========================================
# FUNÇÕES TRIGONOMÉTRICAS
# =========================================

# Ajuste apenas para compatibilidade de impressão
numpy.set_printoptions(legacy='1.25')

# Seno simbólico
seno_sympy = sympy.sin(sympy.pi / 5)

# Seno numérico
seno_numpy = numpy.sin(numpy.pi / 5)

print('sen(pi/5) com sympy =', seno_sympy)
print('sen(pi/5) com numpy =', seno_numpy)


# =========================================
# TIPO DE DADO COMPLEXO
# =========================================

# Python reconhece automaticamente números complexos
tipo_complexo = type(1.5 + 2.1j)
print('Tipo de 1.5 + 2.1j:', tipo_complexo)


# =========================================
# RESUMO FINAL DOS RESULTADOS
# =========================================

print('\nResumo final:')
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print('e =', e)
print('f =', f)
print('g =', g)
print('h =', h)
print('i =', i)
print('y =', y)
print('r =', r)
print('z =', z)
