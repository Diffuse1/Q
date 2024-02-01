class art:
    def __init__(self,marca,id, nombre,precio=None,kg=None,descuento=None,piezas=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.kg = kg
        self.descuentos = descuento
        self.id = id
        self. piezas = piezas
        pass
class cart(art):
    def __init__(self, marca, nombre, precio, kg, descuento, id, piezas,articulo, preciofinal,iva,ahorro):
        super().__init__(marca, nombre, precio, kg, descuento, id, piezas)
        self.articilo = articulo
        self.preciofinal = preciofinal
        self.iva = iva
        self.ahorro = ahorro
        pass
    def __str__(self):
        return f"id: {self.id} - marca: {self.marca} - nombre: {self.nombre} - precio: {self.precio} - kg: {self.kg} - descuentos: {self.descuentos} - piezas: {self.piezas}"