
#   ESTACIÓN        MESES
#   Verano          enero-febrero-marzo
#   Otoño           abril-mayo-junio
#   Invierno        julio-agosto- septiembre
#   Primavera       octubre-noviembre- diciembre

#dado un mes, decidir a qué estación pertenece
mes = input("Ingresar nombre de mes: ")

if mes == 'enero' or mes == 'febrero' or mes == 'marzo':
    print('La estación es verano')
elif mes == 'abril' or mes == 'mayo' or mes == 'junio':
    print('La estación es otoño')
elif mes == 'julio' or mes == 'agosto' or mes == 'septiembre':
    print('La estación es invierno')
elif mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre':
    print('La estación es primavera')
else:
    print('No ingresaste un mes que yo conozca')