import pygame
import sys

pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pong')

verde = (0,128,0)
vermelho = (255,0,0)
preto = (0,0,0)
branco = (128,128,128)
azul = (0,255,128)
amarelo = (0,0,0)

raquete_largura = 10
raquete_altura = 100
raquete_esqueda_y = altura//2 - raquete_altura//2
raquete_direita_y = altura//2 - raquete_altura//2
bola_x, bola_y = largura//2,altura//2
bola_dx, bola_dy = 5,5
velocidade_raquete = 5

 while True:

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                        teclas = pygame.key.get.pressed()
                        if teclas[pygame.k_w]:
                              raquete_esqueda_y -= velocidade_raquete
                        if teclas[pygame.k_s]:
                              raquete_esqueda_y += velocidade_raquete
                        if teclas[pygame.k_UP]:
                              raquete_direita_y -= velocidade_raquete
                        if teclas[pygame.k_DOWN]:
                              raquete_direita_y += velocidade_raquete

                        bola_x += bola_dx
                        bola_y += bola_dy

                        if bola_y <=0 or bola_y >= altura - 10:
                          bola_dy = - bola_dy     

                          if bola_x <= 20 and raquete_esqueda_y < bola_y < raquete_esqueda_y + raquete_altura:
                                bola_dx = -bola_dx
                          if bola_x <=  largura - 20 and raquete_direita_y < bola_y < raquete_direita_y + raquete_altura:
                                bola_dx = -bola_dx

                          if bola_dx < 0 or bola_x > largura:
                                      bola_x,bola_y = largura//2,altura//2

                                      tela.fill(preto)
                                      pygame.draw.rect(tela,azul,(10,raquete_esqueda_y,raquete_largura,raquete_altura))
                                      pygame.draw.rect(tela,azverde,(-20,raquete_direita_y,raquete_largura,raquete_altura))
                                      pygame.draw.ellipse(tela,amarelo,(bola_x,bola_y,10,10))

                                      pygame.display.flip()

                                      pygame.time.Clock().tick(60)

                                      
                                





