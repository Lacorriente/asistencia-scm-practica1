

print("=== SISTEMA DE ASISTENCIA v2.0.0 ===")

contador_asistencias = 0

def registrar_asistencia(estudiante):
    global contador_asistencias

    dni = estudiante["dni"].strip()
    nombre = estudiante["nombre"]
    apellido = estudiante["apellido"]

    if len(dni) >= 7 and dni.isdigit():
        contador_asistencias += 1
        print(f"[OK] Asistencia registrada para: {nombre} {apellido}")
        print(f"DNI: {dni}")
        print(f"Total de asistencias registradas: {contador_asistencias}")
    else:
        print("[ERROR] DNI inválido")

# Registrar asistencias
registrar_asistencia({
    "dni": "40123456",
    "nombre": "Juan",
    "apellido": "Perez"
})

registrar_asistencia({
    "dni": "40123457",
    "nombre": "Maria",
    "apellido": "Gomez"
})


