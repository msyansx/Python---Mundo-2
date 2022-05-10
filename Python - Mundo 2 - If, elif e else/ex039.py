from time import sleep
from datetime import date

print('='*50)
print("ALISTAMENTO NO EXÉRCITO")
print('='*50)

print('_'*50)
print("BEM VINDO AO EXÉRCITO BRASILEIRO")
print('_'*50)

nome = str(input("\nQual é o seu nome? "))
nasc = int(input("Em que ano você nasceu? "))
ano_atual = date.today().year
alist = 18
idade = ano_atual - nasc

print("\n\nOlá {}, seja bem vindo ao exército Brasileiro!".format(nome))
print("Aguarde um momento para analisarmos se você deve se alistar...\n")
sleep(3)

print("A sua idade é {}.\n".format(ano_atual - nasc))

if idade == alist:
    print("Você está na idade certa para se alistar no exército!!!")
elif idade <= 0:
    print("Idade inválida, por favor reveja as informações.")
elif idade > alist:
    print("""Já se passaram {} ano(s) que você deveria ter se alistado.
    Deve correr para não se prejudicar com o governo.""".format(idade - alist))
elif idade < alist:
    print("Ainda faltam {} ano(s) para você poder se alistar!".format(alist - idade))
