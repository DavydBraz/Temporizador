#Temporizador e outras funcoes relacionadas a tempo
import time

#menu
def Menu():
  print("\n---------------------------MENU--------------------------")
  print("\n1-Temporizador")
  print("\n2-Pomodoro")
  print("\n3-Sair")
  print("\n---------------------------------------------------------")

#funcao do temporizador
def Temporizador():
  print("\n===Temporizador selecionado===")
  try:
    tempo = int(input("\nDigite o tempo em segundos: "))


    #while tempo!=0 seria a mesma coisa que esse while tempo, porque quando ele for zero ele retorna false
    while tempo:
      #essa linha de baixo, em resumo, serve para utilizar o divmod que se trata de algo para realizar divisoes recorrentes salvando tanto o valor da divisao-> resultado, bem como do resto, nesse caso abaixo, o resto da divisao de tempo em minutos por 60, exemplo se for 70 vai ter "1" de resultado que vai ser atribuido a minutos, ja "segundos" vai receber os "10" de resto da divisao.
      minutos, segundos = divmod(tempo, 60)

      #formatado as variaveis para que elas sejam impressas na mesma linha, e com o formato certo, no caso no minimo 2 casas de digito, ou seja, mesmo que seja so 7 segs, por exemplo, que imprima 07, um minuto e três segundos seja: 01:03
      timer = "{:02d}:{:02d}".format(minutos, segundos)
      print(timer, end="\r")
      #o end="\r" serve para que no final quando ele mudar, nao pule linha ou escreva abaixo como normalmente acontece, e sim, que reescreva sobre o que esta ali

      #sleepzinho de 1 segundo para o contador ir diminuindo de 1 em 1 segundo certinho
      time.sleep(1)
      tempo = tempo - 1
    print("Tempo acabou!")
  
    #Barulhinho de beep
    print("\a")
    print("\a")

    #questionando para executar novamente o temporizador ou nao, formato string base, com opcao sendo ou a sigla ou a palavra da escolha, para caso alguem digite a palavra nao se atendo a esse detalhe da sigla, por padrao caso digite algo fora das especificacoes retorne ao menu
    escolha = str(input("\nDeseja usar novamente o temporizador? (s/n): "))
    if escolha == "s" or escolha == "sim":
      Temporizador()
    elif escolha == "n" or escolha == "nao":
      print("\nTemporizador finalisado")
    else:
      print(
      "\nDigitou algo fora das escolhas, devido a isso ocorreu um erro, ira retornar para o menu inicial"
      )
  except:
    print("\nOcorreu um erro, provavelmente digitou algo fora dos parametros, o programa ira retornar a tela do menu inicial")

#funcao do Pomodoro
def Pomodoro():
  print("\n===Pomodoro selecionado===")
  try:
    tempo = int(input("\nTempo do Pomodoro: "))
    tempo *= 60
    while tempo:
      minutos, segundos = divmod(tempo, 60)
      timer = "{:02d}:{:02d}".format(minutos, segundos)
      print(timer, end="\r")
      time.sleep(1)
      tempo = tempo - 1
    print("Tempo do Pomodoro teminado\n")
    print("\a")
    print("\a")
    opcao = str(input("Quer utilizar o pomodoro novamente (s/n): "))
    if opcao == "s" or opcao == "sim":
      Pomodoro()
    elif opcao == "n" or opcao == "nao":
      print("\nPomodoro finalisado\n")
    else:
      print(
        "\nDigitou algo fora das opcoes, devido ao erro retornara para o menu inicial"
      )
  except:
    print("\nOcorreu um erro, provavelmente digitou algo fora dos parametros, o programa ira retornar a tela do menu inicial")

#laco infinito com while, para executar infinitamente as funcoes ate que a opcao sair seja selecionada
while True:
  Menu()
  opcao = str(input("\nQual opcao voce deseja:"))
  if opcao == "1":
    Temporizador()
  elif opcao == "2":
    Pomodoro()
  elif opcao == "3":
    print("\nPrograma finalizado, obrigado pela uso e preferencia :)")
    break
  else:
    print(
      "\nComando nao valido, tente algum que esteja presente nas opcoes disponiveis, exemplo: 2\n"
    )
