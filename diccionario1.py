mi_diccionario = []
import os
sw = True



def fnt_agregar(diccionario, codigo_persona , nombre, apellido, contacto, correo, edad, estrato, sexo, telefono):
    if codigo_persona == '' or nombre == '' or apellido == '' or contacto == '' or edad == '' or estrato == '' or sexo == '' or telefono == '':
        print('¡¡Tienes que rellenar todos los espacios!!')   
    else:
        if sexo == 'm' or sexo == 'M' and edad >= 15 and edad <=25 and estrato >= 1 and estrato <= 2:
            diccionario[codigo_persona] = {'nombre': nombre, 'Apellido': apellido, 'Contacto': contacto, 'Correo': correo, 'Edad': edad, 'Estrato': estrato, 'Sexo': sexo, 'Telefono': telefono}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')
        
def fnt_registro(op):
    os.system('cls')
    if op == 1:
        codigo = input('Código: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        contacto = input('Contacto: ')
        correo = input('Correo: ')
        edad = int(input('Edad: '))
        estrato = int(input('Estrato: '))
        sexo = input('Sexo(M - F): ')
        telefono = input('Telefono: ')
        fnt_agregar(mi_diccionario, codigo, nombre, apellido, contacto, correo, edad, estrato, sexo, telefono)
        
        
while sw == True:
    os.system('cls')
    print('¡Bienvenido al sistema de registro de personas!!')
    op = int(input('¿Que quieres hacer?\n1 - Registrar\n2 - Salir\n'))
    if op == 1:
        fnt_registro(op)
    elif op == 2:
        sw = False
    else:
        print('¡Opción no valida!!')
    