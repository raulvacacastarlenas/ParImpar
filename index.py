#PAR O IMPAR
print("Hola, bienvenido a par o impar, introduce un número:")

numero = input()

def parimpar(numero):
        if int(numero) % 2 == 0:
            print(numero +" Es un numero par")
            

        elif int(numero) < 0:
            print("Adeu")
        

        else:
            print(numero + " Es un numero impar")
   
if numero.isdigit():
     print("bien")
else:
    print("El valor introducido no es un numero")
    while numero.isdigit() != True:
        print("Introduce un numero, no valen los otros caracteres") 
        numero = input()
        
parimpar(numero)

while int(numero) >= 0:
    print("Introduce otro numero:")
    numero = input()
    parimpar(numero)
