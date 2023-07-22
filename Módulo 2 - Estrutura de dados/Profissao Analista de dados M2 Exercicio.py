# 1. Listas

# Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.

filmes = ['Um Sonho de Liberdade','O Poderoso Chefão','Batman: O Cavaleiro das Trevas','O Poderoso Chefão II','12 Homens e uma Sentença','A Lista de Schindler','O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction - Tempo de Violência',' O Senhor dos Anéis: A Sociedade do Anel','Três Homens em Conflito' ]
print(filmes)
print(len(filmes))

# Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.

print(filmes.insert(0,'O Poderoso Chefão'))
print(len(filmes))

print(filmes.pop(2))
print(filmes)

print(len(filmes))

# 2. Conjuntos

# Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
# Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado.

filmes = ['O Poderoso Chefão', 'Um Sonho de Liberdade', 'Batman: O Cavaleiro das Trevas', 'O Poderoso Chefão II', '12 Homens e uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', 'Pulp Fiction: Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', 'O Senhor dos Anéis: A Sociedade do Anel', 'Três Homens em Conflito', 'Três Homens em Conflito']

print(filmes)

filmes = {'O Poderoso Chefão', 'Um Sonho de Liberdade', 'Batman: O Cavaleiro das Trevas', 'O Poderoso Chefão II', '12 Homens e uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', 'Pulp Fiction: Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', 'O Senhor dos Anéis: A Sociedade do Anel', 'Três Homens em Conflito', 'Três Homens em Conflito'}
print(filmes)
print(type(filmes))

filmes = {'O Poderoso Chefão', 'Um Sonho de Liberdade', 'Batman: O Cavaleiro das Trevas', 'O Poderoso Chefão II', '12 Homens e uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', 'Pulp Fiction: Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', 'O Senhor dos Anéis: A Sociedade do Anel', 'Três Homens em Conflito', 'Três Homens em Conflito'}
print(list(filmes))
print(type(list(filmes)))


# 3. Dicionários

# Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>, 'sinopse': <sinopse do filme>}`.

filmes = {
    'nome': 'Um Sonho de Liberdade',
    'ano' : 1994,
    'sinopse' : 'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'
    }
print(filmes)