class ClaseConGetterySetter():
    def __init__(self):
        self.__propieda_privada = None#como no puedo acceder a propiedad privada por que lo hemos declarado como privado, nos tenemos que crear en modulo de abajo
        
    def setPropiedadPrivada(self, valor):
        self.propiedad_privada = valor
        
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
#esto es lo mismo que:
    def PropiedadPrivada(self, valor=None):#aunque parezca redundate hay que poner el valor por defecto, en este acso None porque si no casca
        if valor == None:
            return self.__propiedad_privada#Getter consultas el valor
        else:
            self.__propiedad_privada = valor#setter le das un valor
    def __str__(self):
        return "ClaseConGetterYSetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
        
if __name__ == "__main__":
    c = ClaseConGetterySetter()