import manejousers

class Cliente:

    
    def __init__(self, nombre, apellido, celular, BD):
        self.nombre = nombre
        self.apellido = apellido
        self.compras = 0
        self.precio = 0
        self.celular = celular
        BD.update({nombre:{
            "Nombre" : nombre,
            "Apellido" : apellido,
            "Celular" : celular,
            "Compras" : self.compras,
            "Precio" : self.precio,
        }})
        manejousers.save_data(BD)

    def __str__(self):
        return f"Nombre: {self.nombre}"
    

    def mostrar_deuda(self):
        return f"La deuda es de: {self.precio}" 

    def comprar(self, nombre, precio, BD):
        self.compras = self.compras + 1
        self.precio = self.precio + precio
        try:
            BD.update({nombre["Compras":self.compras, "Precio":self.precio]})
            manejousers.save_data(BD)
        except:
            print("Error al ingresar usuario")
