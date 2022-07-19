usuarios = {}
opcion = ''
while opcion != '3':
    if opcion == '1':
       
        nombre = input("Ingrese el su primer nombre: ")
        dni = int(input("Ingrese el número de su DNI: "))
        edad = int(input("Ingrese su edad: "))
        persona = {'Nombre': nombre, 'DNI': dni, 'Edad': edad}
        almacenamiento= edad
        usuarios[almacenamiento] = persona
    if opcion == '2':
        print("Se muestra la lista de usuarios registrados: ")
        
        for dat in sorted(usuarios.values(), key=lambda value: value['Edad']):
            print(dat)
    opcion=input("Opciones\n(1) Insertar Datos\n(2) Ver lista de registrados\n(3) Cerrar programa:\nElija un número: ")
