from rest_framework import viewsets

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

from .serializer import RolSerializer
from .serializer import UsuarioSerializer
from .serializer import DatosUsuarioSerializer
from .serializer import LocalSerializer
from .serializer import CategoriaSerializer
from .serializer import TallaSerializer
from .serializer import ProductoSerializer
from .serializer import ProductoImagenSerializer
from .serializer import OfertaSerializer
from .serializer import CuponSerializer
from .serializer import ArticuloCarritoSerializer
from .serializer import PedidoSerializer
from .serializer import PQRInformacionSerializer
from .serializer import PQRRespuestaSerializer



class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DatosUsuarioViewSet(viewsets.ModelViewSet):
    queryset = DatosUsuario.objects.all()
    serializer_class = DatosUsuarioSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TallaViewSet(viewsets.ModelViewSet):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.all()
    serializer_class = ProductoImagenSerializer

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class ArticuloCarritoViewSet(viewsets.ModelViewSet):
    queryset = ArticuloCarrito.objects.all()
    serializer_class = ArticuloCarritoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PQRInformacionViewSet(viewsets.ModelViewSet):
    queryset = PQRInformacion.objects.all()
    serializer_class = PQRInformacionSerializer

class PQRRespuestaViewSet(viewsets.ModelViewSet):
    queryset = PQRRespuesta.objects.all()
    serializer_class = PQRRespuestaSerializer
