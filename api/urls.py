from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'rol', views.RolViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'dtsusuario', views.DatosUsuarioViewSet)
router.register(r'local', views.LocalViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'talla', views.TallaViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'productoimagen', views.ProductoImagenViewSet)
router.register(r'oferta', views.OfertaViewSet)
router.register(r'cupon', views.CuponViewSet)
router.register(r'articulocarrito', views.ArticuloCarritoViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'pqrinfo', views.PQRInformacionViewSet)
router.register(r'pqrrespuest', views.PQRRespuestaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="Shoes_company API"))
]
