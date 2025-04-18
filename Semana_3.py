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


