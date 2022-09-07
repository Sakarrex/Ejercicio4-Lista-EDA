from ListaEncadena import ListaEncadenada
if __name__ == "__main__":
    UnaLista = ListaEncadenada()
    switch = int(input("1: punto c\n2: punto d\n0: Fin\n"))
    while switch != 0:
        if switch == 1:
            UnaLista.puntoC(input("Ingresar Cargo: "))
        elif switch == 2:
            UnaLista.puntoD(input("Ingresar Materia: "),input("Ingresar Cargo:"),int(input("Ingresar Anio: ")))
        else:
            print("Codigo no valido")
        switch = int(input("1: punto c\n2: punto d\n0: Fin\n"))