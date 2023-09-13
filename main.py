from paquete1.comprador import Cliente
from paquete1.manejousers import *

BD = {}

cliente1 = Cliente("Leandro", "Insua", 3364234543, "leooinsua79@gmail.com", BD)
cliente1.comprar("Leandro", "iPhone", BD)
cliente1.comprar("Leandro", "Laptop", BD)
print(cliente1.__str__())
print(cliente1.mostrar_deuda())