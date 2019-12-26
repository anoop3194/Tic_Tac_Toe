# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:06:33 2019

@author: Anoop
"""

import random

#game_input = ['null', 'X', 0, 'X', 0, 'X', 0, 'X', 0, 'X']
def board(game_input):
    print(game_input[7],"|",game_input[8],"|",game_input[9]) 
    print(game_input[4],"|",game_input[5],"|",game_input[6]) 
    print(game_input[1],"|",game_input[2],"|",game_input[3])

def player_input():
    marker=' '
    marker= input("Player-1 kindly choose your marker as 'X' or 'O' :")
    marker = marker.upper()
    if (marker == 'X' or marker == 'O'):
        #marker= input("Player-1 kindly choose your marker as 'X' or 'O'")
        if marker == 'X':
            return ('X' , 'O')
        else:
            return ('O', 'X')
    else:
        print("Kindly choose the correct marker")
        #player1, player2 = player_input()
        player_input()
        
#a,b = player_input()
#print(a,b)
def put_marker(game_input, marker, position):
    game_input[position]= marker

def win(game_input,marker):
    return((game_input[7]==game_input[4]==game_input[1]==marker) or
           (game_input[8]==game_input[5]==game_input[2]==marker) or
           (game_input[9]==game_input[6]==game_input[3]==marker) or 
           (game_input[1]==game_input[2]==game_input[3]==marker) or
           (game_input[4]==game_input[5]==game_input[6]==marker) or
           (game_input[7]==game_input[8]==game_input[9]==marker) or
           (game_input[7]==game_input[5]==game_input[3]==marker) or
           (game_input[1]==game_input[5]==game_input[9]==marker))

def choose_player():
    player=random.randint(1,2)
    if player==1:
        return 'player 1'
    else:
        return 'player 2'
    
def space(game_input, position):
    return game_input[position]== ' '

def full_board_check(game_input):
    for i in range (1,10):
        if space(game_input,i):
            return False
    return True
    
def player_choice(game_input):
     position=0
     while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
         position=int(input("Please choose your position(1-9) on numpad: "))
     return position
def play_again():
    choice=input("Would you like to play again (Y/N):")
    return choice.upper()

def main_fun():
    
    #while True:
        the_board=[' ']*10
        player1, player2 = player_input()
        print(player1 + " is player_1 sign")
        print(player2 + " is player_2 sign")
        turn=choose_player()
        print(turn +" will play frist")
        play_game=input("Are you ready to play(Y/N): ")
        play_game=play_game.upper()
        if (play_game == "Y"):
            game_on = True 
        else:
            game_on = False
        
        while game_on:
            if turn=='player 1':
                board(the_board)
                position=(player_choice(the_board))
                put_marker(the_board, player1, position)
                if win(the_board,player1):
                    board(the_board)
                    print("Player 1 has won yeyeyeye")
                    #play_again()
                    game_on=False
                else:
                    if full_board_check(the_board):
                        board(the_board)
                        print("game tie")
                        #play_again()
                    else:
                        turn='player 2'
            else:
                board(the_board)
                position=(player_choice(the_board))
                put_marker(the_board, player2, position)
                if win(the_board,player2):
                    board(the_board)
                    print("Player 2 has won yeyeyeye")
                    #play_again()
                    game_on=False
                else:
                    if full_board_check(the_board):
                        board(the_board)
                        print("game tie")
                        #play_again()
                    else:
                        turn='player 1'
        count=1
        #print(count)
        return count
count= main_fun()
if count==1:
    choice=play_again()
    if choice=='Y':
        main_fun()
    else:
        print("Thanks for playing")
else:
    main_fun()
        
        
    

                       
                    
        
    
    

 


    
    






  
    
