nome  = str(input("Qual é o seu nome? "))

if nome == "Yan":
    print("Que nome maravilhoso!")
elif nome == "João" or nome == "Lucas" or nome == "Matheus":
    print("Teu nome é bem comum no Brasil.")
elif nome in 'Ana Claudia Paula Fernanda':
    print("Belo nome feminino!")
else: 
    print("Seu nome é normal.")
    
print("Tenha um bom dia, {}!".format(nome))