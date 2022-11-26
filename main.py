#Temporizador :) 
import time

#def menu():
#  print("\n--------------------Temporizador-------------------------")
#  print("\n1-Temporizador")
#  print("\n2-Pomodoro")
#  print("\n3-Cronometro")
#  print("\n4-Sair")
#  print("\n---------------------------------------------------------")


#def Cronometro():

#def Hora():

def Temp_Seg():
  tempo=input("\nDigite o tempo em segundos:")

  #verifica se trata de um digito ou nao, caso nao seja, recomeca denovo, caso seja pode converter para inteiro e dar prosseguimento
  if tempo.isdigit():
    tempo=int(tempo)
  else:
    print("\nEntrada nao valida, digite um numero inteiro por favor")
    Temp_Seg()
    
  #while tempo!=0 seria a mesma coisa que esse while tempo, porque quando ele for zero ele retorna false
  while tempo:
    #essa linha de baixo, em resumo, serve para utilizar o divmod que se trata de algo para realizar divisoes recorrentes salvando tanto o valor da divisao-> resultado, bem como do resto, nesse caso abaixo, o resto da divisao de tempo em minutos por 60, exemplo se for 70 vai ter "1" de resultado que vai ser atribuido a minutos, ja "segundos" vai receber os "10" de resto da divisao.
    minutos, segundos = divmod(tempo, 60)
    
    #formatado as variaveis para que elas sejam impressas na mesma linha, e com o formato certo, no caso no minimo 2 casas de digito, ou seja, mesmo que seja so 7 segs, por exemplo, que imprima 07, um minuto e três segundos seja: 01:03
    timer="{:02d}:{:02d}". format(minutos, segundos)
    print(timer, end="\r")
    #o end="\r" serve para que no final quando ele mudar, nao pule linha ou escreva abaixo como normalmente acontece, e sim, que reescreva sobre o que esta ali

    #sleepzinho de 1 segundo para o contador ir diminuindo de 1 em 1 segundo certinho
    time.sleep(1)
    tempo=tempo-1
  print("Tempo acabou!")
  print("\a")
  print("\a")

#def Pomodoro():
  #Tempo de estudo, quantidade de horas, tempo de descanso
  #tempo=input("Quantas horas pretende estudar(Digite um numero inteiro): ")
  


Temp_Seg()
#while True:
 # menu()
