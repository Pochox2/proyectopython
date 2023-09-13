import json

DB = {}

def register(DB): 
        user = input("Ingrese el usuario que desea tener \n")
        password = input("Ingrese la contraseña que desea tener \n")
        DB.update({user:password})

def open_data(DB):
        with open("data.txt", "r") as file:
               content = file.read()
               DB = json.loads(content)
               return DB

DB = open_data(DB)

def show_data(DB):
       print("Datos registrados: ", DB)

def login ():
        user = input("Ingrese nombre de usuario")
        password = input("Ingrese contraseña")
        try:
                if DB[user] == password:
                  print("Inicio de sesion exitoso")
                else:
                 print("Contraseña incorrecta")
        except KeyError:
               print("El usuario no existe")
               

def save_data(DB):
        with open ("data.txt", "w") as file:
                file.write(json.dumps(DB))


# a = int(input("Ingrese 1 si desea ingresar al menu, de lo contrario ingrese cualquier otro numero \n"))

# while (a == 1) :
#         os.system("cls")
#         print ("Bienvenido al menú de usuarios. Ingrese el numero de la operacion que desea realizar: \n 1. Registrar usuario \n 2. Loguearse \n 3. Ver datos de usuarios") 
#         b = int(input())
#         if b==1: 
#                 register(DB)
#                 save_data(DB)
#         elif b == 2:
#                 login()
#         elif b == 3:
#                 show_data(DB)
#         else:
#                 print("La opcion elegida no es correcta")
#         a = int(input("Si desea seguir navegando en el menu ingrese 1: "))
# else: 
#         print("Muchas gracias por usar el menu")