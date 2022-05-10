from time import sleep  

print("="*50)
print("ANALISANDO TRIANGULOS")
print("="*50)

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

print("\nUm momento...")
sleep(2)

while a <= 0 or b <= 0 or c <= 0:
    print("\n\nValor inválido, por favor tente novamente.")
    a = float(input("\nDigite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    c = float(input("Digite o terceiro valor: "))
 
while a + b <= c or b + c <= a or a + c <= b:
    print("Não é possível formar um triângulo com estes valores.")   
    a = float(input("\nDigite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    c = float(input("Digite o terceiro valor: "))
     
if a == b and a != c or b == c and b != a or a == c and a != b:
    print("\nSerá formado um triângulo ISÓSCELES.")
elif a == b and b == c and a == c:
    print("\nVocê terá um triãngulo EQUILÁTERO")
else: 
    print("\nVocê terá um triângulo ESCALENO")