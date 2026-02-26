print("---Bienvenido al programa---\n---CALCUTRON 3000---")

usur_guard = "alexjavce"
contr_guard = "salsa123"

usur_ = input("Ingresa tu nombre de usuario: ")
while usur_ != usur_guard:
    usur_ = input("INCORRECTO, Ingresa nuevamente tu usuario: ")
if usur_ == usur_guard:
    print("-Usuario correcto, anteriormente registrado-")

contr_ = input("\nIngresa tu contraseña: ")
while contr_ != contr_guard:
    contr_ = input("INCORRECTO, Ingresa nuevamente la contraseña: ")


if usur_ == usur_guard and contr_ == contr_guard:
    print(f"---CREDENCIALES CORRECTAS---\nBienvenido {usur_guard} al programa")

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
print("(mas operaciones)Cargando...")
