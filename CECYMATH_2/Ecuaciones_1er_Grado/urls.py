from django.urls import path
from .views import addon_ecuaciones

urlpatterns = [
    path("addon_/ecuaciones_1er_grado", addon_ecuaciones, name='addon_ecuaciones'),
]
