print('Generador de listas')
x=int(input('¿Cuántas listas quiere escribir?'))
lista=[0]*x
for i in range(0,x):
    print('Digame cuantas palabras tiene la lista', i+1, ':')
    y=int(input())
    lista[i]=[0]*y
    for y in range(0,y):
        print('Digame la palabra', y+1, ': ')
        lista[i][y]=input()
        
for i in range (0,x):
    print('La lista',i+1,'es: ', lista[i])



    