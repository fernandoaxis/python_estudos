# ===============================
# VARIÁVEIS BOOLEANAS (True / False)
# ===============================

# Atribuindo valores booleanos
x = True
print('x =', x)

y = False
print('y =', y)

# Operador != (diferente)
# True é diferente de False → resultado será True
print('x != y →', x != y)

# Operador not (negação lógica)
# not False → True
z = not y

# Operador == (igualdade)
# x é True e z também é True → resultado será True
print('x == z →', x == z)


# ===============================
# STRINGS
# ===============================

# Exemplo de string literal
print('Esta é uma string')

# Atribuindo uma string a uma variável
mensagem = 'Universidade Federal '

# Exibindo o tipo da variável (str = string)
print('Tipo da variável mensagem:', type(mensagem))

# Exibindo o conteúdo da string
print(mensagem)


# ===============================
# CONCATENAÇÃO DE STRINGS
# ===============================

# O operador + junta (concatena) strings
UFLA = mensagem + 'de Lavras, MG.'
print(UFLA)


# ===============================
# MÉTODOS DE STRING
# (strings são IMUTÁVEIS)
# ===============================

# Esses métodos NÃO alteram a string original
print('Capitalizada:', UFLA.capitalize())
print('Minúscula:', UFLA.lower())
print('Maiúscula:', UFLA.upper())

# A string original permanece a mesma
print('String original:', UFLA)


# ===============================
# REPETIÇÃO DE STRINGS
# ===============================

# O operador * repete a string
print('Repetição da string:')
print(UFLA * 2)


# ===============================
# FORMATAÇÃO DE STRINGS
# ===============================

# {} são marcadores que serão substituídos pelos valores do format()
modelo_nome = 'Nome: {}, Sobrenome: {}'

# Substituição dos valores nos {}
print(modelo_nome.format('Gustavo', 'Furtado Ferreira'))


# ===============================
# ENTRADA DE DADOS (input)
# ===============================

# input() sempre retorna uma STRING
nome = input('Entre com seu primeiro nome: ')

# Concatenação de strings
print(nome + ' foi aprovado!')


# ===============================
# CONVERSÃO DE TIPOS (str → int)
# ===============================

# O valor digitado é recebido como string
# int() converte a string para inteiro
# Se o usuário digitar algo que não seja número, ocorrerá erro
x = int(input('Entre com um valor inteiro: '))

# Exibindo o valor e o tipo da variável
print('Valor digitado:', x)
print('Tipo da variável x:', type(x))
