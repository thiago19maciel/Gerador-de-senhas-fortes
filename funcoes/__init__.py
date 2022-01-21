from os import system
from random import randint
from time import sleep

def menu(*lista_de_opcoes):
    system("cls")
    while True:
        for pos,opc in enumerate(lista_de_opcoes):
            print(f"[{pos}] -> {opc}")
        try:
            opcao = int(input("\nDigite a opcao desejada: "))
            if 0 <= opcao <= len(lista_de_opcoes) - 1:
                break
            else:
                system("cls")
                print(f"Erro! Digite um numero entre 0 e {len(lista_de_opcoes)}.")    
        except:
            system("cls")
            print("Erro! Digite um numero inteiro")
    return opcao

def tela_de_carregamento(msg):    
    for carregar in range(0,2):
        frase = "Gerando senha."
        for ponto in range(0,3):
            system("cls")
            print(f"{frase}")
            sleep(1)
            frase += "."
    
def gerar_caractere(tipos_aceitos):
    tipo = randint(0,len(tipos_aceitos)-1)
    posicao = randint(0,len(tipos_aceitos[tipo])-1)
    caractere = tipos_aceitos[tipo][posicao]
    return caractere
    
def l():
    system('cls')