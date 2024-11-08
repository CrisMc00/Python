class Cola:
    
    def __init__(self):
        self.max = 5
        # self.cola = [5, 2, 4, 7, 1]
        self.cola = [''] * self.max
        self.Inicio = -1
        self.Fin = -1

    def Inicializar(self):
        self.Inicio = -1
        self.Fin = -1

    def Mostrar(self):
        if self.Inicio == -1:
            print("Cola Vacía")
        else:
            if self.Inicio <= self.Fin:
                for i in range(self.Inicio, self.Fin + 1):
                    print(i , " -> " , self.cola[i])
            else:
                for i in range(self.Inicio, self.max):
                    print(i , " -> " , self.cola[i])
                for i in range(0, self.Fin + 1):
                    print(i , " -> " , self.cola[i])

    def Insertar(self):
        if self.Fin == self.Inicio - 1 or (self.Inicio == 0 and self.Fin == self.max - 1):
            print("Cola Llena")
        else:
            v = int(input("Ingrese el valor a insertar: "))
            if self.Inicio != -1:
                print("1. inicio")
                print("2. fin")
                opcion = int(input("Introduce la opcion: "))
            else:
                opcion = 2
            
            if opcion == 1:
                if self.Inicio == -1:
                    self.Inicio = 0
                    self.Fin = 0
                    self.cola[self.Inicio] = v
                if self.Inicio > 0:
                    self.Inicio -= 1
                    self.cola[self.Inicio] = v
                if self.Inicio == 0:
                    self.Inicio = self.max - 1
                    self.cola[self.Inicio] = v
            else: 
                if self.Fin == self.max - 1:
                    self.Fin = 0
                else:
                    self.Fin += 1
                if self.Inicio == -1:
                    self.Inicio = 0
                self.cola[self.Fin] = v

    def Eliminar(self):
        if self.Inicio == -1:
            print("Cola Vacia")
            t = None
        else:
            t = self.cola[self.Inicio]
            if self.Inicio == self.Fin:
                self.Inicio = -1
                self.Fin = -1
            else:

                print("1. inicio")
                print("2. fin")
                opcion = int(input("Introduce la opcion: "))

                if opcion == 1:
                    if self.Inicio == self.max - 1:
                        self.Inicio = 0
                    else:
                        self.Inicio += 1
                else:
                    if self.Fin == 0:
                        self.Fin = self.max - 1
                    else:
                        self.Fin -= 1

        return t

class Menu: 

    cola = Cola()

    while True:  # Bucle infinito hasta que el usuario decida salir
        print("1. Inicializar")
        print("2. Mostrar")
        print("3. Insertar")
        print("4. Eliminar")
        print("5. Creditos")
        print("6. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':  # Compara con cadenas de texto
            cola.Inicializar()
            input("Presiona enter para volver al menu")

        elif opcion == '2':
            cola.Mostrar()
            input("Presiona enter para volver al menu")

        elif opcion == '3':
            
            cola.Insertar()
            input("Presiona enter para volver al menu")

        elif opcion == '4':
            cola.Eliminar()
            input("Presiona enter para volver al menu")

        elif opcion == '5':
            print("Desarrolladores:")
            print("Jared Baldelamar Ortega Matricula: 23170092")
            print("Cristian Adrian Mata Chairez Matricula: 23170091")
            print("Victor Gael Barajas Vazquez Matricula> 23170083")
            print("Materia: Estructura de Datos")
            print("Profesor: Jesus Adrian Burciaga Perez")
            input("Presiona enter para volver al menu")

        elif opcion == '6':
            print("Gracias por usar el programa")
            break  
    