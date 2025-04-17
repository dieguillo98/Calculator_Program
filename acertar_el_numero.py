import random
numero_secreto = random.randint(1,1000)

acierto = False

for intentos in range(1,11,1):
    print(f'Intento numero: {intentos}')
    numero_ingresado = int(input('Ingrese el valor que piensa que es el numero a adivinar: '))
    if numero_ingresado > numero_secreto:
        print("Demasiado alto")
    elif numero_ingresado < numero_secreto:
        print('Demasiado bajo')
    else:
        print(f'EXITO!!!... Lo adivinaste en el intento numero: {intentos}')
        acierto = True
        break
if intentos == 10 and not acierto:
    print(f'ERROR!!!... No pudiste adivinar, el numero secreto era: {numero_secreto}')
