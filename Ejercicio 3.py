usuarios = {}
opcion = ''
while opcion != '3':
    if opcion == '1':
       
        nombre = input("Ingrese el su primer nombre: ")
        edad = input("Ingrese su edad: ")
        dni = input("Ingrese el número de su DNI: ")
        telefono = input("Ingrese su número telefónico: ")
        persona = {'Nombre': nombre, 'Edad': edad, 'DNI': dni, 'Teléfono': telefono}
        almacenamiento= nombre
        usuarios[almacenamiento] = persona

    if opcion == '2':
        print("Se muestra la lista de usuarios registrados: ")
        for key in usuarios.values():
            print(key)
    if opcion != '1' or '2' or '3':
        print("La opcion que ha elegido es incorrecta por favor vuelva a intentarlo")
    opcion=input("Opciones\n(1) Insertar Datos de Usuario\n(2) Ver lista de usuarios registrados\n(3) Cerrar el programa:\nElija un número: ")