# ejercicio de  Matemática (Vir)
# ejercicio de Programacion (Mante)

################################# PROGRAMACION ##########################################################
# Se provee el encabezado de una función python con 3 parámetros (a,b,c) que son números enteros.
# Se deben resolver los siguientes incisos de manera independiente, pero siempre dentro del cuerpo de la función
# - Mostrar "a es el mayor" si a es el mayor de los 3 números
# - Mostrar "b está en el medio" si a y c son iguales y además b es mayor que a pero menor que c
# - Mostrar "c no es el mayor" si c no es el mayor de los 3 números
# - Evaluar si alguna de las leyendas nunca se mostrará. Justificar la decisión.
def funcMensajes(a, b, c):
    #insertar código aquí
   if a>b and a>c:
       print ("a es el mayor")
   if a==c and b>a and  b<c:
       print ("b está en el medio")
   if not (c>a and c>b):
       print("c no es el mayor")



