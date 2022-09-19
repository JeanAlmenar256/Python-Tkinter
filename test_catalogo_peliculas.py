from Dominio.Peliculas import Peliculas
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp


opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar Pelicula ')
        print('2. Listar Peliculas ')
        print('3. Eliminar Catalogo ')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese nombre de la pelicula: ')
            pelicula = Peliculas(nombre_pelicula)
            cp.agregar_pelicula(nombre_pelicula)
        elif opcion == 2:
            cp.listar_pelicula()

        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        print(type(e))
        opcion = None