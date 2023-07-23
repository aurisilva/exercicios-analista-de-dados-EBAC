# 0 Preparação do ambiente
# Neste exercício vamos trabalhar com os arquivos de csv e texto definidos abaixo. Execute cada uma das células de código para escrever os arquivos na sua máquina virtual.

# carros.csv: arquivo csv com informações sobre carros (venda, manutenção, portas, etc.).

# 1. Extração de coluna de arquivo csv
# 1.1. Extraia os valores `valor_venda` e armazena em uma lista.

valor_venda = []

with open(file='./carros.csv', mode='r', encoding='utf8') as arquivo:
    linha=arquivo.readline()# lê o cabeçalho
    linha=arquivo.readline()# lê a primeira linha
    while linha:
        linha_separada=linha.split(sep=',')# quebra a string nas virgulas e salva os resultados em uma lista
        valor_da_venda=linha_separada[1]# seleciona o segundo elemento da lista
        valor_venda.append(valor_da_venda)# salva o valor na lista de valor_venda
        linha=arquivo.readline()# lê uma nova linha, se a linha não existir, salva o valor None

print(valor_venda)

# 1.2 Complete a função abaixo para extrair uma coluna, do arquivo csv em uma lista.

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int) -> list:

  coluna = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
  # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
    while linha:
      linha_separada = linha.split(',')
      elemento = linha_separada[indice_coluna]
      elemento = elemento.replace('\n', '') # Método replace para remover o caractere especial '\n' de quebra de linha
      coluna.append(elemento)
      linha = arquivo.readline()

  return coluna

# Você pode testar a função com os códigos abaixo.

# extrair a coluna valor_manutencao
valor_manutencao = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=2)
print(valor_manutencao) # deve retornar ['med', 'vhigh', 'vhigh', ...]

# extrair a coluna porta_malas
porta_malas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=5)
print(porta_malas) # deve retornar ['small', 'small', 'small', ...]


# Exercício bônus

# 1 Funções para arquivo csv
# Complete a função abaixo para extrair uma coluna do arquivo csv em uma lista. Os elementos devem ter o tipo de dado correto.

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str) -> list:

  coluna = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
  # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
    while linha:
      linha_separada = linha.split(',')
      elemento = linha_separada[indice_coluna]
  # use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'
      if tipo_dado == 'str':
        coluna.append(str(elemento))
      elif (tipo_dado == 'int'):
        coluna.append(int(elemento))
      elif (tipo_dado == 'float'):
        coluna.append(float(elemento))
      elif (tipo_dado == 'bool'):
        coluna.append(bool(elemento))
      else:
        coluna.append(elemento)
      linha = arquivo.readline()

  return coluna

# Você pode testar a função com os códigos abaixo.

# extrair a coluna valor_venda
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
print(valor_venda) # deve retornar ['vhigh', 'med', 'low', ...]

# extrair a coluna pessoas
pessoas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=4, tipo_dado='int')
print(pessoas) # deve retornar [2, 2, 2, ...]

# 2 Funções para arquivo txt

# Complete a função abaixo para extrair uma as palavras de uma linha do arquivo txt em uma lista.

def extrai_linha_txt(nome_arquivo: str, numero_linha: int) -> list:

  palavras_linha = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
  # extraia a linha do arquivo utilizando o parametro 'numero_linha'
    for linha in range(numero_linha):
      linha = arquivo.readline()
  # quebre a linha em palavras com o comando split, note que o separador é um espaço ' '
    palavras_linha = linha.split()

  return palavras_linha

# Você pode testar a função com os códigos abaixo.

linha10 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=10)
print(linha10) # deve retornar ['Mas', 'eis', 'que', 'chega', 'a', 'roda', 'viva']