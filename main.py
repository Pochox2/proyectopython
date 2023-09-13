from paquete1.comprador import Cliente
from paquete1.manejousers import open_data

BD = {}
BD = open_data(BD)
cliente1 = Cliente("Leandro", "Insua", 3364234543, BD)
cliente1.comprar("Leandro", 5500, BD)