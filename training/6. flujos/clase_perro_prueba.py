#Generar una clase de un perro que tenga altura, peso, nombre, que ladre, una condicional y darle
#una estructura if que si el perro tiene sobrepeso duerma o el contrario entrene.

class Perro:

    peso_ideal = 20  # Este valor puede cambiar dependiendo de la raza o tamaño del perro

    def __init__(self, name, peso, height):
        self.name = name
        self.peso = peso
        self.height = height

    def ladrar(self):
        print(f"{self.name} dice: ¡Guau guau!")

    def evaluar_sobrepeso(self):
        # Definimos un peso límite para determinar si tiene sobrepeso
        
        if self.peso > Perro.peso_ideal:
            print(f"{self.name} tiene sobrepeso, ¡A entrenar!")
        else:
            print(f"{self.name} está en forma, ¡Bien hecho!")

    def __add__(self, val2): 
        return Perro(self.name, self.peso + val2.peso, self.height) 


# Ejemplo de uso
perro1 = Perro("Firulais", 50, 25)
perro2 = Perro("Max", 45, 18)

perro1.ladrar()
perro1.evaluar_sobrepeso()

perro2.ladrar()
perro2.evaluar_sobrepeso()

print(perro1+perro2)