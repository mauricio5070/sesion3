# creacion de la clase animal y pato

class Animal:

    numero_de_animales=0
    def __init__(self):

        print('Se ha creado un animal')

        Animal.numero_de_animales +=1
    #atributos de la instancia

        self.estoy_vivo= True

    def crecer(self):
        print('Soy un animal y estoy creciendo')

    def respirar(self):
        print('Soy un animal y estoy respirando')

    def reproducir(self):
        print('Soy un animal y me estoy reproduciendo')
    def morir(self):
        self.estoy_vivo= False
        print('Soy un animal muerto')

    def vivir_o_morir(self):
        self.estoy_vivo= not self.estoy_vivo


class Pato(Animal):
    def __init__(self, nombre_pato='Pato',ala_color='Blanco',pico_color='Naranja'):
        super().__init__()
        self.nombre_pato=nombre_pato
        self.ala_color=ala_color
        self.pico_color=pico_color
        print('Se ha creado un PATO y me llamo: {}'.format(self.nombre_pato))

    #def respirar(self):
         #  print('Ademas de ser un PATO yo.....')
         #super().respirar()


    #sobrecarca para imprimir pato
    def __str__(self):
        return 'Soy un pato y me llamo {}' \
               ', tengo las alas color {}' \
               ' y el pico color {}'.format(self.nombre_pato, self.ala_color, self.pico_color)



    #def __repr__(self):
        #return 'Soy un pato y me llamo {}' \
            #   ', tengo las alas color {} ' \
              # ' y el pico color {}'. format(self.nombre_pato,self.ala_color,self.pico_color)


    #sobrecarga de la suma
    def __add__(self,other):
        return Pato('FrankenPato',ala_color=self.ala_color,
                    pico_color=other.pico_color)





animalito= Animal()

print('Estoy vivo?', animalito.estoy_vivo)
animalito.vivir_o_morir()
print('Estoy vivo?', animalito.estoy_vivo)
print('------------------------------------CREAMOS UN PATO -----------------------------------------------------------------')
patito= Pato('Julio')
patito2= Pato('Bernardo','Negro','Amarillo')
patito.crecer()
print('pato Estoy vivo?', patito.estoy_vivo)
patito.reproducir()
patito.respirar()
patito.vivir_o_morir()
print('pato Estoy vivo?', patito.estoy_vivo)
print('-----------------------------PRUEBA SOBRECARGA STR Y ADD--------------------------------------------------------------')

print(patito)
print(patito2)

print('Ahora los sumamos........')
print(patito2+patito)


print('------------------------------------CONTEO DE ANIMALES --------------------------------------------------------------')
print('Numero de animales:', patito.numero_de_animales)


input()