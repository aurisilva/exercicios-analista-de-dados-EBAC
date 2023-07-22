
# 1 Estrutura condicional for / in

# Na lista `propaganda_online` abaixo, estão presente os dados de usuários que acessaram um determinado site e se o mesmo clicou em uma propaganda.

propaganda_online = [
  {'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85, 'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99, 'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
  {'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada'},
  {'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32, 'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]

for dado_de_usuario in propaganda_online:
  print(dado_de_usuario)

# 1.1. Imprime os seguintes valores da lista:
# `tempo_gasto_site` e `idade`

# Dica: Utilize os conceitos de chave e valor de elementos de uma lista para selecionar os valores de uma chave (lista[chave]), conforme exemplo abaixo, na qual imprime somente os dados da chave `cidade`:

for dado_de_usuario in propaganda_online:
    print(dado_de_usuario['cidade'])

# Extrair os valores da chave tempo_gasto_site

for dado_de_usuario in propaganda_online:
    print(dado_de_usuario['tempo_gasto_site'])

# Extrair os valores da chave idade
for dado_de_usuario in propaganda_online:
    print(dado_de_usuario['idade'])

# 2 Estrutura condicional if / else

# 2.1. Utilize a estrutura if/else para imprimir a cidade dos usuários que gastaram mais de 100 horas de tempo na internet

# Dica: Após a iteração dos elementos da lista (Através da estrutura condicional FOR),  utilize a estrutura if/else para criar a condição dos valores da chave `tempo_gasto_internet`

for dado_de_usuario in propaganda_online:
        if dado_de_usuario['tempo_gasto_internet'] > 100:
            print(f"O usuário da cidade de {dado_de_usuario['cidade']} gastou mais de 100 horas na internet.")

# 3 Estrutura condicional try / except

# 3.1. Utilize a estrutura try/except para imprimir as cidades dos usuários que passaram mais de 70 segundos no site.

# Dica: Realize o tratamento de exceções dentro da execução da iteração dos elementos da lista

for dado_de_usuario in propaganda_online:
    try:
      tempo_site = dado_de_usuario['tempo_gasto_site']
      if tempo_site > 70:
        print(f"A cidade de {dado_de_usuario['cidade']} passou mais de 70 segundos no site.")
    except Exception as exc:
         print(f"Tempo gasto no site da cidade de {dado_de_usuario['cidade']} estava vazio.")
