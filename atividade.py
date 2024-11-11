#Faça um programa que crie uma matriz aleatoriamente.O tamanho da matriz deve ser informado pelo usuário.

import random

# Função para criar e imprimir a matriz
def criar_matriz(linhas, colunas):
    # Criando a matriz com números aleatórios
    matriz = [[random.randint(1, 100) for _ in range(colunas)] for _ in range(linhas)]
    
    # Imprimindo a matriz
    print("\nMatriz gerada:")
    for linha in matriz:
        print(linha)
    return matriz
    # Entrada do usuário para o tamanho da matriz
try:
    linhas = int(input("Informe o número de linhas: "))
    colunas = int(input("Informe o número de colunas: "))

    if linhas <= 0 or colunas <= 0:
        print("O número de linhas e colunas deve ser maior que zero.")
    else:
        # Chamando a função para criar e imprimir a matriz
        criar_matriz(linhas, colunas)
except ValueError:
    print("Por favor, insira um número inteiro válido.")
