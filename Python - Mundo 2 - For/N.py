
lc =  int(input("Quantidade de linhas e colunas: "))

#J REPRESENTA COLUNA
#I REPRESENTA LINHA


#UMA POSSÍVEL MANEIRA DE FAZER
#for i in range(0, lc+1):
#    for j in range(0, lc+1):
#        if i == j or (i >= j and j == 0) or (i <= j and j == lc):
#            print(" N ", end=' ')
#        else: 
#            pri#nt("   ", end=' ')
#    print("\n")#

#UMA SEGUNDA MANEIRA DE FAZER
for i in range(0, lc+1):
    for j in range(0, lc+1):
        if i == j or j == 0 or j == lc:
            print(" E ", end=' ')
        else: 
            print("   ", end=' ')
    print("\n")


