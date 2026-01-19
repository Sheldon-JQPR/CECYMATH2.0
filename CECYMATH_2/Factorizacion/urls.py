from django.urls import path
from .views import addon_factorizacion

urlpatterns = [
    path("addon_/factorizacion", addon_factorizacion, name='addon_factorizacion'),
]
