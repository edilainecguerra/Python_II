# Conceitos Fundamentais da Web

# Web (WWWW): nome mais simples para definir world wide web. 
# A internet é a rede global de computadores, é uma infraestrutura.  
# URL (Uniform Resource Locator): scheme (protocolo) - host (enderço) - path (caminho dentro do servidor para encontrar o recurso)

# Scheme - define como acessar o recurso
# Host - nome do servidor que armazena o recurso/documento
# DNS - recebe o host e retorna o endereço IP correspondente
# Path - em uma URL especifica o caminho relativo do recurso a partir de um diretório predefinido
# HTTP - tipo de protocolo 

# Intercâmbio de dados - para fazer intercâmbio de dados, as padronizações são muito importantes
# HTML é uma linguagem que permite defibir cabeçalhos, listas, imagens, hiperlinks, etc em uma página web 
# Elemento âncora: serve para criar textos de hiperlink
# JSON - linguagem de intercambio de dados que define um formato padrão para descrever, em formato texto objetos como dicionários, lisas, números e strings. 

# urllib.request - requisitar e receber recursos web por meio de código 
# Função urlopen()

from urllib.request import urlopen
def getSource(url) :
    response = urlopen(url)
    html = response. read()
    return html.decode()

html = getSource('http://univesp.br')
print(html)

# html.parser processar elementos HTML em uma página web
# feed()
#para cada token lido executa um handle correspondente

from html.parser import HTMLParser
class MyParser(HTMLParser): 
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs: 
                if attr [0] == "href":
                    print(attr[1])










