# Escreva uma função estadoNasc() que aceite como entrada o nome completo de
# um presidente dos Estados Unidos (como uma string) e retorne o estado em que ele nasceu. 
# Você deverá usar esse dicionário para armazenar o estado em que cada presidente recente nasceu:

def estadoNasc(nome):
    dicionario = {
    'Barack Hussein Obama':'Hawaii',
    'George Walker Bush':'Connecticut',
    'William Jefferson Clinton':'Arkansas',
    'George Herbert Walker Bush':'Massachussetts',
    'Ronald Wilson Reagan':'Illinois',
    'James Earl Carter, Jr':'Georgia'
    }
    return dicionario.get(nome,'Nome não encontrado')
print(estadoNasc('Barack Hussein Obama'))


