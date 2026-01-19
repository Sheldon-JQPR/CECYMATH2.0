from django.urls import path
from .views import addon_jerarquia

urlpatterns = [
    path("addon_/jerarquia_operaciones", addon_jerarquia, name='addon_jerarquia'),
]
