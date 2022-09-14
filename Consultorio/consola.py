from Consultorio.consultorio import Consultorio


class UIConsola:

    def __init__(self):
        self.opciones = {
            "1": self.registrar_paciente,
            "2": self.agendar_cita,
            "3": self.cancelar_cita,
            "4": self.agregar_mes,
            "5": self.salir
        }
        self.consultorio = Consultorio("Carrera 70b #9-123", "Salud Increible")

    def mostrar_menu(self):
        print("""
        \n
        MENU DE OPCIONES
        =====================
        1. Registrar paciente
        2. Agendar cita
        3. Cancelar cita
        4. Crear nueva agenda mensual
        5. Salir
        =====================
        """)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def registrar_paciente(self):
        print("""\n >>> REGISTRAR PACIENTE""")
        print("Ingresa los datos del paciente: \n")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        fecha_nacimiento = input("Fecha de nacimiento: ")
        celular = input("Celular: ")
        self.consultorio.ingresar_paciente(nombre, cedula, fecha_nacimiento, celular)
        print("El usuario ha sido ingresado con éxito")

    def agendar_cita(self):
        print("""\n >>> AGENDAR CITA""")

        cedula = input("Ingrese la cédula: ")
        print("Ingrese la fecha de este año en la que requiere la cita")
        mes = input("Mes: ")
        dia = int(input("Día: "))
        print("Tenemos un horaio de atención de 8:00 a 17:00 hrs")
        hora = int(input("Ingrese la hora deseada en horario militar: "))

        resultado = self.consultorio.asignar_cita_paciente(cedula, mes, dia, hora)
        if resultado == -6:
            print(f"ERROR: La cédula {cedula} no esta registrada")
        elif resultado == -5:
            print("ERROR: El usuario ya tiene una cita agendada")
        elif resultado == -4:
            print("ERROR: El mes ingresado no existe")
        elif resultado == -3:
            print("ERROR: El día ingresado no es válido")
        elif resultado == -2:
            print("ERROR: La hora ingresada no es válida")
        elif resultado == -1:
            print("ERROR: La hora solicitada ya está ocupada")
        else:
            print("La cita se ha agendado con éxito")

    def cancelar_cita(self):
        print("""\n >>> CANCELAR CITA""")

        cedula = input("Ingrese la cédula: ")
        resultado = self.consultorio.cancelar_cita_paciente(cedula)

        if resultado == -2:
            print(f"ERROR:La cédula {cedula} no está registrada")
        elif resultado == -1:
            print("ERROR: El usuario no tiene cita agendada")
        else:
            print("La cita se ha cancelado con éxito")

    def agregar_mes(self):
        print("""\n >>> CREAR NUEVA AGENDA MENSUAL""")

        resultado = self.consultorio.crear_agenda_mensual()
        if resultado == -1:
            print("ERROR: Ya han sido creadas todas las agendas mensuales del año 2022")
        else:
            print(f"La nueva agenda mensual de {resultado} ha sido creada exitosamente")

    def salir(self):
        print("\n MUCHAS GRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)

