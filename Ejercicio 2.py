Alumnos = {}
while True:
    "(1)" == "Añadir Alumno"
    nombre = input ("Nombre:")
    x =  (input ("Aprobado o Desaprobado:"))
    Alumnos[nombre] = x
    print (Alumnos)
    "(2)" == "Numero de aprobados"
    if Alumnos.values() == "Aprobado":
        print ("El numero de aprobados es:", +1)
        
        "(3)" == "Mostrar todo el alumnado"
    print (Alumnos.keys())