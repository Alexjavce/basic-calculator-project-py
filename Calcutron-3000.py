print("---Bienvenido al programa---\n---CALCUTRON 3000---")

usuarios = []
contrasenas = []

usuario = input("Ingresa tu Usuario para guardar: ")
contrasena = input("Ingresa tu Contraseña para guradarlo: ")

usuarios.append(usuario)
contrasenas.append(contrasena)


usur_ = input("Ingresa tu nombre de usuario: ")
while usur_ != usuarios[0]:
    usur_ = input("INCORRECTO, Ingresa nuevamente tu usuario: ")
if usur_ == usuarios[0]:
    print("-Usuario correcto, anteriormente registrado-")

contr_ = input("\nIngresa tu contraseña: ")
while contr_ != contrasenas[0]:
    contr_ = input("INCORRECTO, Ingresa nuevamente la contraseña: ")


if usur_ == usuarios[0] and contr_ == contrasenas[0]:
    print(f"---CREDENCIALES CORRECTAS---\nBienvenido {usuarios[0]} al programa")

menu=1
while menu == 1:

    print("¿Deseas calcular areas de figuras geometricas o operaciones matematicas basicas?")
    men_option=int(input("Selecciona el numero de la opcion que desees calcular:\n1.Calculo de Areas\n2.Operaciones aritmeticas\nSeleccion:"))

    if men_option == 2:

        print("\n---Ingresa el numero correspondiente a la opcion que quieres calcular---\n")
        sel_usu=int(input("1.suma\n2.resta\n3.multiplicacion\n4.division\nSeleccion: "))

        match sel_usu:
            case 1: 
                print("--Seleccionaste suma--\n")
                elem_=int(input("selecciona cuantos numeros vas a sumar:"))
                if elem_ == 2:
                    num_a=float(input("ingresa primer numero: "))
                    num_b=float(input("ingresa el segundo numero: "))
                    print(f"la suma de {num_a} y {num_b} es:\n")
                    print(num_a+num_b)
                    input("")
                elif elem_ == 3:
                    num_a=float(input("ingresa el primer numero: "))
                    num_b=float(input("ingresa el segundo numero: "))
                    num_c=float(input("ingresa el tercer numero: "))
                    print(f"la suma de {num_a}, {num_b} y {num_c} es:\n")
                    print(num_a+num_b+num_c)
                    input("")
                elif elem_ == 4:
                    num_a=float(input("ingresa el primer numero: "))
                    num_b=float(input("ingresa el segundo numero: "))
                    num_c=float(input("ingresa el tercer numero: "))
                    num_d=float(input("ingresa el cuerto numero: "))
                    print(f"la suma de {num_a}, {num_b}, {num_c} y {num_d} es:\n")
                    print(num_a+num_b+num_c+num_d)
                    input("")
            case 2:
                print("--seleccionaste resta--\n")
                elem_=int(input("selecciona cuantos numeros vas a restar: "))
                if elem_ == 2:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    print(f"la resta entre {num_a} y {num_b} es: \n")
                    print(num_a-num_b)
                    input("")
                elif elem_ == 3:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    num_c=float(input("ingresa el tercer termino: "))
                    print(f"la resta entre {num_a}, {num_b} y {num_c} es: \n")
                    print(num_a-num_b-num_c)
                elif elem_ == 4:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    num_c=float(input("ingresa el tercer termino: "))
                    num_d=float(input("ingresa el cuarto termino: "))
                    print(f"la resta entre {num_a}, {num_b}, {num_c} y {num_d} es: \n")
                    print(num_a-num_b-num_c-num_d)
            case 3:
                print("--seleccionaste multiplicacion--\n")
                elem_=int(input("ingresa el numero de elementos que vas a multiplicar: "))
                if elem_ == 2:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    print(f"{num_a} por (x) {num_b} es: \n")
                    print(num_a*num_b)
                elif elem_ == 3:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    num_c=float(input("ingresa el tercer termino: "))
                    print(f"{num_a} por (x) {num_b} y por (x) {num_c} es: \n")
                    print(num_a*num_b*num_c)
                elif elem_ == 4:
                    num_a=float(input("ingresa el primer termino: "))
                    num_b=float(input("ingresa el segundo termino: "))
                    num_c=float(input("ingresa el tercer termino: "))
                    num_d=float(input("ingresa el cuarto termino: "))
                    print(f"{num_a} por (x) {num_b}, por (x) {num_c} y por {num_d} es: \n")
                    print(num_a*num_b*num_c*num_d)
            case 4:
                print("--seleccionaste division--\n")
                dividendo=float(input("ingresa el dividendo de la operacion: "))
                divisor=float(input("ingresa el divisor: "))
                print(f"{dividendo} dividido entre {divisor} es igual a:\n")
                print(dividendo/divisor)
                print(f"y el residuo(modulo) es: {dividendo%divisor}")

    elif men_option == 1:
        def a_cuadrado():
            lado=float(input("Ingresa la longitud de uno de los lados del cuadrado: "))
            print(f"El area de tu cuadrado es igual a {lado**2}")

        def a_triangulo():
            base=float(input("Ingresa la longitud de la base del triangulo: "))
            altura=float(input("Bien, Ahora necesito la altura del triangulo: "))
            print(f"El area de tu triangulo es {(base*altura)/2}")

        def a_circulo():
            diam=float(input("Ingresa el diametro del circulo: "))
            radio = diam / 2
            print(f"El area del circulo es: {3.1416 * (radio**2)}")

        print("---MiniCalcutron_Areas---")

        
        sel=int(input("Para que figura geometrica necesitas calcular su area:\n1. Cuadrado\n2. Triangulo\n3. Circulo\nSelección: "))

        if sel == 1:
            a_cuadrado()
        elif sel == 2:
            a_triangulo()
        elif sel == 3:
            a_circulo()
        else:
            print("Ingresa valor correcto")
menu=int(input("¿Requieres volver a calcular? (1 para sí, 0 para no): "))
