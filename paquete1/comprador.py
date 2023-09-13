# import manejousers

class Cliente:

    
    
    def __init__(self, nombre, apellido, celular, correo, BD):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.correo = correo
        self.compras = 0
        self.precio = 0
        BD.update({nombre:{
            "Nombre" : nombre,
            "Apellido" : apellido,
            "Celular" : celular,
            "Correo" : correo,
            "Compras" : self.compras,
            "Precio" : self.precio,
        }})

        # manejousers.save_data(BD)

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido} \nCorreo: {self.correo}"
    

    def mostrar_deuda(self):
        return f"La deuda es de: {self.precio}" 

    def comprar(self, nombre, prod , BD):
        Productos = {"Laptop":500, 
                 "iPhone": 600,
                 "Heladera": 900 
                 }
        self.compras = self.compras + 1
        precio = Productos[prod]
        self.precio = self.precio + precio
        try:
            BD.update({nombre:{"Compras":self.compras, "Precio":self.precio}})
            print(f"Compra realizada, monto: {precio}")
            # manejousers.save_data(BD)
        except:
            print("Error al ingresar usuario")
