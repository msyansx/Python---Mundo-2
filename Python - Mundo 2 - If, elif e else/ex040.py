from time import sleep 

print('='*50)
print("MÉDIA ESCOLAR")
print('='*50)

print("""Lembrando que:
Média menor que 5.0: Aluno reprovado.
Média entre 5.0 e 6.9: Aluno de recuperação.
Média acima de 7.0: Aluno aprovado.""")

aluno = str(input("\n\nDigite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

while nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
    print("\nNota inválida.")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    if nota1 > 0 and nota1 < 10 and nota2 > 0 and nota2 < 10: 
        break

media = float((nota1 + nota2) / 2)
    
print("""\nAguarde enquanto calculamos a sua média.""")
sleep(2)

if media < 0:
    print("\n\nValor inválido para nota. Por favor reveja as informações.")
elif media < 5.0:
    print("\nO aluno {} foi reprovado com media {}!".format(aluno, media))
elif media <= 6.9:
    print("\nO aluno {} está de recuperação por ter uma média {}.".format(aluno, media))
else:
    print("\nO aluno {} foi aprovado com uma média {}, Parabéns!".format(aluno, media))
 