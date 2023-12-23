# 1.Calculadora - Carlos Tovar - 20.12.2023

#Funcion para calcular
def operacion(oper,a,b):
    if oper == 1:
        return a+b
    elif oper == 2:
        return a-b
    elif oper == 3:
        return a*b
    elif oper == 4:
        return a/b
    else:
        print("Opción no valida")

#Hacemos la solicitud de datos
def inicio():
    opcion = int(input("Que quieres hacer hoy?\n1.Suma\n2.Resta\n3.Multiplicación\n4.Division\n"))
    num1 = float(input("Primer numero: "))
    num2 = float(input("\nSegundo numero: "))
    print("El resultado es: ",operacion(opcion,num1,num2))
    volver()

#Preguntamos si queremos repetirlo
def volver():
    opc = int(input("\nRepetir?"))
    if opc == 1:
        inicio()
    else:
        print("Hasta luego!")
#Aqui iniciamos el programa :D
inicio()