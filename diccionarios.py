def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    #     'llave4': 4
    # }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 320258236,
        'Colombia': 50372424
    }

    # print(poblacion_paises['Mexico'])

    # for pais in poblacion_paises.keys(): # Devuelve las llaves
    # for pais in poblacion_paises.values(): # Devuelve los valores
    for pais, poblacion in poblacion_paises.items(): # Devuelve llave y valor
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == "__main__":
    run()