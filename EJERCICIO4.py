def tribonacchi(posición):
    if posición > 2:
        result = tribonacchi(posición-1) + tribonacchi(posición-2) + tribonacchi(posición-3)
        #print(result)
    elif posición == 2:
        result=1
        #print(result)
    elif posición == 1:
        result=1
        #print(result)
    else:
        result=0
        #print(result)
    return result

num=int(input('Escriba la posicion del termino para la sucesion tribonacci: '))

print(tribonacchi(num))