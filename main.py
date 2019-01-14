import turtle
import random#importamos el modulo random para que vayan avanzando las tortugas. simula el lanzamiento de un lado

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ("red", "blue", "green", "orange")
    
    def __init__(self, width, height):
        '''self.width = width  #ya no hace falta porque lo hemos puesto abajo en el screen.setup
        self.height = height'''
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()
    
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])#lo he cambiado de abajo a arriba para que el cambio de negro a color sea tan rapido que no se aprecie
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
 
            self.corredores.append(new_turtle)
            
    def competir(self):
         
         hayGanador = False#creamos esta variable y la declaro False porque estan todas en la linea de salida
         
         while not hayGanador:
             for tortuga in self.corredores:
                 avance = random.randint(1,6)#declaramos esta varuable para que avancen segun lo que vaya sacando el dado(numero random entre 1 y 6) y como lo tiene que hacer con todas las tortugas lo metemos en un bucle
                 tortuga.forward(avance)#avanza lo que saca random
                 
                 if tortuga.position()[0] >= self.__finishLine:#hemos pedido la posicion. nos da una tupla y el [0] es la primera coordenada de la posicion que nos da, por eso se la ponemos la otra es la posicion de la tortuga
                     hayGanador = True
                     print("la tortuga de color {} ha ganado".format(tortuga.color()[0]))#tortuga.color actua como un getter. Nos tiene que dar el color de la tortuga ganadora y como es una funcion se ponen los ()
                     break#esto lo ponemos para que encuanto llegue una, no termine el bucle






if __name__ == "__main__":
    circuito = Circuito(640, 480)
    circuito.competir()#invoco la funcion para que avancen