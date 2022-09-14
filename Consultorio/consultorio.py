import datetime


class Consultorio:
    def __init__(self, direccion, nombre):
        self.direccion: str = direccion
        self.nombre = nombre
        self.lista_pacientes: list[Paciente] = []
        self.lista_agendas: list[Agenda] = []
        self.contador_meses: int = 1
        self.crear_agenda_mensual()

    def identificar_paciente(self, cedula):
        for paciente in self.lista_pacientes:
            if paciente.cedula == cedula:
                paciente_hallado = paciente
                return paciente_hallado
        return None

    def ingresar_paciente(self, nombre, cedula, fecha_de_nacimiento, celular):
        paciente = Paciente(nombre, cedula, fecha_de_nacimiento, celular)
        self.lista_pacientes.append(paciente)

    def obtener_mes(self, mes):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        if mes.lower() in meses:
            return meses.index(mes.lower()) + 1
        else:
            return None

    def obtener_nombre_mes(self, numero_mes):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return meses[numero_mes - 1]

    def dia_maximo_del_mes(self, mes):
        if mes == 2:
            return 28
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return 30
        else:
            return 31

    def asignar_cita_paciente(self, cedula: str, mes: str, dia: int, hora_militar: int):
        """
        La función asignará una cita al paciente
        :param cedula: str de la cédula del paciente
        :param mes: str del nombre del mes
        :param dia: int del día del mes
        :param hora_militar: int de la hora solicitada
        :return: 0 si la cita se agendó con éxito
        -1 si la cita solicitada ya esta ocupada
        -2 si la hora ingresada no es válida
        -3 si el día ingresado no es válido
        -4 si el mes ingresdao no existe
        -5 si el paciente ya tiene agendada una cita
        -6 si la cédula ingresada no está registrada
        """
        paciente = self.identificar_paciente(cedula)
        if paciente is not None:
            if not paciente.tiene_cita:
                numero_mes = self.obtener_mes(mes)
                if numero_mes is not None:
                    dia_maximo = self.dia_maximo_del_mes(numero_mes)
                    if dia > 0 and dia <= dia_maximo:
                        fecha = datetime.date(2022, numero_mes, dia)
                        if hora_militar >= 8 and hora_militar <= 17:
                            hora = datetime.time(hora_militar, 0)
                            for agenda in self.lista_agendas:
                                if agenda.fecha == fecha:
                                    for h in agenda.horario:
                                        if h.hora == hora:
                                            if h.paciente == None:
                                                h.paciente = paciente
                                                paciente.tiene_cita = True
                                                return 0
                                            else:
                                                return -1
                        return -2
                    return -3
                return -4
            return -5
        return -6

    def cancelar_cita_paciente(self, cedula):
        """
        La función cancelará la cita de un paciente
        :param cedula: str de la cedula del ususario
        :return: 0 si la cita se ha cancelado con éxito
        -1 si el usuario no tiene cita
        -2 si la cédula no está registrada
        """
        paciente = self.identificar_paciente(cedula)
        if paciente is not None:
            if paciente.tiene_cita:
                for agenda in self.lista_agendas:
                    for h in agenda.horario:
                        if h.paciente == paciente:
                            h.paciente = None
                            paciente.tiene_cita = False
                            return 0
            return -1
        return -2

    def crear_agenda_mensual(self):
        """
        Este requisito creará la agenda para un mes entero, el algoritmo determinará automáticamente cuál mes sigue y cuantos días tendrá
        :return: str nombre_mes Devolverá el nombre del mes si el procesos es exitoso
        -1 si ya se han completado todos los meses del año
        """
        if self.contador_meses < 12:
            numero_dias = self.dia_maximo_del_mes(self.contador_meses)
            nombre_mes = self.obtener_nombre_mes(self.contador_meses)
            for x in range(1, numero_dias + 1):
                agenda = Agenda(datetime.date(2022, int(self.contador_meses), x))
                for numero_veces in range(0, 10):
                    agenda.horario.append(Cita(datetime.time(8 + numero_veces, 0)))
                self.lista_agendas.append(agenda)
            self.contador_meses += 1
            return nombre_mes
        return -1


class Agenda:

    def __init__(self, fecha):
        self.fecha: datetime.date = fecha
        self.horario: list[Cita] = []


class Cita:
    def __init__(self, hora):
        self.hora: datetime.time = hora
        self.paciente: Paciente = None


class Paciente:
    def __init__(self, nombre, cedula, fecha_nacimiento, celular):
        self.nombre: str = nombre
        self.cedula: str = cedula
        self.fecha_nacimiento: datetime.date = fecha_nacimiento
        self.celular: str = celular
        self.tiene_cita: bool = False