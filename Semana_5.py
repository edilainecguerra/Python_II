# Algoritmos clássicos de ordenação I
# Ordenção é organizar uma sequência de elementos, de mosdo que estabelçam alguma relação de ordem
# Ocasionalmente, dá menos trabalho buscar um elemento em um conjunto desordenado
# Porém, para várias chamadas, a ordenação pode ser mais eficiente 

# Terminologia
# Ordenação interna: todos os registros cabem na memória principal
# Ordenação externa: feita por blocos para armazenamento em discos
# Ordenação estável: chaves iguais em um conjunto são preservadas

# Bubble sort: percorre um conjunto várias vezes e, a cada iteração, compara cada elemento com seu sucessor e colocá-los em ordem

# Exemplo
x = (25,57, 48, 37, 12, 92, 86, 33)
def bublle_sort (x):
    x = list(x)
    n = len(x)
    for i in range(n):
        for j in range(0,n-i-1):
            if x[j]> x[j+1]:
                x[j], x[j+1] = x [j+1], x [j]
    return x

print (bublle_sort(x))


