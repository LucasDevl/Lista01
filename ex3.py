# Imprime a pergunta na tela
print("Qual é o verdadeiro nome do Batman?")
print("a) Bruce Wayne")
print("b) Clark Kent")
print("c) Peter Parker")
print("d) Tony Stark")
print("e) Steve Rogers")

# reposta certa
reposta_certa = "a"

# Pede ao usuário que digite a resposta, para armazenar na variavel 'reposta'
resposta = input("Digite a letra correspondente à sua resposta: ")

# Mostra na tela a resposta certa, e a do usuario
print("Você respondeu alternativa", resposta + ".")
print("A resposta correta é a alternativa", reposta_certa + ".")