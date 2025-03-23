#Ingresa un numero que sera evaluado en positivo, negativo o cero
number = int(input("Ingresa un numero : "))
if number> 0 : print(number, "es positivo.")
elif number< 0 : print(number, "es negativo.")
else : print("El numero es 0.")
#Ingresa un numero que sera digitado como una edad ya sea menor o mayor
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
#Ingresa una contraseña
contraseña = input("Ingresa la contraseña: ")
#verificar si es correcta la contraseña
if contraseña == "secreto123":
    print("Contraseña coincidida")
else:
    print("Contraseña no coincidida.")
#Ingresa tres numeros que seran para establecer el mayor
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
mayor = max(num1, num2, num3)
print(f"El número mayor es: {mayor}")
#Ingresa una nota
nota = float(input("Ingresa una nota entre 0 y 100: "))
if 90 <= nota <= 100:
    print("Calificación: Excelente")
elif 70 <= nota < 90:
    print("Calificación: Aprobado")
elif 0 <= nota < 70:
    print("Calificación: Reprobado")
else:
    print("Nota fuera de rango")