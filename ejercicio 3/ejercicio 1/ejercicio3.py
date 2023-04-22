# presentar la tabla de multiplicar de un numero ingresado por el usuario 

for n in range(1,10):
    print("---tabla" + str(n)+"---")
    for i in range(10): 
        rta = i*n
        print(i,"x",n,"=", rta)


# Bucle for

coleccion = {"juanchito":22,"maria":32,"jose":45,"luis":50}
for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")

coleccion = "marihuanero hp"

for i in coleccion:
       print(f"{i}", end = " ")