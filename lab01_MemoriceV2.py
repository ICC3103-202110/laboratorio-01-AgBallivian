import random as rng
import numpy as np
def playcards(c):
    l = []
    for i in range(1, c + 1):
        l.append(i) #lista con los pares
        l.append(i)
    rng.shuffle(l) #lista shuffeleada
    cardsplay = np.zeros((2, c)) #lista de juego con 0    
    #reemplazo de 0 por numeros, esta es la lista de juego
    for j in range(0, (c)):
        cardsplay[0][j] = l[0]
        l.pop(0)
        #print(cardsplay, "\n")
    for j in range(0, (c)):
        cardsplay[1][j] = l[0]
        l.pop(0)
        #print(cardsplay, "\n")
    #print(cardsplay)
    return(cardsplay)

def zerocards(c):
    tab_zeros = np.zeros((2, c))
    return(tab_zeros)
    
def play_cards(tab_game, tab_answer, c):
    #Tablero inicio de turno
    tab_back = tab_game
    play_turn = 0
    while play_turn != 2:
        #Seleccion 1
        if play_turn == 0:
            print("Primera Seleccion") 
            print("seleccione fila (0 o 1): ")
            row1 = int(input())
            print("seleccione columna (0 a ",c-1, "): ")
            col1 = int(input())
            #Coordenadas 1
            coord1 = (row1, col1)
            
            #Comprobar si ya esta seleccionado
            if tab_game[row1, col1] == 0:
                #Mostrar primera seleccion
                print("=========seleccion exitosa=========") #DEBUG\\
                tab_game[row1, col1] = tab_answer[row1, col1]
                print(tab_game)
                play_turn += 1
            else:
                print("Error, La carta ya fue elegida anteriormente")
                play_turn = 0
        #Seleccion 2    
        elif play_turn == 1:
            print("Segunda Seleccion") 
            print("seleccione fila ( 0 o 1 ): ")
            row2 = int(input())
            print("seleccione columna ( 0 a ",c-1, "): ")
            col2 = int(input())
            #Coordenadas 2
            coord2 = (row2, col2)
            
            #Repite Segunda eleccion en caso de seleccionar la misma
            if coord1 == coord2: 
                print("Error, seleccionaste la misma carta")
                play_turn = 1
            elif tab_game[row2, col2] != 0:
                print("Error, La carta ya fue elegida anteriormente")
                play_turn = 1
            else:
                #Comprobar Respuesta
                
                if tab_game[row1, col1] == tab_answer[row2, col2]:
                    print(tab_game[row1, col1], "=====sel 1=====\n", tab_answer[row2, col2], "=====sel 2=====\n")#DEBUG\\
                    #Mostrar segunda seleccion
                    tab_game[row2, col2] = tab_answer[row2, col2]
                    print(tab_game)
                    
                    print("\n+ + + P U N T O + + +\n")
                    
                    return(True, tab_game)
                elif tab_game[row1, col1] != tab_answer[row2, col2]:
                    print(tab_game[row1, col1], "=====sel 1=====\n", tab_answer[row2, col2], "=====sel 2=====\n")#DEBUG\\
                    #Mostrar segunda seleccion
                    tab_game[row2, col2] = tab_answer[row2, col2]
                    print(tab_game)
                    
                    print("\n- - - F A I L - - -\n")  
                    
                    #Reiniciar Tablero
                    tab_game = tab_back
                    
                    return(False, tab_back)
        

#c = int(input("Cartas a jugar: "))
c=2 #DEBUG\\

#Tablas
tab_answer = playcards(c)
tab_game = zerocards(c)
tab_back = tab_game

#puntaje
point_total = 0
point_max = c
point_p1 = 0
point_p2 = 0

#Turnos
player_actual = 1
player_result = 0

while point_total < point_max:
    point_total = point_p1 + point_p2
    print("point_total ", point_total) #DEBUG\\
    print("Puntaje Actual:\n", 
          point_p1, "P1\n",
          point_p2, "P2\n", 
          "Turno Jugador ", player_actual)
    print()
    print(tab_game)
    print()
    print(tab_answer, "Tab_answer\n") #Tablero Respuesta #DEBUG\\
    #Turno P1
    
    if player_actual == 1:
        player_result = play_cards(tab_game, tab_answer, c)
        #Puntaje
        if player_result[0] == True:
            point_p1 += 1
            player_actual = 2
        elif player_result[0] == False:
            point_p1 += 0
            tab_game = player_result[1]
            player_actual = 2
    elif player_actual == 2:
        player_result = play_cards(tab_game, tab_answer, c)
        #Puntaje
        if player_result[0] == True:
            point_p2 += 1
            player_actual = 1
        elif player_result[0] == False:
            point_p2 += 0
            tab_game = player_result[1]
            player_actual = 1
    
print("Juego finalizado ")   