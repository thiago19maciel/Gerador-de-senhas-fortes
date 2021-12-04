from random import randint
from os import system
from time import sleep


minusculas = "qwertyuiopasdfghjklzxcvbnm"
maiusculas = minusculas.upper()[::-1]
numeros = "1234567890"
simbolos = "!@#$%"
tipos = [minusculas,maiusculas,numeros,simbolos]
senha = ""

system("cls")
print("\nBem vindo ao gerador de senhas\n")
tamanho_da_senha = int(input("Digite o tamanho da senha desejada: "))

for i in range(0,tamanho_da_senha):
    while True:
        tipo = randint(0,3)
        posicao = randint(0,len(tipos[tipo])-1)
        caractere = tipos[tipo][posicao]
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