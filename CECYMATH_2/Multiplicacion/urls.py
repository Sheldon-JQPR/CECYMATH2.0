from django.urls import path
from .views import addon_multiplicacion

urlpatterns = [
    path("addon_/multiplicacion", addon_multiplicacion, name='addon_multiplicacion'),
]
