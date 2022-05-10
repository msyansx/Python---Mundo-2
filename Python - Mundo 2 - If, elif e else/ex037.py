print("\033[31m="*50)
print("CONVERTENDO NÚMEROS EM DIFERENTES BASES")
print("="*50,'\033[m')

while True:
    
    print("-----"*5)
    num = int(input("Digite o valor a ser convertido: "))
    print("-----"*5)
    menu = int(input('''Deseja converter para qual base? 
    [1] - Binário
    [2] - Hexadecimal
    [3] - Octal
    [4] - Sair\n\n'''))

    if menu == 4:
        print("\n\033[34mObrigado por usar este código.\033[m\n")
        break
    #OCTAL
    elif menu == 3:
        x = []
        while num > 0:
            resultado = num // 8
            resto = num % 8
            x.insert(0, resto)

            num = resultado
        print(x)

    #HEXADECIMAL
    elif menu == 2:
        x = []
        while num > 0:
            resultado = num // 16
            resto = num % 16        

            if resto == 10:
                resto = 'a'
            elif resto == 11:
                resto = 'b'
            elif resto == 12:
                resto = 'c'
            elif resto == 13:   
                resto = 'd'
            elif resto == 14:
                resto = 'e'
            elif resto == 15:
                resto = 'f'

            num = resultado
            x.insert(0, resto)

        print(x)

    #BINARIO
    elif menu == 1:
        while num > 0:
            resultado = num // 2
            resto = num % 2
            x.insert(0, resto)

            num = resultado 
        print(x)
    
#elif menu == 4:
    
#-----------------------------------------------------------------------------------------------------

#while menu <= 0 or menu >= 4:
#    print("Por favor digite uma das 3 opções.")
#    menu = int(input("""Deseja converter para qual base? 
#[1] - Binário
#[2] - Hexadecimal
#[3] - Octal\n\n"""))
#
#if menu == 1:
#   print("O número {} em binário é: {}".format(num, format(num, "b"))) 
#elif menu == 2:
#    print("O número {} em hexadecimal é: {}".format(num, format(num, "x")))
#else:
#    print("O número {} em octal é: {}".format(num, format(num, "o"))) 




#-----------------------------------------------------------------------------------------------------
#n = int(input("Digite um número: "))
#print("------"*5)
#print("[1] HEXADECIMAL")
#print("[2] BINÁRIO")
#print("[3] OCTAL")
#
#enun = int(input("DIGITE A OPÇÃO QUE DESEJA CONVERTER: "))
#
#if enun == '1': 
#    hexadecimal = int(hex(n)[2:])
#    print("O valor em hexadecimal é {}".format(hexadecimal))
#elif enun == '2':
#    binario = int(bin(n))
#    print("O valor em binário é {}".format(binario)[2:])
#elif enun == '3':
#    octal = int(oct(n))
#    print("O valor em octal é {}".format(octal)[2:])