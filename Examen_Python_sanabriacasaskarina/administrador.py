import json
import mensage


def abrirArchivo():
    with open(".clientes.json","r") as abrirArchivo:
        return json.load()
    
    
def guardarArchivo():
    with open(".clientes.json","w") as abrirArchivo:
        return json.dump()
    
    
    
    def usuarios():
        while(True):
            print(mensage.menuAdministrador)
            opcion=int(input('->'))
            match opcion:
                case 1:
                     datos=abrirArchivo()
                     nuevoNombre=input('Ingresa los nuevos nombres: ')
                     usuarios['nombres']=nuevoNombre
                     print(mensage.valida)
                     guardarArchivo=()
                     
                case 2: 
                    datos=abrirArchivo()
                    nuevoApellido=input('ingrese los nuevos apellidos: ')
                    usuarios['apellidos']=nuevoApellido
                    print(mensage.valida)
                    guardarArchivo=()
                    
                case 3:
                    datos=abrirArchivo()
                    nuevaDireccion=input('ingrese la nueva direccion: ')
                    usuarios['direccion']=nuevaDireccion
                    print(mensage.valida)
                    guardarArchivo=()
                    
                case 4:
                    datos=abrirArchivo()
                    nuevoContacto=input('ingrese el nuevo contacto: ')
                    usuarios['contacto']=nuevoContacto
                    print(mensage.valida)
                    guardarArchivo=()
                    
                case 5:
                    break
                case _:
                    print(mensage.noValida)
                    
                    
                    
                    
                    
                    
                    
    
                    
                    
                    
                    
                    
                    

                    
        