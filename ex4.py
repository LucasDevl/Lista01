pergunta = 'Qual é o verdadeiro nome do batman?'
alternativaA = 'Bruce Wayne'
alternativaB = 'Peter Parker'
alternativaC = 'CBUM'
alternativaD = 'RAMON'
alternativaE = 'URS'

print(pergunta)
print('a) ', alternativaA)
print('b) ', alternativaB)
print('c) ', alternativaC)
print('d) ', alternativaD)
print('e) ', alternativaE)

respostaCerta = 'a'
resposta = ''

resposta = input('Digite sua resposta: ')
if resposta == respostaCerta:
    print('CORRETO')
else:
    print('ERRADO')
