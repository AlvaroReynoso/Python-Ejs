import random
from faker import Faker

# Instancia de Faker
fake = Faker()

# Crear el archivo SQL
with open("datos_falsos.sql", "w") as file:

    # Función para generar datos falsos y una sola sentencia INSERT para 'paciente'
    def generar_pacientes(n):
        sql = "INSERT INTO paciente (nombre, telefono, email, fecha_nac) VALUES\n"
        values = []
        for _ in range(n):
            nombre = fake.name()
            telefono = fake.phone_number()
            email = fake.email()
            fecha_nac = fake.date_of_birth(minimum_age=18, maximum_age=90)
            values.append(f"('{nombre}', '{telefono}', '{email}', '{fecha_nac}')")
        sql += ",\n".join(values) + ";\n"
        file.write(sql)

    # Función para generar datos falsos y una sola sentencia INSERT para 'doctor'
    def generar_doctores(n):
        especialidades = ['Cardiología', 'Neurología', 'Pediatría', 'Dermatología', 'Gastroenterología']
        sql = "INSERT INTO doctor (nombre, telefono, email, fecha_nac, especialidad) VALUES\n"
        values = []
        for _ in range(n):
            nombre = fake.name()
            telefono = fake.phone_number()
            email = fake.email()
            fecha_nac = fake.date_of_birth(minimum_age=25, maximum_age=65)
            especialidad = random.choice(especialidades)
            values.append(f"('{nombre}', '{telefono}', '{email}', '{fecha_nac}', '{especialidad}')")
        sql += ",\n".join(values) + ";\n"
        file.write(sql)

    # Función para generar datos falsos y una sola sentencia INSERT para 'cita'
    def generar_citas(n):
        sql = "INSERT INTO cita (fecha_cita, id_doctor, id_paciente) VALUES\n"
        values = []
        for _ in range(n):
            fecha_cita = fake.date_time_this_year()
            id_doctor = random.randint(1, 5)  # Asume que tienes entre 1 y 5 doctores
            id_paciente = random.randint(1, 10)  # Asume que tienes entre 1 y 10 pacientes
            values.append(f"('{fecha_cita}', {id_doctor}, {id_paciente})")
        sql += ",\n".join(values) + ";\n"
        file.write(sql)

    # Función para generar datos falsos y una sola sentencia INSERT para 'diagnostico'
    def generar_diagnosticos(n):
        diagnosticos = ['Gripe', 'Migraña', 'Fractura', 'Gastritis', 'Infección Respiratoria']
        sql = "INSERT INTO diagnostico (nombre, id_doctor, id_paciente, id_cita) VALUES\n"
        values = []
        for _ in range(n):
            nombre_diagnostico = random.choice(diagnosticos)
            id_cita = random.randint(1, 20)  # Asume que tienes entre 1 y 20 citas
            id_doctor = random.randint(1, 5)  # Asume que tienes entre 1 y 5 doctores
            id_paciente = random.randint(1, 10)  # Asume que tienes entre 1 y 10 pacientes
            values.append(f"('{nombre_diagnostico}', {id_doctor}, {id_paciente}, {id_cita})")
        sql += ",\n".join(values) + ";\n"
        file.write(sql)

    # Función para generar datos falsos y una sola sentencia INSERT para 'tratamiento'
    def generar_tratamientos(n):
        tratamientos = ['Reposo', 'Antibióticos', 'Cirugía', 'Fisioterapia', 'Dieta Especial']
        sql = "INSERT INTO tratamiento (descripcion, id_diagnostico) VALUES\n"
        values = []
        for _ in range(n):
            descripcion = random.choice(tratamientos)
            id_diagnostico = random.randint(1, 15)  # Asume que tienes entre 1 y 15 diagnósticos
            values.append(f"('{descripcion}', {id_diagnostico})")
        sql += ",\n".join(values) + ";\n"
        file.write(sql)

    # Llamadas para generar datos y escribirlos en el archivo SQL
    generar_pacientes(10)     # Generar 10 pacientes en un solo INSERT
    generar_doctores(5)       # Generar 5 doctores en un solo INSERT
    generar_citas(20)         # Generar 20 citas en un solo INSERT
    generar_diagnosticos(15)  # Generar 15 diagnósticos en un solo INSERT
    generar_tratamientos(10)  # Generar 10 tratamientos en un solo INSERT
