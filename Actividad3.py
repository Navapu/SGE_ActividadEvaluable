# Utilizando una lista para almacenar usuarios y contraseñas
usuarios_contrasenas_lista = [
    ["usuario1", "contrasena1"],
    ["usuario2", "contrasena2"],
    ["usuario3", "contrasena3"],
    ["usuario4", "contrasena4"],
    ["usuario5", "contrasena5"]
]

# Realizar dos consultas
consulta_usuario1 = "usuario3"
consulta_usuario2 = "usuario6"

# Consulta 1
for usuario, contrasena in usuarios_contrasenas_lista:
    if usuario == consulta_usuario1:
        print(f"Contraseña para {usuario}: {contrasena}")
        break
else:
    print(f"Usuario {consulta_usuario1} no encontrado.")

# Consulta 2
for usuario, contrasena in usuarios_contrasenas_lista:
    if usuario == consulta_usuario2:
        print(f"Contraseña para {usuario}: {contrasena}")
        break
else:
    print(f"Usuario {consulta_usuario2} no encontrado.")


# Utilizando un diccionario para almacenar usuarios y contraseñas
usuarios_contrasenas_diccionario = {
    "usuario1": "contrasena1",
    "usuario2": "contrasena2",
    "usuario3": "contrasena3",
    "usuario4": "contrasena4",
    "usuario5": "contrasena5"
}

# Realizar dos consultas
consulta_usuario1 = "usuario3"
consulta_usuario2 = "usuario6"

# Consulta 1
if consulta_usuario1 in usuarios_contrasenas_diccionario:
    contrasena1 = usuarios_contrasenas_diccionario[consulta_usuario1]
    print(f"Contraseña para {consulta_usuario1}: {contrasena1}")
else:
    print(f"Usuario {consulta_usuario1} no encontrado.")

# Consulta 2
if consulta_usuario2 in usuarios_contrasenas_diccionario:
    contrasena2 = usuarios_contrasenas_diccionario[consulta_usuario2]
    print(f"Contraseña para {consulta_usuario2}: {contrasena2}")
else:
    print(f"Usuario {consulta_usuario2} no encontrado.")
