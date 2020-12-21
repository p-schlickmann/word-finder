cross_words = [
    ['A', 'V', 'E', 'T', 'O'],
    ['A', 'B', 'C', 'D', 'E'],
    ['C', 'B', 'C', 'D', 'E'],
    ['O', 'B', 'C', 'D', 'E'],
    ['R', 'B', 'C', 'D', 'E'],
    ['N', 'B', 'C', 'D', 'E'],
    ['O', 'B', 'C', 'D', 'E'],
    ['A', 'B', 'C', 'D', 'E'],
    ['A', 'B', 'C', 'D', 'E'],
    ['A', 'B', 'C', 'D', 'E'],
]

search = 'VETO'

for i in range(9):  # 9 linhas
    row = cross_words[i]  # pegar a linha
    row_string = ''.join(row)  # esse metodo junta toda a linha em uma string
    string_position = row_string.find(search)  # esse metodo pega a string row string e ve se dentro dela tem a string 'search',
                                                # se tiver retorna a posição dela, se não tiver retorna -1
    if string_position > -1:  # maior que -1 quer dizer que achou
        print(f"A busca '{search}' foi achada na posição cross_words[{i}][{string_position}]")

for j in range(5):  # 5 colunas
    column = []  # inicializar o array dessa coluna
    for i in range(9):
        column.append(cross_words[i][j])  # adicionar os valores ao array da coluna inicializado acima
    column_string = ''.join(column)  # juntar a coluna em uma unica string, por exemplo a coluna 0 vai ficar 'AACORNOAAA'
    string_position = column_string.find(search)  # buscar nessa string da coluna se o 'search' está dentro dela
    if string_position > -1:
        print(f"A busca '{search}' foi achada na posição cross_words[{string_position}][{j}]")


