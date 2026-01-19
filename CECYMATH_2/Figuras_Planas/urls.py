from django.urls import path
from .views import addon_figuras

urlpatterns = [
    path("addon_/figuras_planas", addon_figuras, name='addon_figuras'),
]
