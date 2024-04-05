import pygame
import numpy as np
import gc                       
import time

# creamos la ventana donde se mostrara el juego
pantallaJuego=pygame.display.set_mode((1200,675))    
pygame.init()

# la funcion buscaminas  mostrara en pantalla una imagen donde esta una cudricula 
# en donde dependiendo la posicion en donde se de click mostrara una bandera o una mina 
# llevara un registro de puntuacion y contara con el boton regresar para que pueda volver a jugar 
def Buscaminas():
    juego1=pygame.image.load("fondomina.png")
    juego=pygame.transform.scale(juego1,(1200,675))
    imagen1=pygame.image.load("banderamina.png")
    imagen=pygame.transform.scale(imagen1,(70,70))
    imagenExp1=pygame.image.load("mina.png")
    imagenExp=pygame.transform.scale(imagenExp1,(70,70))
    gameOver1=pygame.image.load("gameover.jpg")
    gameOver=pygame.transform.scale(gameOver1,(300,200))
    pantallaJuego.blit(juego,(0,0))
    pygame.display.update()
    miMatriz=np.random.randint(2,size=[5,5])
    puntaje=0
    while True:
        for eventos1 in pygame.event.get():
            if eventos1.type==pygame.QUIT:                              
                print("Saliendo...")
                exit()

            if eventos1.type==pygame.MOUSEBUTTONDOWN:   
                x,y=eventos1.pos 
                if x>=966 and y>=575 and x<=1167 and y<=632:           
                    print("Boton RETURN...")
                    gc.collect(generation=2)                           
                    Menu()                                          

            if eventos1.type==pygame.MOUSEBUTTONDOWN:
                x,y=eventos1.pos
                #Cuadricula 1:-------------------------------------------------------------------------------------------------------
                if x>=375  and x<=457 and y>=85 and y<=170:              
                    print(miMatriz)
                    posX=0                                            
                    posY=0                                              
                    if (miMatriz[posX] [posY]==0):                      
                        puntaje=puntaje+1                              
                        miMatriz[posX] [posY]=2                        
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(375,80))           
                    
                    if (miMatriz[posX] [posY]==1):                      
                        print("IF de Pierdes...")               
                        pantallaJuego.blit(imagenExp,(375,80))          
                        pantallaJuego.blit(gameOver,(25,212))          
                        puntuacionTxt=pygame.font.Font(None,50)      
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))   
                        gc.collect(generation=2)                       
                        miMatriz=miMatriz+3                         
                #Cuadricula 2:-------------------------------------------------------------------------------------------------------    
                if x>=468 and x<=550 and y>=85  and y<=170:
                    print(miMatriz)
                    posX=0
                    posY=1
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(468,80))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(468,80))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3  
                #Cuadricula 3:-------------------------------------------------------------------------------------------------------    
                if x>=564 and x<=642 and y>=85 and y<=170:
                    print(miMatriz)
                    posX=0
                    posY=2
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(564,80))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(564,80))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 4:-------------------------------------------------------------------------------------------------------    
                if x>=652 and x<=734 and y>=85 and y<=170:
                    print(miMatriz)
                    posX=0
                    posY=3
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(653,80))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(653,80))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 5:-------------------------------------------------------------------------------------------------------    
                if x>=744  and x<=826 and y>=85 and y<=170:
                    print(miMatriz)
                    posX=0
                    posY=4
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(744,80))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(744,80))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 6:-------------------------------------------------------------------------------------------------------    
                if x>=375  and x<=457  and y>=178 and y<=260:
                    
                    
                    print(miMatriz)
                    posX=1
                    posY=0
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(375,178))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(375,178))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3   
                #Cuadricula 7:-------------------------------------------------------------------------------------------------------    
                if x>=468 and x<=550 and y>=178 and y<=260:
                    print(miMatriz)
                    posX=1
                    posY=1
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(468,178))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(468,178))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3 
                #Cuadricula 8:-------------------------------------------------------------------------------------------------------    
                if x>=564 and x<=642 and y>=178 and y<=260:
                    print(miMatriz)
                    posX=1
                    posY=2
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(564,178))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(564,178))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3 
                #Cuadricula 9:-------------------------------------------------------------------------------------------------------    
                if x>=652 and x<=734 and y>=178 and y<=260:
                    print(miMatriz)
                    posX=1
                    posY=3
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(653,178))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(653,178))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 10:-------------------------------------------------------------------------------------------------------    
                if x>=744  and x<=826 and y>=178 and y<=260:
                    print(miMatriz)
                    posX=1
                    posY=4
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(744,178))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(749,199))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 11:-------------------------------------------------------------------------------------------------------    
                if x>=375  and x<=457 and y>=270 and y<=350:
                    print(miMatriz)
                    posX=2
                    posY=0
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(375,270))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(375,270))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 12:-------------------------------------------------------------------------------------------------------    
                if x>=468 and x<=550 and y>=270 and y<=350:
                    print(miMatriz)
                    posX=2
                    posY=1
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(468,270))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(468,270))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 13:-------------------------------------------------------------------------------------------------------    
                if x>=564 and x<=642 and y>=270 and y<=350:
                    print(miMatriz)
                    posX=2
                    posY=2
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(564,270))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(564,270))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 14:-------------------------------------------------------------------------------------------------------    
                if x>=652 and x<=734 and y>=270 and y<=350:
                    print(miMatriz)
                    posX=2
                    posY=3
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(653,270))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(653,270))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 15:-------------------------------------------------------------------------------------------------------    
                if x>=744  and x<=826 and y>=270 and y<=350:
                    print(miMatriz)
                    posX=2
                    posY=4
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(744,270))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(744,270))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 16:-------------------------------------------------------------------------------------------------------    
                if x>=375  and x<=457 and y>=364  and y<=444:
                    print(miMatriz)
                    posX=3
                    posY=0
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(375,364))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(375,364))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 17:-------------------------------------------------------------------------------------------------------    
                if x>=468 and x<=550 and y>=364  and y<=444:
                    print(miMatriz)
                    posX=3
                    posY=1
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(468,364))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(468,364))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 18:-------------------------------------------------------------------------------------------------------    
                if x>=564 and x<=642 and y>=364  and y<=444:
                    print(miMatriz)
                    posX=3
                    posY=2
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(564,364))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(564,364))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 19:-------------------------------------------------------------------------------------------------------    
                if x>=652 and x<=734 and y>=364  and y<=444:
                    print(miMatriz)
                    posX=3
                    posY=3
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(653,364))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(653,364))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 20:-------------------------------------------------------------------------------------------------------    
                if x>=744  and x<=826 and y>=364  and y<=444:
                    print(miMatriz)
                    posX=3
                    posY=4
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(744,364))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(744,364))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 21:-------------------------------------------------------------------------------------------------------    
                if x>=375  and x<=457 and y>=456 and y<=536:
                    print(miMatriz)
                    posX=4
                    posY=0
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(375,456))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(375,456))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 22:-------------------------------------------------------------------------------------------------------    
                if x>=468 and x<=550 and y>=456 and y<=536:
                    print(miMatriz)
                    posX=4
                    posY=1
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(468,456))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(468,456))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 23:-------------------------------------------------------------------------------------------------------    
                if x>=564 and x<=642 and y>=456 and y<=536:
                    print(miMatriz)
                    posX=4
                    posY=2
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(564,456))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(564,456))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 24:-------------------------------------------------------------------------------------------------------    
                if x>=652 and x<=734 and y>=456 and y<=536:
                    print(miMatriz)
                    posX=4
                    posY=3
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(652,456))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(652,456))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
                #Cuadricula 25:-------------------------------------------------------------------------------------------------------    
                if x>=744  and x<=826 and y>=456 and y<=536:
                    print(miMatriz)
                    posX=4
                    posY=4
                    if (miMatriz[posX] [posY]==0):
                        puntaje=puntaje+1
                        miMatriz[posX] [posY]=2
                        print("IF de +1 Punto...")
                        pantallaJuego.blit(imagen,(744,456))
                    
                    if (miMatriz[posX] [posY]==1):
                        print("IF de Pierdes...")
                        pantallaJuego.blit(imagenExp,(744,456))
                        pantallaJuego.blit(gameOver,(25,212))
                        puntuacionTxt=pygame.font.Font(None,50)
                        numeroPuntaje=puntuacionTxt.render(F"{puntaje}",0,(240,60,90)) 
                        pantallaJuego.blit(numeroPuntaje,(155,100))
                        gc.collect(generation=2)
                        miMatriz=miMatriz+3
        pygame.display.update()

