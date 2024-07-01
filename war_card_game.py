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


def card_draw():
    caminho_atual = os.path.abspath(__file__)
    diretorio_atual = os.path.dirname(caminho_atual)
    imagens = {}
    for naipe in SUITS:
        for valor in VALUES:
            nome_arquivo = f"{valor.lower()}_of_{naipe.lower()}.png"
            caminho = os.path.join(diretorio_atual, "PNG-cards-1.3", nome_arquivo)
            imagem = pygame.image.load(caminho)
            imagens[(valor, naipe)] = imagem
    return imagens


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo de Cartas - War')


GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
CARD_SIZE = (100, 150)


def playing():
    
    create_deck()
    jogador1, jogador2 = split_deck(create_deck(True))  
    rodada = 1
    
    imagens_cartas = card_draw()
    
    run = True
    empate = False

    while len(jogador1) != 0 and len(jogador2) != 0 and run: 
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
                
            if evento.type == pygame.MOUSEBUTTONDOWN and not empate:
                
                print(f'Rodada: {rodada}')
                c1 = jogador1.pop(0)
                c2 = jogador2.pop(0)
                add =[c1, c2]
                random.shuffle(add)
                
                print(f'Jogador 1 joga: {c1[0]} de {c1[1]}')
                print(f'Jogador 2 joga: {c2[0]} de {c2[1]}')
                
                screen.fill(GREEN)
                
                imagem_c1_redimensionada = pygame.transform.scale(imagens_cartas[c1], CARD_SIZE)
                imagem_c2_redimensionada = pygame.transform.scale(imagens_cartas[c2], CARD_SIZE)

                screen.blit(imagem_c1_redimensionada, (150, 225))
                screen.blit(imagem_c2_redimensionada, (550, 225))
                    
                if card_value(c1) > card_value(c2):
                    jogador1.extend([c1, c2])
                    print('Jogador 1 vence a rodada!')
                    result = "Jogador 1 vence a rodada!"
                elif card_value(c2) > card_value(c1):
                    jogador2.extend([c1, c2])
                    print('Jogador 2 vence a rodada!')
                    result = "Jogador 2 vence a rodada!"
                else:
                    print('Empate!')
                    result = "             Empate!"
                    pygame.display.flip() 
                    
                    empate = True
                    
                print("Tamanho do baralho do jogador 1: ", len(jogador1))
                print("Tamanho do baralho do jogador 2: ", len(jogador2))
                print()  
                        
                font = pygame.font.Font(None, 36)
                text = font.render(result, True, WHITE)
                screen.blit(text, (250, 100))
                
                pygame.display.flip()
                
                rodada += 1
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN and empate:

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
                    
                    screen.fill(GREEN)
                    
                    imagem_c1_redimensionada = pygame.transform.scale(imagens_cartas[c1], CARD_SIZE)
                    imagem_c2_redimensionada = pygame.transform.scale(imagens_cartas[c2], CARD_SIZE)

                    screen.blit(imagem_c1_redimensionada, (150, 225))
                    screen.blit(imagem_c2_redimensionada, (550, 225))
                                    
                    if card_value(c1) > card_value(c2):
                        jogador1.extend(aux)
                        print('Jogador 1 vence a rodada!')
                        result = "Jogador 1 vence a rodada!"
                        break
                    elif card_value(c2) > card_value(c1):
                        jogador2.extend(aux)
                        print('Jogador 2 vence a rodada!')
                        result = "Jogador 2 vence a rodada!"
                        break
                        

                print("Tamanho do baralho do jogador 1: ", len(jogador1))
                print("Tamanho do baralho do jogador 2: ", len(jogador2))
                print()  
                        
                font = pygame.font.Font(None, 36)
                text = font.render(result, True, WHITE)
                screen.blit(text, (250, 100))
               
                empate = False
                
                pygame.display.flip()
                

                                                             
    if len(jogador2) == 0:
        print('Jogador 1 venceu!')
        winner = "Jogador 1 venceu!"
    elif len(jogador1) == 0:
        print('Jogador 2 venceu!') 
        winner = "Jogador 2 venceu!" 
        
    print(f'{rodada} rodadas foram jogadas!')   
    
    screen.fill(GREEN)
    font = pygame.font.Font(None, 72)
    text = font.render(winner, True, WHITE)
    screen.blit(text, (200, 250))
    pygame.display.flip()           
  
      
playing()
    
pygame.quit()
            