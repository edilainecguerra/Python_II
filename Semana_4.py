# Pilhas
# Estrutura para armazenar um conjunto de elementos;
# Novos elementos sempre entram no "topo" da pilha;
# O único elemento que se pode retirar da pilha de um dados momento é o elemento do topo

#Funções
#Push: empilha um elemento na pilha;
#Pop: desempilha o elemento no topo da pilha;
#Top: acessa o elemento do topo, sem desempilhá-lo
#Empty: verifica se a pilha está vazia

#Exemplo

class Pilha():
    def __init__(self): #função init é chamada automaticamente quando se cria um objeto da classe pilha
        self. data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return not len(self.data) > 0
    
p = Pilha()
p. push(4)
p. push(5)
p. push(6)

p.pop()
print (p.data)
p.pop()
print (p.data)

# Exercício
# Converter um número decimal para binário

p = Pilha()
num = 13
while num > 0:
    resto = num % 2
    num = num //2
    p.push(resto)
while not p.empty():
    print(p.pop())


##Filas
#estrutura para armazenar um conjunto de elementos
#novos elementos sempre entram no fim da fila
#o único elemento que pode ser retirado da fila, em um determinado momento, é seu primeiro elemento
#o primeiro elemento a entrar na fila será o primeiro elemento a sair

#Operações Usuais
#inserir() - fim da fila
#remover() - primeiro elemento da fila
#empty() - verifica se a fila está vazia
#top() - quem é o próximo elemento a ser removido, sem remover este elemento

#Exercício
class Fila():
    def __init__(self):
        self.data = []

    def inserir(self,x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
         if len(self.data) > 0:
             return self.data[0] 

    def empty(self):
        return not len(self.data) > 0

f = Fila()
f.inserir(1)
f.inserir(2)
f.inserir(3)
f.inserir(4)

f.remover()
print(f.remover())
f.remover()
print(f.remover())

# Exercício
#Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal.
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila, dependendo da idade de cada uma (acima de
# 60 anos entra na fila prioritária). A saída de pessoas da fila deve ocorrer da seguinte forma: a cada duas pessoas que
#saem da fila prioritária, uma sai da fila normal.

class Fila():
    def __init__(self):
        self.fila_prioritaria = []
        self.fila_normal = []
        self.contador_prioritaria = 0
    
    def inserir_pessoa(self, nome, idade):
        if idade >=60:
            self.fila_prioritaria.append(nome)
            print(f"{nome}(prioritário)foi adicionado à fila prioritária.")
        else:
            self.fila_normal.append(nome)
            print(f"{nome} foi adicionado à fila normal.")

    def atender(self):
        if self.fila_prioritaria:
            pessoa = self.fila_prioritaria.pop(0)
            print(f"Atendendo {pessoa} da fila prioritária.")
            self.contador_prioritaria +=1
        else:
            print("Nenhuma pessoa na fila prioritária para atender agora.")

        if self.contador_prioritaria ==2:
            if self.fila_normal:
                pessoa = self.fila_normal.pop(0)
                print(f"Atendendo {pessoa} da fila normal")
            else:
                print("Nenhuma pessoa na fila normal para atender agora.")
            self.contador_prioritaria = 0

    def exibir_filas(self):
        print("\nFila Prioritária:", self.fila_prioritaria)
        print("Fila Normal:",self.fila_normal)

fila = Fila()
fila.inserir_pessoa("Dona Maria", 72)
fila.inserir_pessoa("João", 45)
fila.inserir_pessoa("Seu José", 65)
fila.inserir_pessoa("Ana", 30)

fila.exibir_filas()

fila.atender()
fila.atender()
fila.atender()

fila.exibir_filas()




        
