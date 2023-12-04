from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TarjetaViewSet, TarjetaCreditoViewSet, TarjetaDebitoViewSet
from .views import CuentaViewSet, CajaAhorroViewSet, CuentaCorrienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'cajas-ahorro', CajaAhorroViewSet)
router.register(r'cuentas-corriente', CuentaCorrienteViewSet)
router.register(r'tarjetas', TarjetaViewSet)
router.register(r'tarjetas-credito', TarjetaCreditoViewSet)
router.register(r'tarjetas-debito', TarjetaDebitoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # otras rutas de tu aplicación
]
#en el frontend se debe persistir el tarjeta_numero cuando se hace get cuenta/api/tarjetas/(customer_id), luego se realiza otra petición get cuenta/api/tarjetas-credito/(tarjeta_numero)
#lo mismo para cuentas, se debe guardar el account id y luego hacer get en cajas-ahorro y cuentas-corriente