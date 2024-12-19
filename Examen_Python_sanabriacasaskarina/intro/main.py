import mensage
import clientes
import json

print(mensage.menuAdministrador)

while(True):
    print(mensage.menuEleccion)
    eleccion=int(input('-> '))
    match eleccion:
        case 1:
            clientes.usuarios()
        case 2:
       
            break    
        case _:
            print(mensage.noValida)
           
    