# la funcion menuayuda mostrar en pantalla como se debe jugar
#junto con el boton volver para empezar el juego o salir si lo desea
def MenuAyuda():
    ayuda1=pygame.image.load("fondoayuda.png") 
    ayuda=pygame.transform.scale(ayuda1,(1200,675))       
    pantallaJuego.blit(ayuda,(0,0))
    pygame.display.update()

    while True:
        for eventos2 in pygame.event.get():
            if eventos2.type==pygame.QUIT:
                print("Saliendo...")
                exit()
            if eventos2.type==pygame.MOUSEBUTTONDOWN:   
                x,y=eventos2.pos 
                if x>=976 and y>=601 and x<=1186 and y<=665:
                    print("Boton RETURN...")
                    Menu()
        pantallaJuego.blit(ayuda,(0,0))
        pygame.display.update()

# la funcion menu mustrara en pantalla las opciones disponibles las cuales son 
# jugar , salir , y una ayuda donde se mostrar como se debe jugar 
def Menu():
    menuPrincipal1=pygame.image.load("fondoinicio.png")
    menuPrincipal=pygame.transform.scale(menuPrincipal1,(1200,675))
    pantallaJuego.blit(menuPrincipal,(0,0))
    pygame.display.update()
    while True:
        for eventos in pygame.event.get():
            if eventos.type==pygame.QUIT:                          
                print("Saliendo...")
                exit()

            if eventos.type==pygame.MOUSEBUTTONDOWN:
                x,y=eventos.pos
                if x>=430 and y>=283 and x<=767 and y<=393:        
                    print("Boton PLAY...")
                    Buscaminas()

            if eventos.type==pygame.MOUSEBUTTONDOWN:
                x,y=eventos.pos
                if x>=1087 and y>=585 and x<=1180 and y<=656:      
                    print("BOTON AYUDA...")
                    MenuAyuda()

            if eventos.type==pygame.MOUSEBUTTONDOWN:  
                x,y=eventos.pos
                if x>=430 and y>=435 and x<=767 and y<=545:        
                    print("Boton EXIT...")
                    exit()

        pantallaJuego.blit(menuPrincipal,(0,0))
        pygame.display.update()
# la funcion menu carga muetra en pantalla una serie de imagenes que simalan que el juego esta cargando  
 
def Carga():
    presentacio1=pygame.image.load("fondo1.png")
    presentacion1=pygame.transform.scale(presentacio1,(1200,675))
    presentacio2=pygame.image.load("fondo2.png")
    presentacion2=pygame.transform.scale(presentacio2,(1200,675))
    presentacio3=pygame.image.load("fondo3.png")
    presentacion3=pygame.transform.scale(presentacio3,(1200,675))   
    pantallaJuego.blit(presentacion1,(0,0))
    pygame.display.update()     
    time.sleep(0.2)            
    pantallaJuego.blit(presentacion2,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion3,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion1,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion1,(0,0))
    pygame.display.update()    
    time.sleep(0.5)
    pantallaJuego.blit(presentacion2,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion3,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion1,(0,0))
    pygame.display.update()    
    time.sleep(0.5)
    pantallaJuego.blit(presentacion2,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    pantallaJuego.blit(presentacion3,(0,0))
    pygame.display.update()     
    time.sleep(0.2)
    Menu() 



if __name__ == '__main__':
    Carga()