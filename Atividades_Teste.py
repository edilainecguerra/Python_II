v = [25, 33, 35, 12, 37, 86, 2, 57]

def quick_sort(v, ini, fim): 
    if ini < fim:
        meio = (ini + fim) // 2
        pivo = v[meio]
        i = ini
        j = fim

        while i <= j:
            while v[i] < pivo:
                i += 1
            while v[j] > pivo:
                j -= 1
            if i <= j:
                v[i], v[j] = v[j], v[i]
                i += 1
                j -= 1

        if ini < j:
            quick_sort(v, ini, j)
        if i < fim:
            quick_sort(v, i, fim)

quick_sort(v, 0, len(v) - 1)
print(v)

# Heap sort
# Heap: estrutura de dados - árvore binária
# para que uma árvore binária seja considerada um heap um nó deve satisfazer uma relação de ordem:
# Heap máximo: pai > = filhos
# Heap mínimo: pai < = filhos
# Forma: nós precisam estar agrupados à esqueda no último nível

# Algoritmos de busca
# Busca Linear: começa no início da lista e verifica se o elemento contido na lista é igual ao que se busca
l = [7,6,3,4]
3 in l

# para retornar a posição, chamo o comando index
l = [7,6,3,4]
l.index(3)

# Se a lista estiver ordenda, é possível realizar a busca binária
l = [7,6,3,4]
l.sort()
print(l)

#Busca Binária: ao invés de comparar inicialmente o elemento desejado com o primeiro elemento, comparamos com o elemento armazenado em um índice qualquer: 

#Exemplo
import random

l = random.sample(range(100), 20)

def busca_binaria(l,x, inicio,fim):
    meio = (inicio + fim)//2

    if x == l[meio]:
        return meio
    
    if x < l[meio]:
        return busca_binaria(l,x, inicio, meio - 1)
    
    if x > l[meio]:
        return busca_binaria(l, x, meio + 1 , fim)

busca_binaria(l, 92, 0, 19)
    

