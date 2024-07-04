import time
import os
import csv


cliente = []
nt = "─"*36
n = 0
pedidos = ("saco 5kg", "saco 10kg", "saco 20kg")
contador = True 
error = "error en la opcion."


archivo = 'cliente.csv'

if os.path.exists(archivo):
    os.system("cls")
else:
    sistema = ("cliente", "sacos 5kg", "saco 10kg", "saco 20kg")
    sistema_str = "      ".join(sistema)
    os.system("cls")
    with open('cliente.csv','w') as archivo:
        archivo.write(sistema_str + '\n')

    with open('pedidos.csv', 'w', newline='') as archivo1:
        escritor_csv = csv.writer(archivo1)
        escritor_csv.writerow(sistema)
    
    with open('direccion.csv', 'w', newline='') as archivo2:
        escritor_csv = csv.writer(archivo2)
        escritor_csv.writerow(sistema)
        
    with open('secctor.csv', 'w', newline='') as archivo3:
        escritor_csv = csv.writer(archivo3)
        escritor_csv.writerow(sistema)
    
    
def borrar(b):
    time.sleep(b)
    os.system("cls")
    
def menu1():
    global contador
    while contador == True:
        print(f"menu de CatPremiun \n{nt}")
        print(f"1) agregar usuario: \n2) ingresar a datos: \n3) salir:")
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        if eleguir in [1,2,3]:
            borrar(0.5)
            return(eleguir)
        else:
            print("no es una opcion")
            borrar(1)
            
def clientes():
    global contador
    while contador == True:
        print(f"escriba su usuario \n{nt}")
        nombre = input("──> ")
        apellido = input("ahora ingrese su apellido \n──> ")
        nombre_apellido = nombre + " " + apellido
        borrar(0.5)
        while contador == True:
            print(f"estas seguro que deseas agregar este nombre? ──> {nombre_apellido} (s/n)\n{nt}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                cliente.append(nombre_apellido)
                borrar(0.5)
                contador = False
            elif eleguir in ["n", "N"]:
                borrar(0.5)
                break
            else:
                print("no es una opcion")
                borrar(1)
    contador = True
            
def pedido():
    global n, contador
    while contador == True:
        n = 0
        print(f"selecione un pedido \n{nt}")
        for i in pedidos:
            n += 1
            print(f"{n}) {i}")
            time.sleep(0.1)
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        if eleguir in [1,2,3,4,5]:
            eleguir -= 1
            cliente.append(pedidos[eleguir])
            break
        else:
            print("no es una opcion")
            borrar(1)
            
def sacos():
    global contador
    while contador == True:
        print(f"ingrese la cantidad de sacos \n{nt}")
        try:
            sacos = float(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        while contador == True:
            print(f"esta bien la cantidad de sacos? ──> {sacos} (s/n) \n{nt}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                sacos_str = str(sacos)
                cliente.append(sacos_str)
                borrar(0.5)
                contador = False
            elif eleguir in ["n", "N"]:
                borrar(0.5)
                break
    contador = True
    sacos_str = str(sacos)
    cliente.append(sacos_str)

def guardar():
    cliente_str = '     '.join(cliente)
    with open('clientes.csv','a') as archivo:
        archivo.write(cliente_str + '\n')
    
    pedido = cliente[1].replace(" ", "_")
    with open(f'{pedidos}.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(cliente)
    cliente.clear()
            
def menu2():
    print(f"que datos quieres ver? \n{nt}")
    print("1) pedidos \n2) clientes \n3) direccion")
    eleguir = int(input("seleccione su opcion: "))
    return(eleguir)
    
while contador == True:
    m = menu1()
    borrar(0.5)
    if m == 1:
        clientes()
        borrar(0.5)
        pedido()
        borrar(0.5)
        sacos()
        guardar()
    elif m == 2:
        f = menu2()
        if f == 1:
            with open('pedidos.csv', 'r', newline='') as archivo3:
                lector_csv = csv.reader(archivo3)
                for i in lector_csv:
                    print(i)
        elif f == 2:
            with open('clientes.csv','r') as file:
                for i in file:
                    print(i + '\n')
                    time.sleep(0.2)
        elif f == 3:
            with open('direccion.csv','r') as file:
                for i in file:
                    print(i + '\n')
                    time.sleep(0.2)
        #solo sirve para volver no sirve para nada este input
        input("presione cualquier enter para volver....")
        borrar(0.5)
    elif m == 3:
        print("saliendo...")
        contador = False