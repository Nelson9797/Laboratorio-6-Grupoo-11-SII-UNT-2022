n=int(input('Ingresa el número de filas: '))
Lista=[0]*(n*2-1)
for j in range(0,n):
        p=0
        k=0
        for i in range(n-1-j,n+j):
            if p==0:
                k=k+1
                Lista[i]=k
                p=1
            elif p==1:
                Lista[i]=' '
                p=0
        for i in range(0,n*2-1):
            if Lista[i]==0:
                Lista[i]=' '
            print(Lista[i],end='')
        print('')
            
        
