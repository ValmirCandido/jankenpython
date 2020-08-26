import random

while True:

    print("\n\nBem vindo ao JankenPython!\n\nEsse é um jogo de pedra, papel, tesoura.")
    x = int(input("\nEscolha uma das opções:\n\n1.Jogador x Jogador\n2.Jogador x Computador \n3.Sair\n\n"))

    if x == 1:
        print("\nJogador x Jogador\n")

        player1 = int(input("\nJogador 1, escolha sua jogada:\n\n1.Pedra\n2.Papel\n3.Tesoura\n\n"))
        player2 = int(input("\nJogador 2, escolha sua jogada:\n\n1.Pedra\n2.Papel\n3.Tesoura\n\n"))
        
        if player1 == 1:
            print("\n--Jogador 1 jogou pedra--\n")
        if player1 == 2:
            print("\n--Jogador 1 jogou papel--\n")
        if player1 == 3:
            print("\n--Jogador 1 jogou tesoura--\n")
        if player2 == 1:
            print("\n--Jogador 2 jogou pedra--\n")
        if player2 == 2:
            print("\n--Jogador 2 jogou papel--\n")
        if player2 == 3:
            print("\n--Jogador 2 jogou tesoura--\n")
        

        if player1 == player2:
            print("\n--Empate--\n")
        elif player1 == 1 and player2 == 2:
            print("\n--Vitória do jogador 2--\n")
        elif player1 == 1 and player2 == 3:
            print("\n--Vitória do jogador 1--\n")
        elif player1 == 2 and player2 == 1:
            print("\n--Vitória do jogador 1--\n")
        elif player1 == 2 and player2 == 3:
            print("\n--Vitória do jogador 2--\n")
        elif player1 == 3 and player2 == 1:
            print("\n--Vitória do jogador 2--\n")
        elif player1 == 3 and player2 == 2:
            print("\n--Vitória do jogador 1--\n")
        else:
            pass

    elif x == 2:
        print("\n--Jogador x Computador--\n")

        player1 = int(input("\nJogador, escolha sua jogada:\n\n1.Pedra\n2.Papel\n3.Tesoura\n\n"))
        comp = random.randint(1,3)

        if player1 == 1:
            print("\n--Jogador jogou pedra--\n")
        if player1 == 2:
            print("\n--Jogador jogou papel--\n")
        if player1 == 3:
            print("\n--Jogador jogou tesoura--\n")
        if comp == 1:
            print("\n--Computador jogou pedra--\n")
        if comp == 2:
            print("\n--Computador jogou papel--\n")
        if comp == 3:
            print("\n--Computador jogou tesoura--\n")
        

        if player1 == comp:
            print("\n--Empate--\n")
        elif player1 == 1 and comp == 2:
            print("\n--Vitória do Computador--\n")
        elif player1 == 1 and comp == 3:
            print("\n--Vitória do jogador--\n")
        elif player1 == 2 and comp == 1:
            print("\n--Vitória do jogador--\n")
        elif player1 == 2 and comp == 3:
            print("\n--Vitória do Computador--\n")
        elif player1 == 3 and comp == 1:
            print("\n--Vitória do Computador--\n")
        elif player1 == 3 and comp == 2:
            print("\n--Vitória do jogador--\n")
        else:
            pass

    elif x == 3:
        print("\n--Até a Proxima!!--\n")
        break
    else:
        print("\n--Opção invalida!!--\n")
        pass
