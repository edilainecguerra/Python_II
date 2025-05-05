v = (25,57, 48, 37, 12, 92, 86, 33)
v = list(v)

def merge_sort(v,ini,fim):
    if ini< fim:
        meio = (ini + fim)//2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio,fim)

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