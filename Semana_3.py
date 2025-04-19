#SEMANA 3
#FUNÇÕES RECURSIVAS - Parte 1
#Ferramenta para resolução dep problemas computacionais - Aplicar a recursão d emaneira indevida, pode afetar bastante o desempenho do programa 
# Recursão: uma função é recursiva, quando é definida nos seus prórpios termos diretamente ou indiretamente
def imprime (l):
    for i in range (len(l)):
        print(l[i])

#Transformando na Função Recursiva: 

def imprime_rec(l,i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l,i+1)
        
l = [1,2,3]
imprime_rec(l)


#Para melhor compreensão da linguagem: 
def imprime_recursivamente(lista, indice=0):
    if indice < len(lista):
        print(lista[indice])
        imprime_recursivamente(lista, indice + 1)

# Testando:
lista = [10, 20, 30]
imprime_recursivamente(lista)

# Quando usar recursão: se existir uma função simples e não recursiva da função, ela deve ser usada. 
# Usamos a recursão quando o problema pode ser definido recursivamente de forma natural. 
# Necessário definir: 
# 1 - Definir o problema de forma recursiva, ou seja, em termos dele mesmo
# 2 - Definir a condição de término (ou condição básica)
# 3 - A cada chamada recursiva, deve-se tentar garantir que se está mais próximo de satisfazer a condição de término

# Exemplo: Implementar a Função Recursiva para calcular o fatorial de um número inteiro positivo passado como parâmetro:

def fat(n):
    if n == 0:
        return 1
    else:
        res = n * fat (n-1)
        return res
print(fat(4))

# Exercício: Implementar uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci. 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
n = 6
n = 15
print(f'0{n}-ésimo termo de Fibonacci é: {fibonacci(n)}')

# Recursão II
#Funções Recursivas e Funções Iterativas
# As funções recursivas costumam apresentar maior lentidão

