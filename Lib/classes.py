'''class art:
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
class carrito():
    def __int__(self, idcart):
        self.idcart = idcart
        self.articulos = []
        pass
    def __str__(self):
        printCarrito = f'Carrito número: {self.idcart}'
        for i in range(0,len(self.articulos),1):
            printCarrito += f'Articulos: {self.articulos[i]}'
        return printCarrito
    def addArticulo(self, idArt):
        self.articulos.append(idArt)
        return 0
    pass'''
class art():
    def __init__(self,id,marca,nombre,precio=None,peso=None,descuento=None,inv=None):
        self.id= id
        self.marca= marca
        self.nombre= nombre
        self.precio= precio
        self.peso= peso
        self.descuentos= descuento
        self.inv= inv
        pass
    def __str__(self):
        return f"id: {self.id} - marca: {self.marca} - nombre: {self.nombre} - precio: {self.precio} - peso: {self.peso} - descuentos: {self.descuento} - inv: {self.inv}"
    def setPrecio(self,precio):
        self.precio =precio
        return 0
    def setPeso(self,peso):
        self.peso =peso
        return 0
    def setMarca(self,marca):
        self.marca =marca
        return 0
    def setNombre(self,nombre):
        self.nombre =nombre
        return 0
    def setDescuento(self,descuento):
        self.descuento =descuento
        return 0
    def setInv(self,inv):
        self.inv =inv
        return 0
    def setId(self,id):
        self.id =id
        return 0
class carrito():
    def __int__(self, idcart):
        self.idcart = idcart
        self.articulos = []
        pass
    def __str__(self):
        printCarrito = f'Carrito número: {self.idcart}'
        for i in range(0,len(self.articulos),1):
            printCarrito += f'Articulos: {self.articulos[i]}'
        return printCarrito
    def addArticulo(self, idArt):
        self.articulos.append(idArt)
        return 0

        pass