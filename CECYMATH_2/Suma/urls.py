from django.urls import path
from .views import addon_suma

urlpatterns = [
    path("addon_/suma",addon_suma, name='addon_suma'),
]