import urllib.parse

request = "titulo=Sorvete+de+banana&detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2"

params = {}

for chave_valor in request.split('&'):
    chave, valor = chave_valor.split('=')
    conteudo = urllib.parse.unquote_plus(valor, encoding= 'utf-8', errors = 'replace')
    params[chave] = conteudo

print(params)