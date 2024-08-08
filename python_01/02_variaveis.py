# Variáveis
nome = "Gisele"
idade = 44

#Exibição de valores
print(nome)
print(idade)
print("anos.\n")

# 1° método de concatenação (string: str)
print("o meu nome é: " + nome + " e tenho " + str(idade) + " anos.\n")

# 2° método de concatenação (format)
print("o meu nome é: {} e tenho {}  anos.\n".format(nome,idade))

#3° método de concatenação (f string)
print(f"o meu nome é: {nome} e tenho {idade} anos.\n" )