print("Evaluación N°1 Programación y Redes Virtualizadas")
integrante1 = input("Por favor, ingrese el nombre del primer integrante de la evaluacion: ")
integrante2 = input("Por favor, ingrese el nombre del segundo integrante de la evaluacion: ")
integrante3 = input("Por favor, ingrese el nombre del tercer integrante de la evaluacion: ")

print("Los integrantes son: ", integrante1)
print("Los integrantes son: ", integrante2)
print("Los integrantes son: ", integrante3)

nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")
seccion = input("Ingrese la sección del alumno: ")
sede = input("Ingrese la sede del alumno: ")

aclList = int(input("Cual es el número de ACL IPV4? "))
if aclList >= 1 and aclList <= 99:
    print("Esta es una ACL IPv4 estándar.")
elif aclList >=100 and aclList <= 199:
    print("Esta es una ACL IPv4 extendida")
else:
    print("Esta ACL IPv4 no es extendida ni estandar .")
