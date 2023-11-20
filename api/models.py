from django.db import models

class Rol(models.Model):
    rol_nombre = models.CharField(max_length=30)
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class Usuario(models.Model):
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    estado = models.BooleanField()
    pwd_cambio = models.BooleanField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class DatosUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(null=True)
    tipo_documento = models.CharField(max_length=5, null=True)
    num_documento = models.IntegerField()
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class Local(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    nit = models.CharField(max_length=9)
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class Categoria(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=25)

class Talla(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    talla = models.IntegerField()

class Producto(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=7, decimal_places=3)
    color = models.CharField(max_length=9)
    marca = models.CharField(max_length=15)
    genero = models.CharField(max_length=10)
    disponible = models.IntegerField()
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class ProductoImagen(models.Model):
    image_path = models.CharField(max_length=255)
    created = models.DateTimeField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Oferta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_oferta = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class Cupon(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class ArticuloCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    datos_usuario = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class Pedido(models.Model):
    articulo = models.ForeignKey(ArticuloCarrito, on_delete=models.CASCADE)
    datos_usuario = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)
    pedido_fecha = models.DateField()
    estado = models.BooleanField()
    creation_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class PQRInformacion(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    datos_usuario = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)
    tipo_peticion = models.CharField(max_length=255)
    descripccion = models.CharField(max_length=255)
    archivo = models.CharField(max_length=255, null=True)
    estado = models.BooleanField()
    tiempo_restante = models.DateTimeField()
    fecha_de_respuesta = models.DateTimeField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)

class PQRRespuesta(models.Model):
    pqr = models.ForeignKey(PQRInformacion, on_delete=models.CASCADE)
    descripcion_respuesta = models.CharField(max_length=255)
    estado = models.BooleanField()
    fecha_de_respuesta = models.DateTimeField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)
    delete_at = models.DateTimeField(null=True)
