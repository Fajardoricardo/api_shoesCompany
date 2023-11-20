from rest_framework import serializers
from .models import Rol
from .models import Usuario
from .models import DatosUsuario
from .models import Local
from .models import Categoria
from .models import Talla
from .models import Producto
from .models import ProductoImagen
from .models import Oferta
from .models import Cupon
from .models import ArticuloCarrito
from .models import Pedido
from .models import PQRInformacion
from .models import PQRRespuesta


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DatosUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosUsuario
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoImagen
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = '__all__'

class ArticuloCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloCarrito
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PQRInformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQRInformacion
        fields = '__all__'

class PQRRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQRRespuesta
        fields = '__all__'

