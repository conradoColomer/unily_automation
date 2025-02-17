usuarios = [
    {"usuario": "admin", "contraseña": "admin123"},
    {"usuario": "invitado", "contraseña": "invitado123"},
    {"usuario": "test", "contraseña": "test123"}
]

for index,user in enumerate(usuarios):
    if index == 0:
        print("First user is... ")

    print(f"The user name is: {user['usuario']}")
    print((f"The user name is: {user['contraseña']}"))

    if index != len(usuarios) -1:
        print("Next user is.....")