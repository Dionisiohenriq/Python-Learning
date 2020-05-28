import re
from url import url_tratativa
# string = "Lorem ipsum dolor"
# print(string.find("dolor"))
# print(string[12:])
# print(string.index("dolor"))
# print('dolor' in string)
# index = url.find('?')
# print(url[index+1:])

url = 'www.bytebank.com/cambio?$=1500&moedaorigem=moedadestino&moedadestino=dolar'
url2 = 'www.bytebank.com/cambio?$=1500&moedaorigem=moedadestino&moedadestino=dolar'
#print(url_tratativa.verifica_url(url))
query = url_tratativa(url)
print(url == url2)
print(query.encontra_valores())
print(len(query))
print(url_tratativa(url))

# string regular expressions
padrao = "[0-9]{4,5}-?[0-9]{4}"
# Vamos testar esse padrão.
texto =  "Meu número para contato é 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())