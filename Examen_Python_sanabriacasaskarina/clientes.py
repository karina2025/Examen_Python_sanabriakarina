import mensage
import json

def abrirArchivo():
    with open(".clientes.json","r") as abrirArchivo:
        return json.load()
    
    
def guardarArchivo():
    with open(".clientes.json","w") as abrirArchivo:
        return json.dump()
    
    
    
def usuarios():
    while (True):
        print(mensage.menuAdministrador)
        opcion=int(input('-> '))
        match opcion:
            case 1: 
                datos=abrirArchivo()
                usuarios= datos ["clientes"]
                cantidad=usuarios[ "clientes"]
                nombre=input("ingrese el nombre del usuario")
                apellido=input("ingrese el apellido del usuario")
                direccion=input("ingrese la direccion del usuario")
                contacto=input("ingrese el contacto del usuario")
                print(" nuevo usuario ingresado")
                encontrado=True
                guardarArchivo=(datos)
            case 2:
                datos=abrirArchivo()
                nombreusuario=input('Ingrese el nombre del ususario: ')
                for usuario in datos['campers']:
                    if str(usuario["nombre"]) == nombreusuario:
                        print(f"Nombres: {usuario['nombres']}\nApellidos: {usuario['apellidos']}\nDireccion: {usuario['direccion']}\nTelefono celular: {usuario['contacto']['celular']}\nTelefono ")
                        print("esto son todos los datos del usuario")
                        encontrado = True
                        guardarArchivo=(datos)
            case 3:
                break            
            case _:
                print(mensage.noValida)
                
                
                
                
                