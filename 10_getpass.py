# importação de bliblioteca getpass
import getpass as gtp

usuario = input("Nome do usuário: ")
senha = gtp.getpass("Digite sua senha: ")

# verificaçãobdo númereo de caracteres da senha 
if len(senha) >=6:
    print(f"usuario cadastrado com sucesso!")
else:
    print(f"Atenção, a senha digitada esta incorreta!")