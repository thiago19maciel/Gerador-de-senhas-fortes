# Imports
from funcoes import *


# Main
minusculas = "qwertyuiopasdfghjklzxcvbnm"
maiusculas = minusculas.upper()[::-1]
numeros = "1234567890"
simbolos = "!@#$%"
tipos = [numeros,minusculas,maiusculas,simbolos]
tipos_aceitos = []
senha = ""

print("\nBem vindo ao gerador de senhas\n")

opcao = menu('Numeros','Numeros + letras minusculas','Numeros + letras maiusculas e minusculas','Numeros + letras maiusculas e minusculas + simbolos')

repeticao = menu('Permitir repeticao','Sem repeticao')

for i in range(opcao+1):
    tipos_aceitos += tipos[i]

while True:
    tamanho_da_senha = int(input("Digite o tamanho da senha desejada: "))
    if repeticao == 0:
        total_caracteres_possiveis = tamanho_da_senha
    elif repeticao == 1:
        total_caracteres_possiveis = 0
        for t in tipos_aceitos:
            total_caracteres_possiveis += len(t)
        
    if 4 <= tamanho_da_senha <= total_caracteres_possiveis:
        break
    l()        
    print(f"Erro! O tamanho da senha deve estar entre 4 e {total_caracteres_possiveis} caracteres.") 
        
for i in range(0,tamanho_da_senha):
    while True:
        caractere = gerar_caractere(tipos_aceitos)
        if (repeticao == 1) and (not caractere in senha): # impedir repeticao
            senha += caractere
            break
        elif repeticao == 0:
            senha += caractere
            break


l()
print(f"A senha criada foi: {senha}\n")
system("pause")