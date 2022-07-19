print('Generador de listas')
x=int(input('¿Cuantas listas quiere escribir? '))
Lista=[0]*x
for i in range(0,x):
    print('Digame cuantas palabras tiene la lista',i+1,': ')
    y=int(input())
    Lista[i]=[0]*y
    for y in range(0,y):  
        print('Digame la palabra',y+1,': ')
        Lista[i][y]=input()

for i in range(0,x):
    print('La lista',i+1,'es: ',Lista[i])