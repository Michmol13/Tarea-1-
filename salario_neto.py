salario_bruto = 0
camisas_vendidas = 0
precio_camisa = 0
seguro_salud = 0.08
impuesto_renta = 0.12
ventas_totales = 0
regalias = 0.03
salario_neto = 0
	
salario_bruto = int(input("Ingrese el salario bruto del empleado:  "))

camisas_vendidas = int(input("Ingrese la cantidad de camisas vendidas:  "))

precio_camisa = int(input("Ingrese el precio de cada camisa:  "))


# Calcular descuentos del seguro_salud y impuesto_renta
seguro_salud = salario_bruto * 0.08
impuesto_renta = salario_bruto * 0.12

# Calcular ventas_totales
ventas_totales = precio_camisa * camisas_vendidas

# Calcular regalias
regalias = ventas_totales * 0.03

# Calcular salario neto
salario_neto = salario_bruto - seguro_salud - impuesto_renta + regalias

# Imprimir el resultado
print (f"El salario neto del empleado es {salario_neto}")