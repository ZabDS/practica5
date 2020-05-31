from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import shutil

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    
with SimpleXMLRPCServer(('127.0.0.1', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def createFile(fileName):
        cmd = "touch ./ShareDir/" + fileName
        if os.system(cmd) == 0:
            return("Archivo Creado")
        else:
            return("Error al crear el archivo")
    
    def readFile(fileName):
        pathFile="./ShareDir/" + fileName
        try:
            fp=open(pathFile,'r')
            return fp.read()
            fp.close()
        except FileNotFoundError:
            return "Error al abrir el archivo"
    
    def writeFile(fileName,data):
        pathFile="./ShareDir/" + fileName
        try:
            fp=open(pathFile,'a')
            fp.write(data)
            return("Archivo escrito")
        except FileNotFoundError:
            return "Error al abrir el archivo"
        
    def renameFile(fileName,newFileName):
        cmd = "mv ./ShareDir/" +fileName+" ./ShareDir/"+newFileName
        if os.system(cmd) == 0:
            return("Archivo renombrado")
        else:
            return("Error al renombrar archivo")
    
    def readDir(dirName):
        cmd = "./ShareDir/" + dirName
        try:
            return os.listdir(cmd)
        except FileNotFoundError:
            return -1
    
    def makeDir(dirName):
        cmd = "./ShareDir/" + dirName
        try:
            os.mkdir(cmd,0o777)
            return "Directorio creado correctamente"
        except FileExistsError:
            return "Error, el directorio ya existe"
    
    def removeDir(dirName):
        cmd = "./ShareDir/" + dirName
        try:
            shutil.rmtree(cmd)
            return "Directorio borrado correctamente"
        except FileNotFoundError:
            return "Error, el directorio no existe"
        
    
    server.register_function(createFile, 'CreateF')
    server.register_function(readFile, 'ReadF')
    server.register_function(writeFile, 'WriteF')
    server.register_function(renameFile, 'RNameF')
    server.register_function(readDir, 'RDir')
    server.register_function(makeDir, 'MDir')
    server.register_function(removeDir, 'RMDir')
    
    server.serve_forever()
