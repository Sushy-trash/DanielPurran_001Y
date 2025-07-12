########################
###zona de trabajo######
########################
productos={'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
stock={'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32],'GF75HD': [749990,2],
'UWU131HD': [349990,1]}
def stock_marca(marca):
    total=0
    for modelo,datos in productos.items():
        if datos[0].lower()==marca.lower():
            total +=stock[modelo][1]
    print(f"el stock es:{total}")
def busqueda_precio(p_min,p_max):
            resultado=[]
            for modelo,datos in stock.items():
                precio,cantidad=datos
                if p_min<=precio <= precio<=p_max and  cantidad>0:
                    marca=productos[modelo][0]
                    resultado.append(f"{marca}--{modelo}")
            if resultado:
                resultado.sort()
                print(f"los notebooks entre los precios consultados son: {resultado}")
            else:
                print("no hay noteboks en ese rango de precio")
  
def eliminar_producto(modelo):
        if modelo in productos and modelo in stock:
            del productos[modelo]
            del stock[modelo]
            return True
        else:
            return False
#############################
#######Menu principal########
#############################

print("Bienvenido a la tienda tecnologicas Psycho-Mantis.\n1)stock de marca.\n2)busqueda de precio.\n3)eliminar producto.\n4)Salir")
opcion=int(input("opcion:"))
if opcion==1:
    marca=input("ingrese la marca: ")
    stock_marca(marca)
elif opcion==2:
    while True:
        try:
            p_min=int(input("ingrese valor minimo: "))
            p_max=int(input("ingrese valor maximo: "))
            break
        except ValueError:
               print("debe ingresar valores enteros!!")
    busqueda_precio(p_min,p_max)
elif opcion==3:
    while True:
        modelo=input("ingrese el modelo a actualizar:")
        resultado=eliminar_producto(modelo)
        if resultado:
             print("producto eliminado!!")
        else:
             print("el modelo no existe")
        continuar=input("desea eliminar otro producto?(s/n):" )
        if continuar!="s":
             break  
elif opcion==4:
    while True:
     print("programa finalizado.")
     break 
else:
     print("debe seleccionar una opcion")
               
 
            
    
