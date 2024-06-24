import math

base_triangulo = 0
altura_triangulo = 0
radio_circulo = 0 
ancho_brazos = 0
altura_brazos = 0
ancho_piernas = 0
altura_piernas = 0
ancho_cuerpo = 0
altura_cuerpo = 0 
area_triangulo = 0
area_circulo = 0
area_brazos = 0
area_piernas = 0
area_cuerpo = 0
area_total_del_muneco = 0 

base_triangulo = float(input("Ingrese la base del triángulo: "))
altura_triangulo = float(input("Ingrese la altura del triángulo: "))
radio_circulo = float(input("Ingrese el radio del círculo: "))
ancho_brazos = float(input("Ingrese el ancho de los brazos: "))
altura_brazos = float(input("Ingrese la altura de los brazos: "))
ancho_piernas = float(input("Ingrese el ancho de las piernas: "))
altura_piernas = float(input("Ingrese la altura de las piernas: "))
ancho_cuerpo = float(input("Ingrese el ancho del cuerpo: "))
altura_cuerpo = float(input("Ingrese la altura del cuerpo: "))

area_triangulo = (base_triangulo * altura_triangulo) / 2
area_circulo = math.pi * radio_circulo**2
area_brazos = ancho_brazos * altura_brazos
area_piernas = ancho_piernas * altura_piernas
area_cuerpo = ancho_cuerpo * altura_cuerpo

area_total_del_muneco = area_triangulo + area_circulo + (area_brazos * 2) + (area_piernas * 2) + area_cuerpo

print(f"El área total del muñeco es: {area_total_del_muneco:.2f}")