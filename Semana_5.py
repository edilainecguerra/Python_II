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

# Insertion sort
# Ordenar o conjunnto inserindo os elementos em um subconjunto já ordenado
# Para fazer isso é necessário ordenar os elementos, se estiverem desordenados

# Exemplo
v = (25,57, 48, 37, 12, 92, 86, 33)
def insertion_sort(v):
    v = list(v)
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >=0 and x < v[j]:
         v[j+1] = v[j]
         j -= 1
        v[j+1] = x
    return v
print (insertion_sort(v))

# Merge sort ou ordenação por intercalação
# Estratégia de dividir para conquistar - resolve-se cada problema separadamente
# Tem-se uma lista que será dividida em duas partes e cada parte se divide em mais duas parte, depois se combina estes vetores
# Uso de vetor auxiliar para intercalar

# Exemplo
v = (25,57, 48, 37, 12, 92, 86, 33)
v = list(v)
def merge_sort(v,ini,fim):
    if ini< fim:
        meio = (ini + fim)//2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio,fim)
    return(v)
def intercala(v, ini, meio, fim):
    esquerda = v[ini:meio+1]
    direita = v[meio+1:fim+1]
    i = j = 0
    k = ini

    while i < len(esquerda) and j <len(direita):
        if esquerda[i] <= direita [j]:
            v[k] = esquerda[i]
            i +=1
        else:
            v[k] = direita[j]
            j+=1
        k +=1

    while i < len(esquerda):
        v[k] = esquerda[i]
        i +=1
        k +=1
    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1

merge_sort(v,0, len(v)-1)
print(v)