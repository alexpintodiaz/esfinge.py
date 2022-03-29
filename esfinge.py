
#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
from turtle import back


print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

snacks = 14.4
shoes = 120
water = 25
bottle = 10
hat = 27.9
flashlight = 58
battery = 12
bag = 77
compass = 78.5
sunglasses = 27
tent = 41.8
knife = 36






#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")

print("shoes", shoes)
print("water", water)
print("flashlight", flashlight)




print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

bottled_water = water + bottle
functional_flashlight = flashlight + battery

print("Bottled water", bottled_water)
print("Functional flashlight", functional_flashlight)




print("¿El precio del agua en botella es menor al de la linterna funcional?")

print(bottled_water < functional_flashlight)





print("¿Cuanto valdría comprar unos snacks y una brujula?")

print(snacks + compass)





print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")

print(shoes <= 100)





#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")


backpack = 0

if bottled_water + functional_flashlight + shoes + tent + sunglasses <= 200:
    backpack = bottled_water + functional_flashlight + shoes + tent + sunglasses
    print("El valor de los elementos es menor a 200:", backpack)

elif bottled_water + functional_flashlight + knife + tent <= 200:
    backpack = bottled_water + functional_flashlight + knife + tent
    print("El valor de los elementos es menor a 200:", backpack)

else:
    print("ups! ninguno de los intentos fue exitoso")






#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")

backpack2 = 0

while backpack2 <= 200:
    backpack2 += bottled_water
    print("mochila dos", backpack2)

backpack2 -= bottled_water
print("nos pasamos, restaremos una botella de agua, ahora tenemos:", backpack2)





#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")


newBackpack1 = {
    "Agua en botella" : {"cantidad": 1, "Valor unitario": bottled_water},
    "Linterna funcional" : {"cantidad": 1, "Valor unitario": functional_flashlight},
    "Cuchillo" : {"cantidad": 1, "Valor unitario": knife},
    "Carpa" : {"cantidad": 1, "Valor unitario": tent}
}

newBackpack2 = {
    "Agua en botella" : {"cantidad": 5, "Valor unitario": bottled_water}
}






#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")


car = [{}] * 7

for section in range(7):
    car[section] = {
      "Agua en botella" : {"cantidad": 1, "Valor unitario": bottled_water},
      "Linterna funcional" : {"cantidad": 1, "Valor unitario": functional_flashlight},
      "Cuchillo" : {"cantidad": 1, "Valor unitario": knife},
      "Carpa" : {"cantidad": 1, "Valor unitario": tent}
    }
    print("Acabas de armar la mochila para el compartimiento: ", section + 1)


for i in car:
    print(i)







#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")


def addElements():
    for section in range(3):
        car[section] = {
          "Agua en botella" : {"cantidad": 1, "Valor unitario": bottled_water},
          "Linterna funcional" : {"cantidad": 2, "Valor unitario": functional_flashlight},
          "Brújula" : {"cantidad": 3, "Valor unitario": compass},
          "Snacks" : {"cantidad": 2, "Valor unitario": snacks}
        }
    imprimir(car)
    totalElements(car)


def totalElements(car):
    total_elements = {}

    print("Cálculo elementos en mochila")
    for backpack in car:
        for element, detail in backpack.items():
            if element in total_elements:
                total_elements[element] += detail["cantidad"]
            else:
                total_elements[element] = detail["cantidad"]

    print(total_elements)


def imprimir(structure):
    for object in structure:
        print(object)

addElements()







