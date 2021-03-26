#IMPORTANTE: CORREGIR MATRIZ PARA PODER ELIMINAR LAS CARTAS
#CREAR INTERFAZ DE MATRIZ

import random as rng
import numpy as np
def playcards(c):
    l = []
    for i in range(1, c + 1):
        l.append(i) #lista con los pares
        l.append(i)
    rng.shuffle(l) #lista shuffeleada
    cardsplay = np.zeros((2, c)) #lista de juego con 0    
    for j in range(0, (c)): #reemplazo de 0 por numeros, esta es la lista de juego
        cardsplay[0][j] = l[0]
        l.pop(0)
    for j in range(0, (c)):
        cardsplay[1][j] = l[0]
        l.pop(0)
    return(cardsplay)

def zerocards(c):
    tab_zeros = np.zeros((2, c))
    return(tab_zeros)

def Ui(tab_):
    row = tab_.shape[0]
    col = tab_.shape[1]
    l1 = ["0"] * col #Creo lista string para reemplazar
    l2 = ["0"] * col
    ui = [l1, l2]
    for i in range(0, row): #Compruebo y reemplazo para la interfaz
        for j in range(0, col):         
            if tab_[i][j] == 0:
                ui[i][j] = ' █ '
            elif tab_[i][j] > 0.9:
                ui[i][j] = tab_[i][j]
            elif tab_[i][j] == 0.9:
                ui[i][j] = '  *  '
    for i in range(0, row): #Mostrar interfaz
        print("\n")
        for j in range(0, col):
            print(ui[i][j], '', end='')
    print("\n")
    return(ui)

def play_cards(tab_game, tab_answer, c):
    #Tablero inicio de turno
    tab_back = np.copy(tab_game)
    play_turn = 0
    while play_turn != 2:
        #Seleccion 1
        if play_turn == 0:
            print("First selection") 
            print("-- Choose Row -- (0 or 1): ")
            row1 = int(input())
            print("|| Choose Column || (0 to ",c-1, "): ")
            col1 = int(input())
            #Coordenadas 1
            coord1 = (row1, col1)
            #Comprobar si ya esta seleccionado
            if tab_game[row1, col1] == 0:
                #Mostrar primera seleccion
                tab_game[row1, col1] = tab_answer[row1, col1]
                Ui(tab_game)
                play_turn += 1
            else:
                print("Error, The card was chosen already")
                play_turn = 0
        #Seleccion 2    
        elif play_turn == 1:
            print("Second Selection") 
            print("-- Choose Row -- (0 or 1): ")
            row2 = int(input())
            print("|| Choose Column || (0 to ",c-1, "): ")
            col2 = int(input())
            #Coordenadas 2
            coord2 = (row2, col2)            
            #Repite Segunda eleccion en caso de seleccionar la misma
            if coord1 == coord2: 
                print("Error, You choose the same card")
                play_turn = 1
            elif tab_game[row2, col2] != 0:
                print("Error, The card was chosen already")
                play_turn = 1
            else:
                #Comprobar Respuesta
                if tab_game[row1, col1] == tab_answer[row2, col2]:
                    #Mostrar segunda seleccion
                    tab_game[row2, col2] = tab_answer[row2, col2]
                    Ui(tab_game)
                    print("+ + + + + + + + + + + \n+ + + P O I N T + + +\n+ + + + + + + + + + + \n") 
                    tab_game[row2, col2] = 0.9
                    tab_game[row1, col1] = 0.9
                    return(True, tab_game)
                elif tab_game[row1, col1] != tab_answer[row2, col2]:
                    #Mostrar segunda seleccion
                    tab_game[row2, col2] = tab_answer[row2, col2]
                    Ui(tab_game)
                    print("- - - - - - - - - -\n- - - F A I L - - -\n- - - - - - - - - -\n")  
                    #Reiniciar Tablero
                    tab_game = np.copy(tab_back)
                    return(False, tab_back)
        
c = int(input("How many pairs to play?: "))

#Tablas
tab_answer = playcards(c)
tab_game = zerocards(c)
tab_back = np.copy(tab_game)

#puntaje
point_total = 0
point_max = c
point_p1 = 0
point_p2 = 0

#Turnos
player_actual = 1
player_result = 0

while point_total < point_max - 1:
    point_total = point_p1 + point_p2
    print("|||Players Points:\n|||", 
          point_p1, "P1\n|||",
          point_p2, "P2\n|||", 
          "Player Turn: ", player_actual)
    print()
    #BETA
    Ui(tab_game)
    print()
    #Turno P1
    if player_actual == 1:
        player_result = play_cards(tab_game, tab_answer, c)
        #Puntaje
        if player_result[0] == True:
            point_p1 += 1
            player_actual = 1
        elif player_result[0] == False:
            point_p1 += 0
            tab_game = np.copy(player_result[1])
            player_actual = 2
    elif player_actual == 2:
        player_result = play_cards(tab_game, tab_answer, c)
        #Puntaje
        if player_result[0] == True:
            point_p2 += 1
            player_actual = 2
        elif player_result[0] == False:
            point_p2 += 0
            tab_game = np.copy(player_result[1])
            player_actual = 1
#Crear Contador final para dar la win a jugador 1 o 2
if point_p1 > point_p2:
    print("PLAYER 1 WIN WITH ", point_p1, "POINTS!")
elif point_p1 < point_p2:
    print("PLAYER 2 WIN WITH ", point_p2, "POINTS!")
else:
    print("TIE!")
print("GAME OVER")   