import re

Opcion = 0
while Opcion != 6:
    print('\nSELECCIONE UNA OPCION')
    print('1. Variables válidas')
    print('2. Enteros y decimales')
    print('3. Operadores aritméticos')
    print('4. Operadores relacionales')
    print('5. Palabras reservadas')
    print('6. Salir')

    Opcion = int(input("OPCION QUE DECEA REALIZAR : "))

    if Opcion == 1:
        print('VARIABLES VALIDAS')
        filename = 'Documento_Practica.txt'
        textfile = open(filename, "r")
        regexs = "[0-9]+\s?\+\s?[0-9]+"
        regexr = "[0-9]+\s?\-\s?[0-9]+"
        regs = re.compile(regexs)
        regr = re.compile(regexr)
        for line in textfile:
            lista = regs.findall(line)
            print(lista)
            lista = regr.findall(line)
            print(lista)
        textfile.close()
    elif Opcion == 2:
        print('ENTEROS Y DECIMALES')
        filename = 'Documento_Practica.txt'
        textfile = open(filename, "r")
        regex = "[0-9]+\.?[0-9]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif Opcion == 3:
        print('OPERADORES ARITMETICOS')
        filename = 'Documento_Practica.txt'
        textfile = open(filename, "r")
        regex = "[\+\-\*\/\%]"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif Opcion == 4:
        print('OPERADORES RELACIONALES')
        filename = 'Documento_Practica.txt'
        textfile = open(filename, "r")
        regex = "\=[\=]|\![\=]|\<\=?|\>\=?"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif Opcion == 5:
        print('PALABRAS VALIDAS')
        filename = 'Documento_Practica.txt'
        textfile = open(filename, "r")
        regex = "assert|pass|and|as|break|class"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print('OPCION NO VALIDA')