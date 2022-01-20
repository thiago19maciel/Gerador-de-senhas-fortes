"""
perguntar tipo de senha
[0] -> Numeros
[1] -> Numeros + letras minusculas
[2] -> Numeros + letras maiusculas e minusculas
[3] -> Numeros + letras maiusculas e minusculas + simbolos
Digite a opcao desejada:

[0] -> Permitir repeticao
[1] -> Sem repeticao
Digite a opcao desejada

"""


from random import randint
from os import system
from time import sleep


def menu(*lista_de_opcoes):
    while True:
        for pos,opc in enumerate(lista_de_opcoes):
            print(f"[{pos}] -> {opc}")
        opcao = int(input("Digite a opcao desejada: "))
        if 0 <= opcao < 4:
            break
        system("cls")
        print("Erro!. Digite uma opcao valida.")
    return opcao

minusculas = "qwertyuiopasdfghjklzxcvbnm"
maiusculas = minusculas.upper()[::-1]
numeros = "1234567890"
simbolos = "!@#$%"
tipos = [numeros,minusculas,maiusculas,simbolos]
tipos_aceitos = []
senha = ""

system("cls")
print("\nBem vindo ao gerador de senhas\n")

opcao = menu('Numeros','Numeros + letras minusculas','Numeros + letras maiusculas e minusculas','Numeros + letras maiusculas e minusculas + simbolos')

for i in range(opcao+1):
    tipos_aceitos += tipos[i]

while True:
    tamanho_da_senha = int(input("Digite o tamanho da senha desejada: "))
    if 4 <= tamanho_da_senha <= 67:
        break
    system("cls")        
    print("Erro! O tamanho da senha deve estar entre 4 e 67 caracteres.")
    
        
for i in range(0,tamanho_da_senha):
    while True:
        tipo = randint(0,len(tipos_aceitos)-1)
        posicao = randint(0,len(tipos_aceitos[tipo])-1)
        caractere = tipos_aceitos[tipo][posicao]
        if not caractere in senha:
            senha += caractere
            break

for carregar in range(0,2):
    frase = "Gerando senha."
    for ponto in range(0,3):
        system("cls")
        print(f"{frase}")
        sleep(1)
        frase += "."

system("cls")
print(f"A senha criada foi: {senha}\n")
system("pause")