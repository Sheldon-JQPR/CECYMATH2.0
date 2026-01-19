from django.urls import path
from .views import addon_polinomios

urlpatterns = [
    path("addon_/polinomios", addon_polinomios, name='addon_polinomios'),
]
