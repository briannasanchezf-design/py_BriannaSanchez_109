'''
Crea un programa en Python que pida al usuario un numero secreto (por ejemplo el 7).
El programa seguira pidiendo al usuario que adivine hasta que acierte.
Agregar mensajes que diga si es menor o menor al numero por adivinar
Limitarlo a cierta cantidad de intentos

Necesito ahora configurar mi juego
(Pedir mi numero secreto)
(Numero de intentos maximos)

Menu
=============
1) Ingresar los valores para configurar
2) Que el usuario juegue
3) Que el usuario pueda pedir salir del juego aun no habiendo completado los numeros de intentos


'''

numero_secreto=5
# numero_secreto = random.randint(1,10)
intentos = 0
max_intentos=5

while True :
 numeroadivinar=int(input("Adivina un numero entre el 1 al 10 :"))
 intentos=intentos + 1
 if numeroadivinar==numero_secreto :
    print("Adivinaste el numero ")
    break
 elif numeroadivinar>numero_secreto :
     print("El numero es mayor al numero secreto")
 else:
     print("El numero es menor al numero secreto")

 if intentos ==max_intentos:
   continuar = input(" Has alcanzado el límite de intentos. ¿Deseas continuar jugando? (s/n): ").lower()
   if continuar== "s" :
      intentos=0
   else:
      print("Gracias por jugar")
      break