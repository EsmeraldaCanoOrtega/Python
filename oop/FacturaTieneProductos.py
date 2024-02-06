#   📌 Lo importante esta abajo
class Producto:
    contador_productos = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto._generar_siguiente_valor()
        self._nombre = nombre
        self._precio = precio
#   GET
    @property
    def nombre (self):
        return self._nombre
#   SET
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

#   📌Se podría utilizar esta manera GET y SET se utiliza un metodo menos(mas eficiente)
#   pero es menos legible

#     def get_nombre (self):
#         return self._nombre
#
#     def set_nombre (self, nombre):
#         self._nombre = nombre

    @property
    def id_producto(self):
        return self._id_producto
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
class Orden:
    contador_ordenes = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_orden = Orden._generar_siguiente_valor()
#   📌 La siguiente recoge una lista de productos
        self._productos = list(productos)

    @property
    def id_orden (self):
        return self._id_orden
    @property
    def productos (self):
        return self._productos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            #   📌 utilizamos el metodo del objeto producto str que devuelve una cadena
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 100.00)
    producto3 = Producto('Calcetines', 50.00)
    producto4 = Producto('Blusa', 50.00)

    productos1 = [producto1, producto2]
    productos2 = [producto3, producto4]

    orden1 = Orden(productos1)
    orden1.agregar_producto(producto3)
    orden1.agregar_producto(producto4)
    print(orden1)
    print(f'Total orden1: {orden1.calcular_total()}')

    for producto in orden1.productos:
        if producto == producto1:
            print(f'Si esta {producto.__str__()}')