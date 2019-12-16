from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('', views.SenhaViewSet)
router.register('categoria', views.CategoriaViewSet)
router.register('tipo', views.TipoViewSet)
router.register('fila', views.FilaViewSet)

app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
]