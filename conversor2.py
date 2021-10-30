menu = """
Bienvenido al conversor de monedas a dolares 💵🤑
1 - Pesos colombianos
2- Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    print("Convertir de pesos colombianos a dolares")
    print("Valor de 1 USD = $3875 pesos colombianos")
    cantidad_pesos = input("¿Cuántos pesos colombianos tienes? ")
    cantidad_pesos = float(cantidad_pesos) # float permite números decimales
    valor_dolar = 3875 # Asignación de valor por dolar
    cantidad_dolares = cantidad_pesos / valor_dolar # Calcula la cantidad de dolares
    cantidad_dolares = round(cantidad_dolares, 2) # Redondea decimales
    cantidad_dolares = str(cantidad_dolares) # Convierte tipo número a string 
    print("---> Tienes $" + cantidad_dolares + ' dolares.') # Muestra resultado
elif opcion == 2:
    print("Convertir de pesos argentinos a dolares")
    print("Valor de 1 USD = $65 pesos argentinos")
    cantidad_pesos = input("¿Cuántos pesos mexicanos tienes? ")
    cantidad_pesos = float(cantidad_pesos) # float permite números decimales
    valor_dolar = 65 # Asignación de valor por dolar
    cantidad_dolares = cantidad_pesos / valor_dolar # Calcula la cantidad de dolares
    cantidad_dolares = round(cantidad_dolares, 2) # Redondea decimales
    cantidad_dolares = str(cantidad_dolares) # Convierte tipo número a string 
    print("---> Tienes $" + cantidad_dolares + ' dolares.') # Muestra resultado
elif opcion == 3:
    print("Convertir de pesos mexicanos a dolares")
    print("Valor de 1 USD = $20 pesos MXN")
    cantidad_pesos = input("¿Cuántos pesos mexicanos tienes? ")
    cantidad_pesos = float(cantidad_pesos) # float permite números decimales
    valor_dolar = 20 # Asignación de valor por dolar
    cantidad_dolares = cantidad_pesos / valor_dolar # Calcula la cantidad de dolares
    cantidad_dolares = round(cantidad_dolares, 2) # Redondea decimales
    cantidad_dolares = str(cantidad_dolares) # Convierte tipo número a string 
    print("---> Tienes $" + cantidad_dolares + ' dolares.') # Muestra resultado
else:
    print('Ingresa una opción correcta por favor')