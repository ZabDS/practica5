import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

def concatCads(pila):
    aux = ""
    for cadena in pila:
        aux = aux + cadena
    return aux

pilaDir = []

while True:
    opc = input("Ingrese una de las siguientes opciones\n"
                "1.-Crear un archivo\n"
                "2.-Leer un archivo\n"
                "3.-Escribir en un archivo\n"
                "4.-Renombrar un archivo\n"
                "5.-Leer directorio\n"
                "6.-Crear directorio\n"
                "7.-Borrar directorio\n"
                "8.-Mover a directorio\n"
                "9.-Salir\n")
    if int(opc) == 1:
        FileName = input("Ingrese el nombre del archivo ")
        FileName = concatCads(pilaDir) + FileName
        print(s.CreateF(FileName))
    if int(opc) == 2:
        FileName = input("Ingrese el nombre del archivo ")
        FileName = concatCads(pilaDir) + FileName
        print(s.ReadF(FileName))
    if int(opc) == 3:
        FileName = input("Ingrese el nombre del archivo ")
        FileName = concatCads(pilaDir) + FileName
        datos = input("Ingrese lo que requiera escribir en el archivo: ")
        print(s.WriteF(FileName,datos))
    if int(opc) == 4:
        FileName = input("Ingrese el nombre del archivo ")
        NFileName = input("Ingrese el nuevo nombre del archivo ")
        FileName = concatCads(pilaDir) + FileName
        print(s.RNameF(FileName,NFileName))
    if int(opc) == 5:
        print(s.RDir(concatCads(pilaDir)))
    if int(opc) == 6:
        DirName = input("Ingrese el nombre del directorio ")
        DirName = concatCads(pilaDir) + DirName
        print(s.MDir(DirName))
    if int(opc) == 7:
        DirName = input("Ingrese el nombre del directorio ")
        DirName = concatCads(pilaDir) + DirName
        print(s.RMDir(DirName))
    if int(opc) == 8:
        DirName = input("Ingrese el nombre del directorio ")
        if DirName == "..":
            del pilaDir[len(pilaDir)-1]
        elif(s.RDir(concatCads(pilaDir) + DirName) == -1):
            print("Error, no existe el directorio")
        else:
            DirName = DirName + "/"
            pilaDir.append(DirName)
    if int(opc) == 9:
        break
    else:
        print("Elija una opcion válida")
    
    
        
        