# Módulo | Python: Variáveis & Tipos de Dados
# Exercícios

# Números

# Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de ticket médio abaixo:

# (A) 961.56
sqv_19 = 3
tkt_19 = 320.52
svv_19 = tkt_19 * sqv_19
print(svv_19)

svv_19 = 961.56
sqv_19 = 3
tkt_19 = svv_19 / sqv_19
print(tkt_19)


# (B) 7
svv_20 = 834.47
tkt_20 = 119.21
sqv_20 = svv_20 // tkt_20
print(sqv_20)

tkt_20 = svv_20 / sqv_20
print(tkt_20)



# (C) 3075.62
svv_21 = 15378.12
sqv_21 = 5
tkt_21 = svv_21 / sqv_21
print(tkt_21)


# Strings
# Aplique três métodos distintos na string abaixo.

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao.upper())


print(cancao.replace('Roda mundo', 'Mundo Roda'))

print(cancao.title())


# Extraia da string abaixo o valor da taxa selic na variável selic e o valor do ano na variavel ano. Imprima os valores na tela.

noticia = "Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos."
selic = noticia [12:17]
print(selic)

ano = noticia [62:70]
print(ano)

# Booleanos
# Utilize a tabela da verdade para responder: qual o valor da variável x?

a = False
b = True

x = not a & b
print(x)
True
