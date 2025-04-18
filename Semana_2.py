# Organização de Estudos Semanais
# Semana 2: POO
# Exercícios

# Problema Prático 8.1
# Acrescente o método getx() à classe Ponto; esse método não aceita entrada e retorna a coordenada x do objeto Ponto que chama o método.
# >>> a.getx()
# 3
# Resposta:  
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
      
a = Ponto (3,4)
print(a.getx())
print(a.gety())

# Problema Prático 8.2

# Comece definindo a classe Teste e depois criando duas instâncias de Teste no seu shell do interpretador:
#>>> class Teste:
#     versão = 1.02
# >>> a = Teste()
# >>> b = Teste()

# A classe Teste tem apenas um atributo, a variável de classe versão, que se refere ao valor float 1.02.

# (a)Desenhe os namespaces associados à classe e aos dois objetos, os nomes – se houver – neles contidos e os valores aos quais os nomes se referem.
# (b)Execute essas instruções e preencha os pontos de interrogação:

class Teste:
    versão = 1.02
a = Teste()
b = Teste()

a.versão
b.versão
Teste.versão

a.versão = 2.0
a.versão
b.versão
Teste.versão

Teste.versão = 3.0
a.versão
b.versão
Teste.versão

print(a.versão)
print(b.versão)
print(Teste.versão)

# Para melhor compreender o Código: trata-se da herança de atributis em Python

class Carro:
    rodas = 4

meu_carro = Carro()
carro_vizinho = Carro()

print(meu_carro.rodas)
print(carro_vizinho.rodas)


# Atividade Teste: 

class Cachorro: 
    def __init__(self, idade): 
        self.idade = idade 

class Dalmata(Cachorro): 
    def __init__(self, idade, pedigree): 
        super(Dalmata, self).__init__(idade) 
        self.pedigree = pedigree 

d = Dalmata(3, True) 
print(d.idade, d.pedigree) 

# Atividade Teste

class Ponto: 
    x = -1 
    y = -1 
 
p = Ponto() 
p.x = 2 
p.y = 3 

Ponto.x = 1 
Ponto.y = 4 
print(Ponto.x) 

print(p.x) 
print(p.y) 

print(Ponto.y)
