# -*- coding: utf-8 -*-
"""
OBS: Para testar na força bruta o chave.txt tem que estar "Chave: 0"
(Se a chave estiver 0 na hora de CRIPTOGRAFAR, o código printa "Chave inválida")

Aluno: Mateus Amaral do Nascimento(181101036)
"""

def menu():
    escolha = int(input("Deseja criptografar(1), descriptografar(2) ou sair(3): "))
    arquivo_chave = "chave.txt"
    arquivo_alfabeto = "alfabeto.txt"
    arquivo_texto = "texto.txt"
    arquivo_resultado = "resultado.txt"
    
    with open(arquivo_chave) as arquivo_chave_aberto:
        linhas_chave = arquivo_chave_aberto.readlines()
    
    with open(arquivo_alfabeto) as arquivo_alfabeto_aberto:
        linhas_alfabeto = arquivo_alfabeto_aberto.readlines()
        
    with open(arquivo_texto) as arquivo_texto_aberto:
        linhas_texto = arquivo_texto_aberto.readlines()
        
    for cont in range(len(linhas_texto)):
        linhas_texto[cont] = linhas_texto[cont].lower()
    
    limpar_resultado(arquivo_resultado)
    
    chave = int(str(linhas_chave)[linhas_chave[0].find(":")+4])
    alfabeto = (str(linhas_alfabeto).strip())[linhas_alfabeto[0].find(":")+4:linhas_alfabeto[0].find("'")-1]
    
    executar(escolha, linhas_texto, chave, alfabeto, arquivo_resultado)


def executar(escolha, linhas_texto, chave, alfabeto, arquivo_resultado):
    if escolha == 1 and chave == 0:
        print("Chave inválida!")
    elif escolha == 1:
        for cada_linha in linhas_texto:
            criptografar(cada_linha, chave, alfabeto, arquivo_resultado)      
    elif escolha == 2 and chave == 0:
        for cont in range(len(alfabeto)):
            chave = cont
            repeticao(linhas_texto, chave, alfabeto, arquivo_resultado)
            with open(arquivo_resultado, 'a') as arquivo_fim:
                arquivo_fim.write("\n")
    elif escolha == 2:
        repeticao(linhas_texto, chave, alfabeto, arquivo_resultado)
    elif escolha == 3:
        print("Fim do programa...")
    else:
        print("Comando errado!")


def limpar_resultado(arquivo_resultado):
    with open(arquivo_resultado, 'w') as arquivo_fim:
        arquivo_fim.write("")


def repeticao (linhas_texto, chave, alfabeto, arquivo_resultado):
    for cada_linha in linhas_texto:
        descriptografar(cada_linha, chave, alfabeto, arquivo_resultado)


def criptografar(texto, chave, alfabeto, arquivo_resultado):
    texto_final = ""
    texto = str(texto)    
    alfabeto += alfabeto[0:chave]
    
    for letra in texto:
        posicao = alfabeto.find(letra)
        if posicao != -1:
            texto_final += alfabeto[posicao+chave]
        else:
            texto_final += " "
        
    with open(arquivo_resultado, 'a') as arquivo_fim:
        arquivo_fim.write(texto_final + "\n")


def descriptografar(texto, chave, alfabeto, arquivo_resultado):
    texto_final = ""
    texto = str(texto)
    
    for letra in texto:
        posicao = alfabeto.find(letra)
        if posicao != -1:
            texto_final += alfabeto[posicao-chave]
        else:
            texto_final += " "
        
    with open(arquivo_resultado, 'a') as arquivo_fim:
        arquivo_fim.write(texto_final + "\n")
    
