import pygame

pygame.init()

while 1:
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    print "LEFT"

  if keys[pygame.K_RIGHT]:
    print "RIGHT"

  if keys[pygame.K_UP]:
    print "UP"

  if keys[pygame.K_DOWN]:
    print "DOWN"
