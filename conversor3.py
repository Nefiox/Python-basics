def conversor(tipo_pesos, valor_dolar):
    print("Convertir de pesos " + tipo_pesos + " a dolares")
    print("Valor de 1 USD = $" + str(valor_dolar) + " pesos "+ tipo_pesos)
    cantidad_pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? ")
    cantidad_pesos = float(cantidad_pesos) # float permite números decimales
    cantidad_dolares = cantidad_pesos / valor_dolar # Calcula la cantidad de dolares
    cantidad_dolares = round(cantidad_dolares, 2) # Redondea decimales
    cantidad_dolares = str(cantidad_dolares) # Convierte tipo número a string 
    print("---> Tienes $" + cantidad_dolares + ' dolares <----') # Muestra resultado
    

menu = """
Bienvenido al conversor de monedas a dolares 💵🤑
1 - Pesos colombianos
2- Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 20)
else:
    print('Ingresa una opción correcta por favor')