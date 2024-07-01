import random
import time
import pygame
import os


SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
VALUES = ('2', '3', '4', '5', '6', 'Jack', 'Queen', 'King', '7','Ace')


def create_deck(aleatorio=False):
    """Cria um baralho com 40 cartas"""
    baralho = [(v, n) for n in SUITS for v in VALUES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def split_deck(baralho):
    """Divide o baralho em duas partes"""
    return baralho[20:], baralho[:20]


def card_value(carta):
    valor, _ = carta
    return VALUES.index(valor)


def playing():
    
    create_deck()
    jogador1, jogador2 = split_deck(create_deck(True))  
    rodada = 1
    
    while len(jogador1) != 0 and len(jogador2) != 0: 
            
        print(f'Rodada: {rodada}')
        c1 = jogador1.pop(0)
        c2 = jogador2.pop(0)
        add = [c1, c2]
        random.shuffle(add)
        
        print(f'Jogador 1 joga: {c1[0]} de {c1[1]}')
        print(f'Jogador 2 joga: {c2[0]} de {c2[1]}')
            
        if card_value(c1) > card_value(c2):
            jogador1.extend(add)
            print('Jogador 1 vence a rodada!')
        elif card_value(c2) > card_value(c1):
            jogador2.extend(add)
            print('Jogador 2 vence a rodada!')
        else:
            print('Empate!')
            aux = [c1, c2]
            while True:
                if len(jogador1) == 0 or len(jogador2) == 0: break
                
                c1 = jogador1.pop(0)
                c2 = jogador2.pop(0)
                aux.extend((c1, c2))                
                print(f'Jogador 1 guarda: {c1[0]} de {c1[1]}')
                print(f'Jogador 2 guarda: {c2[0]} de {c2[1]}')

                if len(jogador1) == 0 or len(jogador2) == 0: break

                c1 = jogador1.pop(0)
                c2 = jogador2.pop(0)
                aux.extend((c1, c2)) 
                random.shuffle(aux)  
                            
                print(f'Jogador 1 joga: {c1[0]} de {c1[1]}')
                print(f'Jogador 2 joga: {c2[0]} de {c2[1]}')
                                                
                if card_value(c1) > card_value(c2):
                    jogador1.extend(aux)
                    print('Jogador 1 vence a rodada!')
                    break
                elif card_value(c2) > card_value(c1):
                    jogador2.extend(aux)
                    print('Jogador 2 vence a rodada!')
                    break
           
        print("Tamanho do baralho do jogador 1: ", len(jogador1))
        print("Tamanho do baralho do jogador 2: ", len(jogador2))
        print()  
        
        rodada += 1                    
                                                             
    if len(jogador2) == 0:
        print('Jogador 1 venceu!')
        winner = "Jogador 1 venceu!"
    elif len(jogador1) == 0:
        print('Jogador 2 venceu!') 
        winner = "Jogador 2 venceu!" 
        
    print(f'{rodada} rodadas foram jogadas!')   
    
playing()
            