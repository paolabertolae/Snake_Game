import pygame
import random
pygame.init()

azul = (26, 83, 92)
laranja = (255, 107, 107)
vermelha = (255, 230, 109)
amarelo = (247, 255, 247)

dimensoes = (500, 500)

d = 20

x = dimensoes[0]/2 - d/2
y = dimensoes[1]/2 - d/2

lista_cobra = [[x,y]]

delta_x = d
delta_y = 0

x_comida = round(random.randrange(0,dimensoes[0] - d)/d)*d
y_comida = round(random.randrange(0,dimensoes[1] - d)/d)*d

fonte = pygame.font.SysFont("hack", 35)

tela = pygame.display.set_mode((dimensoes))  
pygame.display.set_caption('Snake da Paola')

tela.fill(azul)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
  tela.fill(azul)
  for unidade in lista_cobra:
      pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d],10)


def mover_cobra(dx, dy, snake):


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        dx = -d
        dy = 0

      elif event.key == pygame.K_RIGHT:
        dx = +d
        dy = 0
      
      elif event.key == pygame.K_UP:
        dx = 0
        dy = -d

      elif event.key == pygame.K_DOWN:
        dx = 0
        dy = +d
  
  #           c  x
  x_novo = snake[-1][0] + dx
  #           c  y
  y_novo = snake[-1][1] + dy

  snake.append([x_novo, y_novo]) 
  del snake[0]

  return dx, dy, snake
        


def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
  head = lista_cobra[-1]

  x_novo = head[0] + dx
  y_novo = head[1] + dy

  if head[0] == x_comida and head[1] == y_comida:
    lista_cobra.append([x_novo, y_novo])
    x_comida = round(random.randrange(0, dimensoes[0]-d)/d)*d
    y_comida = round(random.randrange(0, dimensoes[1]-d)/d)*d


  pygame.draw.rect(tela, vermelha, [x_comida, y_comida, d, d],10)

  return x_comida, y_comida, lista_cobra


def verifica_parede(lista_cobra):
  head = lista_cobra[-1]
  x = head[0]
  y = head[1]

  if x not in range(-1,dimensoes[0]) or y not in range(-1,dimensoes[1]):
    raise Exception

def verifica_mordeu_cobra(lista_cobra):
  head = lista_cobra[-1]
  corpo = lista_cobra.copy()

  del corpo[-1]
  for x, y in corpo:
    if x == head[0] and y == head[1]:
      raise Exception


def atualizar_pontos(lista_cobra):
  pts = str(len(lista_cobra))
  score = fonte.render("Pontuação: " + pts, True, amarelo)
  tela.blit(score, [0,0])


while True: 
  pygame.display.update()


  delta_x, delta_y, lista_cobra = mover_cobra(delta_x, delta_y, lista_cobra)

  desenha_cobra(lista_cobra)
  x_comida, y_comida, lista_cobra = \
    verifica_comida(delta_x, delta_y,x_comida, y_comida, lista_cobra)

  print(lista_cobra)
  verifica_parede(lista_cobra)
  verifica_mordeu_cobra(lista_cobra)
  atualizar_pontos(lista_cobra)

  clock.tick(7)

