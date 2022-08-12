# jogo pedra,papel e tesoura.
import random

opcoes =  ["pedra","papel", "tesoura"] 
vitorias= 0
perdas = 0
print("|| JOGO PEDRA, PAPEL , TESOURA || \n")
while True:
  jogador = input("Escolha [pedra],[papel] ou [tesoura] para continuar a jogar ou digite [n]: ").lower() 
  if jogador == "n":
    break
  if jogador not in opcoes:
    continue

  aleatorio = random.randint(0,2)

  escolha_comp = opcoes[aleatorio]
  print("Computador escolheu", escolha_comp + ".")

      #vitórias
  if escolha_comp == "pedra" and jogador == "papel" :
    print("Você ganhou! ")
    vitorias +=1
  elif escolha_comp == "papel" and jogador == "tesoura":
    print("Você ganhou! ")
    vitorias +=1
  elif escolha_comp == "tesoura" and jogador == "papel":
    print("Você ganhou! ")
    vitorias +=1

    # empates
  elif escolha_comp == "tesoura" and jogador == "tesoura":
    print("Empate! ")
  elif escolha_comp == "pedra" and jogador == "pedra":
    print("Empate! ")
  elif escolha_comp == "papel" and jogador == "papel":
    print("Empate! ")
  
  else:
    print("voce perdeu!")
    perdas+=1
print("Você ganhou", vitorias, "vezes.")
print("Você perdeu", perdas, "vezes." )
print("Adeus :)")
