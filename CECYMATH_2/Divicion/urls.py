from django.urls import path
from .views import addon_division

urlpatterns = [
    path("addon_/division", addon_division, name='addon_division'),
]
