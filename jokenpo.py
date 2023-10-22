from os import system
from random import choice
###########################
system('color B')
system('cls')
###########################

#Lista de escolhas válidas
escolha = ['tesoura', 'papel', 'pedra']
vitorias_pc = 0
vitorias_user = 0

#Gerar Escolha PC
def maquina():
    decisao = choice(escolha)
    return decisao

#Define o Ganhador
def ganhador(pc_escolha, user_escolha):
    global vitorias_pc
    global vitorias_user
    indice_pc = escolha.index(pc_escolha)
    if escolha[indice_pc-1] != user_escolha and pc_escolha != user_escolha:
        vitorias_pc += 1
        return f'''•Você jogou {user_escolha}
•O computador jogou {pc_escolha}
•O computador ganhou!!
'''
    elif escolha[indice_pc-1] == user_escolha:
        vitorias_user += 1
        return f'''•Você jogou {user_escolha}
•O computador jogou {pc_escolha}
Você ganhou!!        
'''
    else:
        return f'''•Você jogou {user_escolha}
•O computador jogou {pc_escolha}
•Deu empate :O
'''

#Função para mostrar o placar
def placar(n):
    return f'''O placar atual é:
•{n} : {vitorias_user}
•Computador  : {vitorias_pc}
'''

#Main Loop
nickname = input('Digite seu nick: ')
system('cls')
while True:
    try:
        print('''.::JOKENPO INFINITY::.
   [0] Tesoura
   [1] Papel
   [2] Pedra''')
        user = int(input("Sua escolha: "))
        system('cls')
        print(ganhador(maquina(), escolha[user]))
        print(placar(nickname))
        continuar = input('Jogar novamente? (Digite N/NAO para encerrar a execução)')
        if continuar.lower() == 'n' or continuar.lower() == 'nao':
            break
        else:
            system('cls')
            continue
    except:
        system('cls')
        print('Input Inválido.')