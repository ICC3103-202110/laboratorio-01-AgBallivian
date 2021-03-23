# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:02:02 2021

@author: kucho
"""

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
    gcard = np.zeros((2, c))
    return(gcard)

def card_choose(gcard, c_play):
    tmp_card = gcard
    print("Primera Seleccion") 
    row1 = int(input("seleccione fila (0 o 1): "))
    col1 = int(input("seleccione columna: "))
    coord1 = (row1, col1)
    gcard[row1, col1] = c_play[row1, col1]
    print(gcard)
    print("Segunda Seleccion") 
    row2 = int(input("seleccione fila(0 o 1): "))
    col2 = int(input("seleccione columna: "))
    coord2 = (row2, col2)
    gcard[row2, col2] = c_play[row2, col2]
    print(gcard)
    if coord1 == coord2: 
        print("Error, seleccionaste la misma carta")
        card_choose(tmp_card, c_play)
    if gcard[row1, col1] == gcard[row2, col2]:
        print("+ + + P U N T O + + +")
        return(1, gcard)
    elif gcard[row1, col1] != gcard[row2, col2]:
        print("- - - F A I L - - -")   
        return(0, gcard)

    
def game():
    #c = int(input("Cartas a jugar: "))
    c = 2
    c_play = playcards(c)
    gcard = zerocards(c)
    tmp_card = gcard
    tot_points = 0 #para ternimar el juego
    p1_points = 0
    p2_points = 0
    player = 1
    while tot_points <= c*2:
        print("Puntaje Actual:\n", 
              p1_points, "P1\n",
              p2_points, "P2\n", 
              "Turno Jugador ", player)
        print()
        print(gcard)
        print(tmp_card, "temporal")
        print()
        print(c_play, "Cheat\n") #Cheat
        
        if player == 1:
            #print("turno del jugador 1")
            result = card_choose(gcard, c_play)
            if result[0] == 1:
                p1_points = p1_points + 1
            elif result[0] == 0:
                print("Nope")
            player = player + 1
        elif player == 2:
            #print("turno del jugador 2")
            result = card_choose(gcard, c_play)
            if result[0] == 1:
                p2_points = p2_points + 1
            elif result[0] == 0:
                print("Nope")
            player = player - 1

        tot_points = p1_points + p2_points
    
    playerxwin = 1
    return(playerxwin)
    

game()

#CREAR TEMPORAL QUE GUARDE LA TARJETA Y QUE SE MUESTRE LA TARJETA CORRECTAMENTE