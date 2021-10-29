# Convertir de pesos mexicanos a dolares
print("Convertir de pesos mexicanos a dolares")
print("Valor de 1 USD = $20 pesos MXN")
pesos_mxn = input("¿Cuántos pesos mexicanos tienes? ")
pesos_mxn = float(pesos_mxn) # float permite números decimales
valor_dolar = 20 # Asignación de valor por dolar
cantidad_dolares = pesos_mxn / valor_dolar # Calcula la cantidad de dolares
cantidad_dolares = round(cantidad_dolares, 2) # Redondea decimales
cantidad_dolares = str(cantidad_dolares) # Convierte tipo número a string 
print("---> Tienes $" + cantidad_dolares + ' dolares.') # Muestra resultado

# Convertir de dolares a pesos mexicanos
print("Convertir de dolares a pesos mexicanos")
print("Valor de 1 peso MXN = 0.05 USD")
dolares = input("¿Cuántos dolares tienes? ")
dolares = float(dolares)
valor_peso_mxn = 0.05
cantidad_pesos_mxn = dolares / valor_peso_mxn
cantidad_pesos_mxn = round(cantidad_pesos_mxn, 2)
cantidad_pesos_mxn = str(cantidad_pesos_mxn)
print("---> Tienes " + cantidad_pesos_mxn + " pesos MXN")